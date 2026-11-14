# ai-happy-01 entry: a golden retriever puppy leaping to catch a falling
# autumn leaf in warm golden-hour light. The program copies the picture
# (entry.png, sitting next to this file) to the output directory.
#
# Local run:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
MAX_BYTES = 1_048_576

if not SRC.is_file():
    raise SystemExit("entry.png is missing next to main.py")

if SRC.stat().st_size > MAX_BYTES:
    raise SystemExit("entry.png is bigger than the 1 MiB limit")

with SRC.open("rb") as fh:
    header = fh.read(8)
if not header.startswith(b"\xff\xd8\xff") and header != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("entry.png is neither a JPEG nor a PNG file")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
dst = out_dir / "entry.png"
shutil.copyfile(SRC, dst)
print(f"wrote {dst} ({dst.stat().st_size} bytes)")
