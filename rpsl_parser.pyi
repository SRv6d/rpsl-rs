from typing import Tuple, Union

Name = str
Value = Tuple[Union[str, None], ...]

RpslAttribute = Tuple[Name, Value]
RpslObject = Tuple[RpslAttribute, ...]

def parse_rpsl_object(rpsl: str) -> RpslObject:
    """Parse a string containing an RPSL object.

    Example:
        ```python
        >>> rpsl = '''
        aut-num:        AS13030
        as-name:        INIT7
        '''
        >>> rpsl_object = parse_rpsl_object(rpsl)
        >>> print(rpsl_object)
        (('aut-num', ('AS13030',)), ('as-name', ('INIT7',)))
        ```

    Args:
        rpsl: The string containing the RPSL object to parse.

    Returns:
        The attributes contained in the RPSL object.

    Raises:
        RPSLParseError: The RPSL could not be parsed.
    """

def parse_whois_server_response(response: str) -> Tuple[RpslObject, ...]:
    """Parse a string containing a whois server response.

    Example:
        ```python
        >>> response = '''
        ASNumber:       32934
        ASName:         FACEBOOK

        OrgName:        Facebook, Inc.
        OrgId:          THEFA-3
        '''
        >>> rpsl_objects = parse_whois_server_response(response)
        >>> print(rpsl_objects)
        ((('ASNumber', ('32934',)), ('ASName', ('FACEBOOK',))),
         (('OrgName', ('Facebook, Inc.',)), ('OrgId', ('THEFA-3',))))
        ```

    Args:
        rpsl: The string containing the whois server response to parse.

    Returns:
        The objects contained in the response.

    Raises:
        RPSLParseError: The RPSL contained in the response could not be parsed.
    """
