use rpsl::{object, parse_object};

#[test]
fn single_line_objects_display_correctly() {
    let expected = concat!(
        "role:           ACME Company\n",
        "address:        Packet Street 6\n",
        "address:        128 Series of Tubes\n",
        "address:        Internet\n",
        "email:          rpsl-parser@github.com\n",
        "nic-hdl:        RPSL1-RIPE\n",
        "source:         RIPE\n",
        "\n"
    );

    let borrowed = parse_object(expected).unwrap();
    let owned = object! {
        "role": "ACME Company";
        "address": "Packet Street 6";
        "address": "128 Series of Tubes";
        "address": "Internet";
        "email": "rpsl-parser@github.com";
        "nic-hdl": "RPSL1-RIPE";
        "source": "RIPE";
    };

    assert_eq!(borrowed.to_string(), expected);
    assert_eq!(owned.to_string(), expected);
}

#[test]
fn multi_line_objects_display_correctly() {
    let expected = concat!(
        "role:           ACME Company\n",
        "address:        Packet Street 6\n",
        "                128 Series of Tubes\n",
        "                Internet\n",
        "email:          rpsl-parser@github.com\n",
        "nic-hdl:        RPSL1-RIPE\n",
        "source:         RIPE\n",
        "\n"
    );

    let borrowed = parse_object(expected).unwrap();
    let owned = object! {
        "role": "ACME Company";
        "address": "Packet Street 6", "128 Series of Tubes", "Internet";
        "email": "rpsl-parser@github.com";
        "nic-hdl": "RPSL1-RIPE";
        "source": "RIPE";
    };

    assert_eq!(borrowed.to_string(), expected);
    assert_eq!(owned.to_string(), expected);
}
