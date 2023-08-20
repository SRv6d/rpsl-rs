from typing import TypeAlias

from hypothesis import given, note, settings
from rpsl_parser import parse_rpsl_object, parse_whois_server_response

from property_based import strategies
from property_based.rpsl_test_types import (
    RpslAttributeMultiValue,
    RpslTextObject,
    RpslWhoisServerResponse,
    WhoisServerMessage,
)

_RpslAttributes: TypeAlias = list[str]


def rpsl_object_to_tuple(
    rpsl: RpslTextObject,
) -> tuple[tuple[str, tuple[str | None, ...]], ...]:
    """Convert a RPSL object to a tuple of attributes as returned by the parser."""
    return tuple(
        (
            attr.name,
            (attr.value,)
            if not isinstance(attr, RpslAttributeMultiValue)
            else attr.value,
        )
        for attr in rpsl
    )


@settings(max_examples=5000)
@given(strategies.rpsl_text_object())
def test_property_based_rpsl_object(rpsl: RpslTextObject):
    """A property based RPSL object is parsed correctly."""
    expected = rpsl_object_to_tuple(rpsl)
    parsed = parse_rpsl_object(rpsl.text)
    note("RPSL:" + "\n" + rpsl.text)
    assert parsed == expected


@given(strategies.whois_server_response())
def test_property_based_whois_server_response(response: RpslWhoisServerResponse):
    """A property based WHOIS server response is parsed correctly."""
    expected = tuple(
        rpsl_object_to_tuple(obj)
        for obj in (_ for _ in response if not isinstance(_, WhoisServerMessage))
    )

    parsed = parse_whois_server_response(response.text)

    note("Response:" + "\n" + response.text)
    assert parsed == expected
