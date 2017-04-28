#!/bin/bash
python compression_text.py fichier_input.txt comp.txt
python decompression_text.py comp.txt output.txt
diff --side-by-side --suppress-common-lines --strip-trailing-cr fichier_input.txt output.txt | wc -l
