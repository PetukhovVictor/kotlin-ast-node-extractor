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

subtree_per_file = len(sys.argv) == 5 and sys.argv[4] == '--subtree-per-file'

target = sys.argv[1]
folder_input = sys.argv[2]
folder_output = sys.argv[3]


def ast_file_process(filename):
    root = AstReader.read(filename)
    ast_node_extractor = AstNodeExtractor(root, target)
    extraction_nodes = ast_node_extractor.extract()

    def ast_write(filename, extraction_nodes):
        relative_filename = os.path.relpath(filename, folder_input)
        AstWriter.write(folder_output, relative_filename, extraction_nodes)
        TimeLogger.console_output(None, prefix='Processing ' + relative_filename + '...')

    if subtree_per_file:
        ast_node_counter = 1
        for extraction_node in extraction_nodes:
            basename = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            new_filename = basename + '.' + str(ast_node_counter) + extension
            ast_write(new_filename, [extraction_node])
            ast_node_counter += 1
    else:
        ast_write(filename, extraction_nodes)


extraction_time = FilesWalker.walk(folder_input, ast_file_process)
TimeLogger.console_output(extraction_time, prefix='Extraction time nodes of \'' + target + '\' type: ')
