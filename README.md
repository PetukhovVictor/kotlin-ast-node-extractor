# kotlin-ast-node-extractor

Program for extraction of the specified node type from Kotlin AST.

Program extract subtree of AST, which are nodes of the specified type.

Example of use:
```
python main.py -t FUN -i ./ast -o ./ast_extracted --subtree_per_file
```

Program arguments:
* target node type (e.g. FUN, REFERENCE_EXPRESSION, IMPORT_DIRECTIVE, etc);
* input folder with ASTs (using recursive);
* output folder (will be placed here ASTs subtree, which are nodes of the specified type);
* write subtree per file (if specified --subtree-per-file flag, then extracted subtree written in many files: one subtree = one file)
