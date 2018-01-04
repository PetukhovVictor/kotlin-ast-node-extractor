import os
import argparse

from lib.AstNodeExtractor import AstNodeExtractor
from lib.helper.AstReader import AstReader
from lib.helper.AstWriter import AstWriter
from lib.helper.FilesWalker import FilesWalker

parser = argparse.ArgumentParser()

parser.add_argument('--target', '-t', nargs=1, type=str, help='target type of AST node')
parser.add_argument('--input', '-i', nargs=1, type=str, help='ASTs input folder')
parser.add_argument('--output', '-o', nargs=1, type=str, help='ASTs snippets output folder')
parser.add_argument('--subtree_per_file', action='store_true')
args = parser.parse_args()

target = args.target[0]
folder_input = args.input[0]
folder_output = args.output[0]
subtree_per_file = args.subtree_per_file


def ast_file_process(filename):
    root = AstReader.read(filename)
    ast_node_extractor = AstNodeExtractor(root, target)
    extraction_nodes = ast_node_extractor.extract()

    def ast_write(filename, extraction_nodes):
        relative_filename = os.path.relpath(filename, folder_input)
        AstWriter.write(folder_output, relative_filename, extraction_nodes)
        print('Processing ' + relative_filename + '...')

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


FilesWalker.walk(folder_input, ast_file_process, log_text='Extraction time nodes of ' + target)
