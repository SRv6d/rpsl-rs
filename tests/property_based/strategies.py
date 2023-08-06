"""Hypothesis composite strategies for RPSL components."""

from functools import partial

from hypothesis import assume, example, strategies

from property_based.rpsl_test_types import (
    TestRpslAttributeMultiValue,
    TestRpslAttributeNoneValue,
    TestRpslAttributeSingleValue,
    TestRpslTextObject,
    TestWhoisServerMessage,
)

ascii_characters = partial(strategies.characters, min_codepoint=0, max_codepoint=127)

@strategies.composite
def _rpsl_attribute_name(draw: strategies.DrawFn) -> str:
    """RPSL attribute name strategy.

    According to RFC 2622, an "<object-name>" is made up of
    letters, digits, the character underscore "_", and the character
    hyphen "-"; the first character of a name must be a letter, and
    the last character of a name must be a letter or a digit.

    Creates a string of ASCII characters including 
    letters, digits, underscore and hyphen.
    """
    return draw(
        strategies.text(
            alphabet=ascii_characters(
                whitelist_categories=["Ll", "Lu", "Nd"], # letters and digits
                whitelist_characters=["_", "-"]
            ),
            min_size=1,
        )
    )


@strategies.composite
def _rpsl_attribute_value(draw: strategies.DrawFn) -> str:
    """RPSL attribute value strategy.

    Creates a string of ASCII characters excluding control characters that
    must not start with, or consist only of whitespace.
    """
    value = draw(
        strategies.text(
            alphabet=ascii_characters(
                blacklist_categories=["Cc"]
            ),
            min_size=1,
        )
    )
    assume(not value.isspace() and not value.startswith(" "))

    return value


@strategies.composite
def _rpsl_attribute_empty_value(draw: strategies.DrawFn) -> str:
    """RPSL empty attribute value strategy.

    Creates a string consisting of zero or more spaces.
    """
    return draw(
        strategies.text(
            alphabet=strategies.characters(
                whitelist_categories=(), whitelist_characters=[" "]
            )
        )
    )


@strategies.composite
def _rpsl_attribute_space_separator(draw: strategies.DrawFn) -> str:
    """RPSL space separator strategy.

    Creates a string consisting of 0-80 spaces.
    """
    return " " * draw(strategies.integers(min_value=0, max_value=80))


@strategies.composite
@example(TestRpslAttributeSingleValue("role:   ACME CORP", "role", "ACME CORP"))
@example(
    TestRpslAttributeSingleValue(
        "descr:    Unaligned description", "descr", "Unaligned description"
    )
)
def rpsl_single_value_attribute(
    draw: strategies.DrawFn,
) -> TestRpslAttributeSingleValue:
    """Single value RPSL attribute strategy.

    Creates a single property based RPSL attribute, consisting of a name and a value
    separated by a colon with 0-80 whitespaces. The value cannot be empty
    or consist only of spaces.

    Examples:
        ```python
        ('role:   ACME CORP', 'role', 'ACME CORP')
        ('descr:    Unaligned description', 'descr', 'Unaligned description')
        ('0: 0', '0', '0')
        ('rur0F:                                       psp0F', 'rur0F', 'psp0F')
        ```
    """
    name = draw(_rpsl_attribute_name())
    value = draw(_rpsl_attribute_value())
    spacing = draw(_rpsl_attribute_space_separator())

    line = f"{name}:{spacing}{value}"
    return TestRpslAttributeSingleValue(line, name, value)


@strategies.composite
def rpsl_none_value_attribute(draw: strategies.DrawFn) -> TestRpslAttributeNoneValue:
    """None value RPSL attribute strategy.

    Creates a single property based RPSL attribute, where the value
    corresponds to a None value like an empty string or a string consisting
    of only spaces.

    Examples:
        ```python
        ('remarks:   ', 'remarks', None)
        ('remarks:', 'remarks', None)
        ```
    """
    name = draw(_rpsl_attribute_name())
    value = draw(_rpsl_attribute_empty_value())
    spacing = draw(_rpsl_attribute_space_separator())

    line = f"{name}:{spacing}{value}"
    return TestRpslAttributeNoneValue(line, name, None)


MULTILINE_CONTINUATION_PREFIX = (
    "                ",
    "+               ",
    "\t            ",
)


@strategies.composite
@example(
    TestRpslAttributeMultiValue(
        "address: Packet Street 6\n 128 Series of Tubes",
        "address",
        ("Packet Street 6", "128 Series of Tubes"),
    )
)
@example(
    TestRpslAttributeMultiValue(
        "address: Packet Street 6\n+ 128 Series of Tubes",
        "address",
        ("Packet Street 6", "128 Series of Tubes"),
    )
)
def rpsl_multi_value_attribute(draw: strategies.DrawFn) -> TestRpslAttributeMultiValue:
    """Multiple attribute RPSL line strategy.

    Creates a single property based RPSL attribute, consisting of a name and multiple
    values that may be None like.
    Each continuation line must be prefixed with a continuation character.
    Empty values are represented by a line consisting of only a "+" character.

    Examples:
        ```python
        (
            "address: Packet Street 6\n 128 Series of Tubes",
            "address",
            ("Packet Street 6", "128 Series of Tubes"),
        )
        (
            "address: Packet Street 6\n+ 128 Series of Tubes",
            "address",
            ("Packet Street 6", "128 Series of Tubes"),
        )
        ```
    """
    name = draw(_rpsl_attribute_name())
    values = draw(
        strategies.lists(
            _rpsl_attribute_value() | _rpsl_attribute_empty_value(), min_size=1
        )
    )

    text = f"{name}:{draw(_rpsl_attribute_space_separator())}{values[0]}"
    for value in values[1:]:
        text += "\n"

        if not value or value.isspace():
            text += "+"  # Blank lines are valid if prefixed with "+"
        else:
            prefix = draw(strategies.sampled_from(MULTILINE_CONTINUATION_PREFIX))
            spacing = draw(_rpsl_attribute_space_separator())
            text += prefix + spacing + value

    return TestRpslAttributeMultiValue(
        text,
        name,
        tuple((value if value and not value.isspace() else None) for value in values),
    )


@strategies.composite
def rpsl_text_object(draw: strategies.DrawFn) -> TestRpslTextObject:
    """RPSL text strategy.

    Creates RPSL text object that should represent any possible combination of
    RPSL attributes. The attributes may be single, multi or None like values, while at
    least one single or multi value attribute is required.
    """
    lines = draw(
        strategies.lists(
            rpsl_single_value_attribute()
            | rpsl_none_value_attribute()
            | rpsl_multi_value_attribute(),
            min_size=1,
        )
    )

    return TestRpslTextObject(lines)


@strategies.composite
@example(
    TestWhoisServerMessage(
        "% This query was served by the RIPE Database Query Service version 1.106.1",
        "This query was served by the RIPE Database Query Service version 1.106.1",
    )
)
def whois_server_message(draw: strategies.DrawFn) -> TestWhoisServerMessage:
    """Whois server message strategy.

    Creates a whois server message that consists of at least one non-control character.
    """
    indicator = "%"
    whitespace = draw(_rpsl_attribute_space_separator())
    value = draw(
        strategies.text(
            alphabet=strategies.characters(blacklist_categories=["Cc"]),
            min_size=1,
        )
    )
    return TestWhoisServerMessage(indicator + whitespace + value, value)
