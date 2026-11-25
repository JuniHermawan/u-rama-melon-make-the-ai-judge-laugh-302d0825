"""Make the AI Judge Laugh — one-line office joke.

The program prints exactly one joke about office life: a single line,
under 200 characters, written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Joke: a boss lets AI write a performance review, the AI hands out a
raise, and HR dismisses the raise as a hallucination. The setup is a
true 2026 office scene (AI-written reviews, HR as gatekeeper); the turn
is the last word — the raise itself is the hallucination.

Revision: added _check_gate(), which enforces the competition gate
(UTF-8, 1-200 characters, one line, not only whitespace) before writing,
so a bad joke fails loudly here instead of silently at grading time.
"""

import os

JOKE = "My boss let the AI write my review; it gave me a raise, and HR called it a hallucination."


def _check_gate(text):
    """Enforce the competition gate: 1-200 chars, one line, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    _check_gate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
