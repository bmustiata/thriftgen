from typing import List, Optional


class IFileItem(object):
    """
    An item that appears in a thrift file, be it a service,
    struct or exception.
    """
    item_type: str


class ICommentable(object):
    """
    An item that might have a comment attached to it.
    """
    comment: Optional[str]


class ThriftyType(object):
    """
    A type that can be used in a method parameter, struct, or exception
    member definition.
    """
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class ThriftyAttribute(object, meta=[ICommentable]):
    """
    An attribute that can belong to a method, a struct, or
    an exception.
    """
    name: str
    attrtype: ThriftyType

    def __init__(self,
                 name: str,
                 attrtype: ThriftyType) -> None:
        self.name = name
        self.attrtype = attrtype
        self.comment = None


class ThriftyException(object, meta=[ICommentable, IFileItem]):
    """
    An exception that can be thrown by a service
    """
    name: str
    attributes: List[ThriftyAttribute]

    def __init__(self,
                 name: str,
                 attributes: Optional[List[ThriftyAttribute]]) -> None:
        self.name = name
        self.attributes = attributes or list()
        self.comment = None
        self.item_type = "exception"


class ThriftyStruct(object, meta=[ICommentable, IFileItem]):
    """
    A struct that can be transported as a type for methods
    or exceptions.
    """
    attributes: List[ThriftyAttribute]

    def __init__(self,
                 name: str,
                 attributes: Optional[List[ThriftyAttribute]] = None) -> None:
        self.name = name
        self.attributes = attributes or []
        self.comment = None
        self.item_type = "struct"


class ThriftyMethod(object, meta=[ICommentable]):
    """
    Just a basic service method
    """

    def __init__(self,
                 parameters: Optional[List[ThriftyAttribute]] = None,
                 exceptions: Optional[List[ThriftyException]] = None) -> None:
        self.parameters = parameters or []
        self.exceptions = exceptions or []
        self.comment = None


class ThriftyService(object, meta=[ICommentable, IFileItem]):
    """
    ThriftyService is a service that exports one or more methods.
    """
    name: str
    methods: Optional[List[ThriftyMethod]]

    def __init__(self,
                 name: str,
                 methods: Optional[List[ThriftyMethod]] = None) -> None:
        self.name = name
        self.methods = methods or []
        self.comment = None
        self.item_type = "service"


class ThriftyFile(object):
    """
    A file that contains multiple services, structures and exceptions.
    """
    file_name: str
    file_items: List[IFileItem]

    def __init__(self,
                 file_name: str) -> None:
        self.file_name = file_name
        self.file_items = []
