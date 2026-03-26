#!/usr/bin/env python3


import sys
from collections import Counter


def main():
    if len(sys.argv) < 2:
        print("Usage:   ./word_frequency_filter.py <min frequency>", file=sys.stderr)
        print("Example: ./word_frequency_filter.py 2", file=sys.stderr)
        sys.exit(1)

    try:
        min = int(sys.argv[1])
        if min < 1:
            raise ValueError
    except ValueError:
        print("Error: min_frequency must be a positive integer.", file=sys.stderr)
        sys.exit(1)

    c = Counter()

    for line in sys.stdin:
        word = line.strip()
        if word:
            c[word] += 1

    for word, count in sorted(c.items()):
        if count >= min:
            print(word)


if __name__ == "__main__":
    main()
