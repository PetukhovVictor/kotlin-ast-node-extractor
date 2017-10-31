import sys

from lib.AstNodeExtractor import AstNodeExtractor
from lib.helper.AstReader import AstReader
from lib.helper.AstWriter import AstWriter

if len(sys.argv) <= 1:
    sys.stderr.write('AST file not specified.\n')
    exit()

if len(sys.argv) <= 2:
    sys.stderr.write('AST extraction nodes file (output) not specified.\n')
    exit()

filename = sys.argv[1]
filename_output = sys.argv[2]

root = AstReader.read(filename)
ast_node_extractor = AstNodeExtractor(root, 'FUN')
extraction_nodes = ast_node_extractor.extract()

AstWriter.write(filename_output, extraction_nodes)
