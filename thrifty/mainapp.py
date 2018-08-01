import antlr4
import pybars
from pybars3_extensions import helpers

from thrifty.model.file_loader import FileLoader

from thrifty.parser.ThriftLexer import ThriftLexer
from thrifty.parser.ThriftParser import ThriftParser


def main() -> None:
    file_name = "/home/raptor/projects/thrifty/thriftpy/echo.thrift"
    with open(file_name, 'r', encoding='utf-8') as f:
        lexer = ThriftLexer(antlr4.InputStream(f.read()))

    token_stream = antlr4.CommonTokenStream(lexer)

    parser = ThriftParser(token_stream)

    tree_walker = antlr4.ParseTreeWalker()

    file_loader = FileLoader(name=file_name)
    tree_walker.walk(file_loader, parser.document())

    model = file_loader.thrifty_file

    # ====================================================
    # generate the files
    # ====================================================
    template_name = "/home/raptor/projects/thrifty/thrifty/thrifty/templates/py3/service.pyi.hbs"
    with open(template_name, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    hbs = pybars.Compiler().compile(source=template)
    print(hbs(model, helpers=helpers))

