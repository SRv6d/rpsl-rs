<div align="center">
  <a href="https://github.com/srv6d/rpsl-parser/actions">
    <img src="https://github.com/srv6d/rpsl-parser/workflows/CI/badge.svg" alt="CI status">
  </a>
  <a href="https://pypi.python.org/pypi/rpsl-parser">
    <img src="https://img.shields.io/pypi/v/rpsl-parser.svg" alt="PyPi version">
  </a>
  <a>
    <img src="https://img.shields.io/badge/v3.7+-black?style=flat&color=FFFF00&label=Python" alt="python version">
  </a>
  
</div>
<br>

An [RFC 2622] conformant Routing Policy Specification Language (RPSL) parser with a focus on speed and correctness.

⚡️ Outperforms other parsers by a factor of 33-60x\
📰 Complete implementation for multiline RPSL values\
🧠 Low memory footprint by leveraging zero-copy\
🧪 Robust parsing of any valid input ensured by Property Based Tests

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

## Installation

Using PyPI:

```
pip3 install rpsl-parser
```

[RFC 2622]: https://datatracker.ietf.org/doc/html/rfc2622
