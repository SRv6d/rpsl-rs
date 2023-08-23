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
💬 Able to parse objects directly from whois server responses\
🧠 Low memory footprint by leveraging zero-copy\
🧪 Robust parsing of any valid input ensured by Property Based Tests

## Examples

### Parsing RPSL

A string containing an object in RPSL notation can be parsed to a tuple with attribute name-value pairs.

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

```python
(('role', ('ACME Company',)),
 ('address', ('Packet Street 6',)),
 ('address', ('128 Series of Tubes',)),
 ('address', ('Internet',)),
 ('email', ('rpsl-parser@github.com',)),
 ('nic-hdl', ('RPSL1-RIPE',)),
 ('source', ('RIPE',)))
```

Since RPSL attribute values may be spread over multiple lines and values consisting only of whitespace are valid, the `tuple[str | None, ...]` type is used to represent them.

### Parsing a WHOIS server response

Whois servers often respond to queres with multiple objects.
An example ARIN query for `AS32934` will return with the requested `ASNumber` object first, followed by it's associated `OrgName`:

```
$ whois -h whois.arin.net AS32934
ASNumber:       32934
ASName:         FACEBOOK
ASHandle:       AS32934
RegDate:        2004-08-24
Updated:        2012-02-24
Comment:        Please send abuse reports to abuse@facebook.com
Ref:            https://rdap.arin.net/registry/autnum/32934


OrgName:        Facebook, Inc.
OrgId:          THEFA-3
Address:        1601 Willow Rd.
City:           Menlo Park
StateProv:      CA
PostalCode:     94025
Country:        US
RegDate:        2004-08-11
Updated:        2012-04-17
Ref:            https://rdap.arin.net/registry/entity/THEFA-3
```

To extract each individual object, the parse_whois_server_response function can be used as such:

```python
from rpsl_parser import parse_whois_server_response

parsed = parse_whois_server_response(AS32934)
print(parsed)
```

```python
((('ASNumber', ('32934',)),
  ('ASName', ('FACEBOOK',)),
  ('ASHandle', ('AS32934',)),
  ('RegDate', ('2004-08-24',)),
  ('Updated', ('2012-02-24',)),
  ('Comment', ('Please send abuse reports to abuse@facebook.com',)),
  ('Ref', ('https://rdap.arin.net/registry/autnum/32934',))),
 (('OrgName', ('Facebook, Inc.',)),
  ('OrgId', ('THEFA-3',)),
  ('Address', ('1601 Willow Rd.',)),
  ('City', ('Menlo Park',)),
  ('StateProv', ('CA',)),
  ('PostalCode', ('94025',)),
  ('Country', ('US',)),
  ('RegDate', ('2004-08-11',)),
  ('Updated', ('2012-04-17',)),
  ('Ref', ('https://rdap.arin.net/registry/entity/THEFA-3',))))
```

# 🚧 Work in progress

- ## More descriptive error messages
  When invalid RPSL is parsed, the current error messages do not properly convey where exactly the error is located in the parsed text.

## Installation

Using PyPI:

```
pip3 install rpsl-parser
```

[RFC 2622]: https://datatracker.ietf.org/doc/html/rfc2622
