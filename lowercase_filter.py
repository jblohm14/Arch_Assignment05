#!/usr/bin/env python3

import sys


def main():
    for line in sys.stdin:
        word = line.strip()
        if word:
            print(word.lower())


if __name__ == "__main__":
    main()
