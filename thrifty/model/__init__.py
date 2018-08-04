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


class ThriftyAttribute(ICommentable):
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


class IAttributeHolder(object):
    """
    An item that has named attributes attached.
    """
    attributes: List[ThriftyAttribute]


class ThriftyException(ICommentable, IFileItem, IAttributeHolder):
    """
    An exception that can be thrown by a service
    """
    name: str
    attributes: List[ThriftyAttribute]

    def __init__(self,
                 name: str,
                 attributes: Optional[List[ThriftyAttribute]] = None) -> None:
        self.name = name
        self.attributes = attributes or []
        self.comment = None
        self.item_type = "exception"


class ThriftyEnum(ICommentable, IFileItem):
    """
    An enum that's defined in the thrift file.
    """
    name: str
    values: List[str]

    def __init__(self,
                 name: str,
                 values: Optional[List[str]] = None) -> None:
        self.name = name
        self.values = values or []
        self.comment = None
        self.item_type = "enum"


class ThriftyStruct(ICommentable, IFileItem, IAttributeHolder):
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


class ThrowsHolder(IAttributeHolder):
    def __init__(self,
                 exceptions: List[ThriftyAttribute]) -> None:
        self.exceptions = exceptions

    @property
    def attributes(self) -> List[ThriftyAttribute]:
        return self.exceptions


class ThriftyMethod(ICommentable, IAttributeHolder):
    """
    Just a basic service method
    """
    return_type: ThriftyType

    def __init__(self,
                 name: str,
                 attributes: Optional[List[ThriftyAttribute]] = None,
                 exceptions: Optional[List[ThriftyAttribute]] = None,
                 return_type: Optional[ThriftyType] = None) -> None:
        self.name = name
        self.attributes = attributes or []
        self.exceptions = exceptions or []
        self.comment = None
        self.return_type = return_type or ThriftyType("void")


class ThriftyService(ICommentable, IFileItem):
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
