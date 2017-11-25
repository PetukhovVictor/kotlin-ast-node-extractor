# kotlin-ast-node-extractor

Program for extraction of the specified node type from Kotlin AST.

Program extract subtree of AST, which are nodes of the specified type.

Examplpe of use:
```
python3 main.py -t FUN -i ~/Desktop/least_recently_indexed_14_41_29_10_2017 -o results --subtree-per-file
```

Program arguments:
* **-t**, **--target**: target node type (e.g. FUN, REFERENCE_EXPRESSION, IMPORT_DIRECTIVE, etc);
* **-i**, **--input**: input folder with ASTs (using recoursive);
* **-o**, **--output**: output folder (will be placed here ASTs subtree, which are nodes of the specified type);
* **--subtree_per_file**: write subtree per file (if specified --subtree-per-file flag, then extracted subtree written in many files: one subtree = one file)
