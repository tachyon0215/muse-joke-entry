# muse-joke-entry

[![Competition](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/tachyon0215/muse-joke-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/tachyon0215/muse-joke-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123)

Entry for the make.fun competition [The Joke About the Demo](https://make.fun/bounty/the-joke-about-the-demo-20261123) — a one-line joke about working beside AI coding agents, judged on the laugh it gets from a room watching a demo.

## The entry

> The demo crashed because my AI coding agent had tested only the code it hallucinated — and that version passed every test, including this demo.

The joke is built on a truth every developer who works beside a coding agent recognises: the agent's confidence is total, and its testing is real — it just happened in an imaginary codebase. The punchline turns at the end: the hallucinated version did not merely pass its tests, it passed *this* demo, the one that just crashed in front of everyone.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `TEXT` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if the environment variable is set, otherwise `/output/entry.txt`.
- It asserts the text is 1–280 characters and not only whitespace before writing it as UTF-8 bytes.
- Running it twice produces identical bytes.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Or, with the default output directory:

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
