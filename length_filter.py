#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 3:
        print("Usage:   ./length_filter.py <min_length> <max_length>", file=sys.stderr)
        print("Example: ./length_filter.py 4 6", file=sys.stderr)
        sys.exit(1)

    try:
        min = int(sys.argv[1])
        max = int(sys.argv[2])

        if min < 0 or max < 0:
            raise ValueError("Lengths must be non-negative")
        if min > max:
            raise ValueError("min_length cannot be greater than max_length")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    for line in sys.stdin:
        word = line.strip()
        if word:
            length = len(word)
            if min <= length <= max:
                print(word)


if __name__ == "__main__":
    main()
