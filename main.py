import sys
import os

from lib.AstNodeExtractor import AstNodeExtractor
from lib.helper.AstReader import AstReader
from lib.helper.AstWriter import AstWriter
from lib.helper.FilesWalker import FilesWalker
from lib.helper.TimeLogger import TimeLogger

if len(sys.argv) <= 1:
    sys.stderr.write('Target (type of AST node) not specified.\n')
    exit()

if len(sys.argv) <= 2:
    sys.stderr.write('ASTs folder not specified.\n')
    exit()

if len(sys.argv) <= 3:
    sys.stderr.write('AST extraction nodes folder (output) not specified.\n')
    exit()

target = sys.argv[1]
folder_input = sys.argv[2]
folder_output = sys.argv[3]

def ast_file_process(filename):
    root = AstReader.read(filename)
    ast_node_extractor = AstNodeExtractor(root, target)
    extraction_nodes = ast_node_extractor.extract()

    relative_filename = os.path.relpath(filename, folder_input)
    AstWriter.write(folder_output, relative_filename, extraction_nodes)

    TimeLogger.console_output(None, prefix='Processing ' + relative_filename + '...')


extraction_time = FilesWalker.walk(folder_input, ast_file_process)
TimeLogger.console_output(extraction_time, prefix='Extraction time nodes of \'' + target + '\' type: ')
