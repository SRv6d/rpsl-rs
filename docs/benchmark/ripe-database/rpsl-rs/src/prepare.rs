use std::{
    env,
    fs::{self, File},
    io::{self, BufReader, BufWriter, Write},
    path::Path,
};

use flate2::read::GzDecoder;

const RIPE_DATABASE_URL: &str = "https://ftp.ripe.net/ripe/dbase/ripe.db.utf8.gz";

fn main() {
    let cache_dir = env::args_os()
        .nth(1)
        .expect("usage: prepare-ripe-database CACHE_DIRECTORY");
    prepare_database(Path::new(&cache_dir));
}

fn prepare_database(cache_dir: &Path) {
    fs::create_dir_all(cache_dir).expect("create RIPE database cache directory");

    let database_path = cache_dir.join("ripe.db.utf8");
    let cache_key_path = cache_dir.join("ripe.db.utf8.cache-key");
    let compressed_path = cache_dir.join("ripe.db.utf8.gz.part");
    let database_part_path = cache_dir.join("ripe.db.utf8.part");

    let mut response = ureq::get(RIPE_DATABASE_URL)
        .call()
        .expect("request the RIPE database");
    let cache_key = response
        .headers()
        .get("etag")
        .or_else(|| response.headers().get("last-modified"))
        .expect("RIPE database response to include an ETag or Last-Modified header")
        .to_str()
        .expect("RIPE database cache key to be valid ASCII")
        .to_owned();

    if database_path.is_file()
        && fs::read_to_string(&cache_key_path).is_ok_and(|cached| cached == cache_key)
    {
        println!("using cached RIPE database at {}", database_path.display());
        return;
    }

    println!("downloading {RIPE_DATABASE_URL}");
    let mut compressed_file = BufWriter::new(
        File::create(&compressed_path).expect("create temporary RIPE database archive"),
    );
    let mut body = response.body_mut().as_reader();
    io::copy(&mut body, &mut compressed_file).expect("download the RIPE database");
    compressed_file
        .flush()
        .expect("flush temporary RIPE database archive");
    drop(compressed_file);

    println!("decompressing RIPE database to {}", database_path.display());
    let compressed_file =
        BufReader::new(File::open(&compressed_path).expect("open temporary RIPE database archive"));
    let mut decoder = GzDecoder::new(compressed_file);
    let mut database_file =
        BufWriter::new(File::create(&database_part_path).expect("create temporary RIPE database"));
    let decompressed_bytes =
        io::copy(&mut decoder, &mut database_file).expect("decompress the RIPE database");
    database_file
        .flush()
        .expect("flush temporary RIPE database");
    drop(database_file);

    if database_path.exists() {
        fs::remove_file(&database_path).expect("remove stale cached RIPE database");
    }
    fs::rename(&database_part_path, &database_path).expect("install cached RIPE database");
    fs::write(&cache_key_path, cache_key).expect("record RIPE database cache key");
    fs::remove_file(&compressed_path).expect("remove temporary RIPE database archive");

    println!("prepared {decompressed_bytes} bytes");
}
