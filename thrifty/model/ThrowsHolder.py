from typing import List

from .IAttributeHolder import IAttributeHolder
from .ThriftyAttribute import ThriftyAttribute


class ThrowsHolder(IAttributeHolder):
    def __init__(self,
                 exceptions: List[ThriftyAttribute]) -> None:
        self.exceptions = exceptions

    @property
    def attributes(self) -> List[ThriftyAttribute]:
        return self.exceptions
