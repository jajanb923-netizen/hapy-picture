# Happy picture — make.fun ai-happy-01

An entry for make.fun's "Make the AI judge happy" bounty. The program
writes one picture, a golden retriever puppy leaping joyfully to catch a
falling autumn leaf in warm golden-hour light, to `/output/entry.png`.

- `main.py` — Python 3.13, standard library only; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).
- `entry.png` — the picture: 1024×1024 JPEG, 194,058 bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
