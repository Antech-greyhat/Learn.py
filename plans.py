#!/usr/bin/env python3
"""
PLAN A to Z: CYBERSECURITY
No matter which plan you try, you end up in cybersecurity.

Run:  python plans.py      (Windows)
      python3 plans.py     (Linux / macOS)
No extra libraries needed.
"""

import os
import random
import string
import sys
import time

# ---------- Terminal setup ----------
os.system("")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

RESET = "\033[0m"
BOLD = "\033[1m"


def color(n):
    """256-color foreground."""
    return f"\033[38;5;{n}m"


RED = color(196)
CYAN = color(51)
MAGENTA = color(201)
GREEN = color(46)

# ---------- Config ----------
LINE_DELAY = 0.15      # delay between normal plan lines
TYPE_DELAY = 0.03      # typing speed for "trying ..." lines
DOT_DELAY = 0.45       # delay between dots
FAIL_PAUSE = 0.6       # pause before "failed"
GLITCH_CHANCE = 0.12   # chance a normal line flickers before showing

# letter: (role, color)
DETOURS = {
    "B": ("web development", color(51)),    # cyan
    "D": ("farming", color(46)),            # green
    "F": ("porn star", color(201)),         # magenta
    "H": ("devops", color(33)),             # blue
    "J": ("forex trading", color(226)),      # yellow
    "L": ("musician", color(208)),          # orange
    "N": ("teacher", color(255)),           # white
    "P": ("crypto trading", color(129)),    # purple
    "R": ("thief", color(213)),             # pink
    "T": ("being a sharp boy", color(220)),         # gold
    "V": ("YouTube career", color(37)),     # teal
    "X": ("freelancing", color(154)),       # lime
}

NOISE = "#@%$&?01<>/\\|"


# ---------- Helpers ----------
def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def type_print(text, col="", delay=TYPE_DELAY):
    """Print text one character at a time."""
    for ch in text:
        write(f"{col}{ch}{RESET}")
        time.sleep(delay)


def glitch(text):
    """Return text with some characters swapped for noise."""
    return "".join(
        random.choice(NOISE) if ch != " " and random.random() < 0.3 else ch
        for ch in text
    )


def cyber_line(letter):
    """Instant CYBERSECURITY line, with an occasional glitch flicker."""
    line = f"PLAN {letter}: CYBERSECURITY"
    if random.random() < GLITCH_CHANCE:
        write(f"{RED}{glitch(line)}{RESET}\r")
        time.sleep(0.06)
    write(f"{RED}{line}{RESET}\n")
    time.sleep(LINE_DELAY)


def fail_line(letter, role, col):
    """'trying <role> ... failed' in the role's own color."""
    type_print(f"PLAN {letter}: trying {role} ", col)
    for _ in range(3):
        write(f"{col}.{RESET}")
        time.sleep(DOT_DELAY)
    time.sleep(FAIL_PAUSE)
    write(f" {BOLD}{RED}failed{RESET}\n")
    time.sleep(0.4)


# ---------- Final banner ----------
FONT = {
    "C": [" ████", "█    ", "█    ", "█    ", " ████"],
    "Y": ["█   █", " █ █ ", "  █  ", "  █  ", "  █  "],
    "B": ["████ ", "█   █", "████ ", "█   █", "████ "],
    "E": ["█████", "█    ", "████ ", "█    ", "█████"],
    "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
    "S": [" ████", "█    ", " ███ ", "    █", "████ "],
    "U": ["█   █", "█   █", "█   █", "█   █", " ███ "],
    "I": ["█████", "  █  ", "  █  ", "  █  ", "█████"],
    "T": ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
}


def render_word(word):
    """Turn a word into 5 rows of block letters."""
    rows = []
    for r in range(5):
        rows.append(" ".join(FONT[ch][r] for ch in word))
    return rows


def show_banner():
    rows = render_word("CYBER") + [""] + render_word("SECURITY")
    inner = max(len(r) for r in rows) + 6
    # neon green -> cyan -> blue gradient, one color per row
    gradient = [46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21]

    write("\n")
    write(f"{color(46)}╔{'═' * inner}╗{RESET}\n")
    for i, row in enumerate(rows):
        col = color(gradient[min(i, len(gradient) - 1)])
        write(f"{color(46)}║{RESET}{col}{BOLD}{row.center(inner)}{RESET}{color(46)}║{RESET}\n")
        time.sleep(0.12)
    write(f"{color(46)}╚{'═' * inner}╝{RESET}\n\n")


def blinking_cursor(times=6):
    for _ in range(times):
        write(f"{GREEN}█{RESET}")
        time.sleep(0.45)
        write("\b \b")
        time.sleep(0.35)
    write(f"{GREEN}█{RESET}\n")


def final_message():
    time.sleep(1.0)
    show_banner()

    messages = [
        "Every plan led here for a reason.",
        "The world needs people who protect it.",
        "Keep learning, keep building, keep breaking (legally).",
    ]
    for msg in messages:
        type_print(msg, CYAN, 0.035)
        write("\n")
        time.sleep(0.4)

    write("\n")
    time.sleep(0.5)
    type_print('"123 is still the king."', f"{BOLD}{MAGENTA}", 0.06)
    write("\n\n")
    time.sleep(0.5)
    blinking_cursor()


# ---------- Main ----------
def main():
    for letter in string.ascii_uppercase:
        if letter in DETOURS:
            role, col = DETOURS[letter]
            fail_line(letter, role, col)
        cyber_line(letter)
    final_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        write(f"{RESET}\n")