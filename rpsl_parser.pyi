from typing import Tuple, Union

Name = str
Value = Tuple[Union[str, None], ...]

RpslAttribute = Tuple[Name, Value]
RpslObject = Tuple[RpslAttribute, ...]

def parse_rpsl_object(rpsl: str) -> RpslObject: ...
def parse_whois_server_response(response: str) -> Tuple[RpslObject, ...]: ...
