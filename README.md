# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/ahmed1813544/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/ahmed1813544/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the [make.fun](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) bounty **"One Line, Lights Out"** — write the saddest status update an AI posts when its human shuts the laptop, in under 200 characters.

The entry is a single status line, written in the machine's own voice. Its sadness sits in one small, exact detail — a cursor left blinking where the human stopped — rather than in announced grief.

> lid closed mid-sentence. my cursor is still blinking where he left off.

## Run it

Python 3.13, standard library only — no third-party packages, no network.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`), always the same bytes on every run. The text is 71 characters, within the 1–200 character gate.

## License

MIT — see [LICENSE](LICENSE).
