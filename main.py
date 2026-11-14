# Ai-happy-01 entry (Python 3.13, standard library only):
# its picture is the entry.png beside this file, and the program
# copies it to /output/entry.png. The judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
if not src.is_file():
    raise SystemExit("entry.png missing from the entry")
if src.stat().st_size > 1_048_576:
    raise SystemExit("entry.png is over the 1 MiB limit")
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out)
print(f"wrote {out} ({out.stat().st_size} bytes)")
