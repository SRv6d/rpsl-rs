#![allow(clippy::missing_panics_doc, missing_docs)]

use std::{
    io::{BufRead, BufReader},
    time::Instant,
};

use flate2::read::GzDecoder;
use rpsl::parse_object;

const RIPE_DATABASE_URL: &str = "https://ftp.ripe.net/ripe/dbase/ripe.db.utf8.gz";

#[derive(Debug, Default)]
struct DatabaseStats {
    objects: usize,
    attributes: usize,
    decompressed_bytes: u64,
}

#[test]
#[ignore = "downloads and parses the complete RIPE database"]
fn current_ripe_database_parses() {
    let started = Instant::now();
    let DatabaseStats {
        objects,
        attributes,
        decompressed_bytes,
    } = parse_ripe_database(download_ripe_database());

    assert_ne!(objects, 0, "RIPE database contained no objects");
    eprintln!(
        "parsed {objects} objects with {attributes} attributes from \
         {decompressed_bytes} decompressed bytes in {:?}",
        started.elapsed(),
    );
}

fn download_ripe_database() -> impl BufRead {
    let response = ureq::get(RIPE_DATABASE_URL)
        .call()
        .expect("download the RIPE database");
    let decoder = GzDecoder::new(response.into_body().into_reader());
    BufReader::new(decoder)
}

fn parse_ripe_database(mut database: impl BufRead) -> DatabaseStats {
    let mut stats = DatabaseStats::default();
    let mut line = String::new();
    let mut object = String::with_capacity(1024);
    let mut line_number = 0_usize;
    let mut object_start_line = 0_usize;

    loop {
        line.clear();
        let bytes_read = database
            .read_line(&mut line)
            .expect("decompress the RIPE database as UTF-8");
        if bytes_read == 0 {
            break;
        }

        line_number += 1;
        stats.decompressed_bytes += bytes_read as u64;

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
