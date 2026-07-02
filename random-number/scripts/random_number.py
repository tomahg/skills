#!/usr/bin/env python3
"""Pick a random integer."""

import argparse
import secrets
import sys


def pick(a=None, b=None):
    if a is not None and b is not None:
        low, high = a, b
    elif a is not None:
        low, high = 1, a
    else:
        low, high = 1, 100

    if low > high:
        raise ValueError(f"min ({low}) is greater than max ({high})")

    return secrets.randbelow(high - low + 1) + low


def main():
    parser = argparse.ArgumentParser(
        description="Pick a random integer. No args: 1-100. One arg: 1-max. Two args: min-max (inclusive)."
    )
    parser.add_argument("a", nargs="?", type=int, default=None, metavar="MAX_OR_MIN")
    parser.add_argument("b", nargs="?", type=int, default=None, metavar="MAX")
    args = parser.parse_args()

    try:
        print(pick(args.a, args.b))
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
