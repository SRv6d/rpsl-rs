from typing import TypeAlias

import pytest
from hypothesis import given
from rpsl_parser import parse_rpsl_object

from property_based import strategies
from property_based.rpsl_test_types import (
    RpslTextObject,
    RpslAttributeMultiValue,
)

_RpslAttributes: TypeAlias = list[str]


@given(strategies.rpsl_text_object())
def test_property_based_rpsl_object(rpsl: RpslTextObject):
    """A property based RPSL object is parsed correctly."""
    expected = tuple(
        (
            attr.name,
            (attr.value,)
            if not isinstance(attr, RpslAttributeMultiValue)
            else attr.value,
        )
        for attr in rpsl
    )

    parsed = parse_rpsl_object(rpsl.text)

    assert parsed == expected
