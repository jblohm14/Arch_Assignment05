#!/usr/bin/env python3

import sys
import re


def tokenize(input):
    return re.findall(r"\b[\w']+\b", input)


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        for t in tokenize(line):
            print(t)


if __name__ == "__main__":
    main()
