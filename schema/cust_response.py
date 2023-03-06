from pydantic.generics import GenericModel
from typing import Generic,Optional,TypeVar

T = TypeVar('T')

class Response(GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

    