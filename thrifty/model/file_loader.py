from typing import Optional

from thrifty.parser.ThriftListener import ThriftListener
from thrifty.parser.ThriftPaser import ThriftParser
from thrifty.model import ThriftyFile, ThriftyService, IFileItem, ThriftyStruct, ThriftyException
from thrifty.model.comment_parser import comment_text


class FileLoader(ThriftListener):
    """
    Loads a Thrifty model from an AST tree.
    """

    def __init__(self, name: str) -> None:
        self.thrifty_file = ThriftyFile(name)
        self.current_file_item: Optional[IFileItem] = None
        self.current_comment: Optional[str] = None

    def enterService(self, ctx: ThriftParser.ServiceContext):
        self.current_file_item = ThriftyService(ctx.IDENTIFIER())
        self.thrifty_file.file_items.append(self.current_file_item)

    def exitService(self, ctx: ThriftParser.ServiceContext):
        self.current_file_item = None

    def enterStruct(self, ctx: ThriftParser.StructContext):
        self.current_file_item = ThriftyStruct(ctx.IDENTIFIER())
        self.thrifty_file.file_items.append(self.current_file_item)

    def exitStruct(self, ctx: ThriftParser.StructContext):
        self.current_file_item = None

    def enterException(self, ctx: ThriftParser.ExceptionContext):
        self.current_file_item = ThriftyException(ctx.IDENTIFIER())
        self.thrifty_file.file_items.append(self.current_file_item)

    def exitException(self, ctx: ThriftParser.ExceptionContext):
        self.current_file_item = None

    def enterField(self, ctx: ThriftParser.FieldContext):
        pass

    def enterFunction(self, ctx: ThriftParser.FunctionContext):
        pass

    def enterDocument(self, ctx: ThriftParser.DocumentContext):
        pass

    def exitDocument(self, ctx: ThriftParser.DocumentContext):
        pass

    def enterComment_singleline(self, ctx: ThriftParser.Comment_singlelineContext):
        pass

    def enterComment_multiline(self, ctx: ThriftParser.Comment_multilineContext):
        self.current_comment = comment_text(ctx.ML_COMMENT().getText())
