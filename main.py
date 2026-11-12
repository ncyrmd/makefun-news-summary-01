# A working news-summary-01 entry (Python 3.13, standard library only): its summary
# is the summary.txt beside this file, and the program copies it to the output
# file. The gate takes UTF-8 text of 1 to 2,000 characters that is not only
# white space, and the judge reads exactly the bytes copied, so the program
# writes the file byte for byte, with no added line end.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

source = Path(__file__).with_name("summary.txt")
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
target = output_dir / "entry.txt"
shutil.copyfile(source, target)

# Self-check the gate's rules (1 to 2,000 characters, not only white space);
# fail loudly instead of submitting an invalid entry.
text = target.read_text(encoding="utf-8")
if not 1 <= len(text) <= 2000 or not any(not c.isspace() for c in text):
    raise SystemExit(f"entry.txt is {len(text)} characters; the gate needs 1 to 2,000")
