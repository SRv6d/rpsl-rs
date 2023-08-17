<div align="center">
  <a href="https://github.com/srv6d/rpsl-parser/actions">
    <img src="https://github.com/srv6d/rpsl-parser/workflows/CI/badge.svg" alt="CI status">
  </a>
  <a href="https://pypi.python.org/pypi/rpsl-parser">
    <img src="https://img.shields.io/pypi/v/rpsl-parser.svg" alt="PyPi version">
  </a>
  
</div>
<br>

An [RFC 2622] conformant Routing Policy Specification Language (RPSL) parser with a focus on speed and correctness. It is written in Rust and extensively leverages zero-copy, [outperforming other parsers](docs/benchmark) by a factor of 33-60x. To ensure robust parsing of any valid RPSL input, an exhaustive suite of [property based tests](tests/property_based/) is used.

## Example

```python
from rpsl_parser import parse_rpsl_object

role_acme = """
role:        ACME Company
address:     Packet Street 6
address:     128 Series of Tubes
address:     Internet
email:       rpsl-parser@github.com
nic-hdl:     RPSL1-RIPE
source:      RIPE
"""
parsed = parse_rpsl_object(role_acme)
print(parsed)
```

Prints the following:

```sh
(('role', ('ACME Company',)),
 ('address', ('Packet Street 6',)),
 ('address', ('128 Series of Tubes',)),
 ('address', ('Internet',)),
 ('email', ('rpsl-parser@github.com',)),
 ('nic-hdl', ('RPSL1-RIPE',)),
 ('source', ('RIPE',)))
```

[RFC 2622]: https://datatracker.ietf.org/doc/html/rfc2622
