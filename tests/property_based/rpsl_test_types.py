"""Types representing RPSL components for testing purposes."""

from typing import NamedTuple


class RpslAttributeSingleValue(NamedTuple):
    """A RPSL attribute that has a single value.

    Represents a RPSL attribute containing a single value for testing purposes.

    Attributes:
        text: The RPSL text representation of the attribute.
        name: The name of the attribute.
        value: The value of the attribute.

    Example:
        ```
        aut-num:        AS51531
        ^^^^^^^ - name  ^^^^^^^ - value
        ^^^^^^^^^^^^^^^^^^^^^^^ - text
    """

    text: str
    name: str
    value: str


class RpslAttributeMultiValue(NamedTuple):
    """A RPSL attribute that has multiple values.

    Represents a RPSL attribute containing multiple values for testing purposes.

    Attributes:
        text: The RPSL text representation of the attribute.
        name: The name of the attribute.
        value: The value of the attribute.

    Example:
        ```
        remarks:        The first value
                        ^^^^^^^^^^^^^^^ - value[0]
                        The second value
                        ^^^^^^^^^^^^^^^^ - value[1]
        ```
    """

    text: str
    name: str
    value: tuple[str | None, ...]


class RpslAttributeNoneValue(NamedTuple):
    """A RPSL attribute that has no value.

    Represents a RPSL attribute containing no value for testing purposes.

    Attributes:
        text: The RPSL text representation of the attribute.
        name: The name of the attribute.
        value: The value of the attribute.

    Example:
        ```
        remarks:                  # intentional trailing whitespace
                        ^^^^^^^^^^ - whitespace where we would expect a value
        ```
    """

    text: str
    name: str
    value: None


class RpslTextObject(
    tuple[
        RpslAttributeSingleValue | RpslAttributeMultiValue | RpslAttributeNoneValue,
        ...,
    ]
):
    """A RPSL text object.

    Represents a RPSL text object for testing purposes.
    RPSL text consists of one or more (multiline) attributes.

    Example:
        ```
        aut-num:        AS51531                               <- [0]
        remarks:                                              <- [1]
        remarks:        For peering information please check: <- [2]
                        https://as51531.peeringdb.com         <- [2]
        mnt-by:         DECIX-MNT                             <- [3]
        ```
    """

    @property
    def text(self) -> str:
        """The RPSL text representation of the object."""
        repr_ = "\n".join(attribute.text for attribute in self)
        repr_ += "\n" * 2  # Objects end with a blank line

        return repr_


class WhoisServerMessage(NamedTuple):
    """A whois server message.

    Example:
        ```
        % Information related to 'AS51531'
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - value
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - text
        ```
    """

    text: str
    value: str


class RpslWhoisServerResponse(tuple[RpslTextObject | WhoisServerMessage, ...]):
    """A whois server response.

    Represents a text response from a whois server possibly containing
    multiple RPSL objects as well as server messages.


    Example:
        ```
        % Information related to 'AS51531'               <- server message

        % Abuse contact for 'AS51531' is 'abuse@cix.net' <- server message

        aut-num:        AS51531                          <- start of first RPSL object
        remarks:
        remarks:        For peering information please check:
                        https://as51531.peeringdb.com
        mnt-by:         DECIX-MNT
        descr:          DE-CIX Management GmbH
        descr:          DE
        admin-c:        ENG6695-RIPE
        tech-c:         ENG6695-RIPE
        status:         ASSIGNED
        org:            ORG-DtGI1-RIPE
        mnt-by:         RIPE-NCC-END-MNT
        created:        2010-09-21T11:26:20Z
        last-modified:  2019-12-04T11:19:36Z
        source:         RIPE
        ```
    """

    @property
    def text(self) -> str:
        """The text representation of the server response."""
        repr_ = "\n".join(_.text for _ in self)
        repr_ += "\n"

        return repr_
