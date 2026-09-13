use std::{
    env,
    fs::File,
    io::{BufRead, BufReader},
};

use rpsl::parse_object;

#[derive(Debug, Default)]
struct DatabaseStats {
    objects: usize,
    attributes: usize,
    bytes: u64,
}

fn main() {
    let database_path = env::args_os()
        .nth(1)
        .expect("usage: parse-ripe-database-rpsl-rs DATABASE");
    let database = BufReader::new(File::open(&database_path).expect("open the RIPE database"));
    let stats = parse_database(database);

    println!(
        "objects={} attributes={} bytes={}",
        stats.objects, stats.attributes, stats.bytes
    );
}

fn parse_database(mut database: impl BufRead) -> DatabaseStats {
    let mut stats = DatabaseStats::default();
    let mut line = String::new();
    let mut object = String::with_capacity(1024);
    let mut line_number = 0_usize;
    let mut object_start_line = 0_usize;

    loop {
        line.clear();
        let bytes_read = database
            .read_line(&mut line)
            .expect("read the RIPE database as UTF-8");
        if bytes_read == 0 {
            break;
        }

        line_number += 1;
        stats.bytes += bytes_read as u64;

        if object.is_empty() && (line.starts_with('#') || line.starts_with('%')) {
            continue;
        }

        if line == "\n" || line == "\r\n" {
            if !object.is_empty() {
                stats.attributes +=
                    parse_database_object(&object, object_start_line, stats.objects + 1);
                stats.objects += 1;
                object.clear();
            }
            continue;
        }

        if object.is_empty() {
            object_start_line = line_number;
        }
        object.push_str(&line);
    }

    if !object.is_empty() {
        stats.attributes += parse_database_object(&object, object_start_line, stats.objects + 1);
        stats.objects += 1;
    }

    assert_ne!(stats.objects, 0, "RIPE database contained no objects");
    stats
}

fn parse_database_object(source: &str, start_line: usize, object_number: usize) -> usize {
    let object_type = source
        .split_once(':')
        .map_or("<unknown>", |(object_type, _)| object_type);
    let object = parse_object(source)
        .map_err(|error| {
            let dump_line = start_line + error.line() - 1;
            format!(
                "failed to parse RIPE {object_type} object {object_number}, \
                 starting at dump line {start_line}; failure at dump line {dump_line}:\n{error}"
            )
        })
        .unwrap();

    object.len()
}
