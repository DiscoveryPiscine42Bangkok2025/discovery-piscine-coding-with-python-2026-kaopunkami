#!/usr/bin/env python3
import sys


def shrink(s: str) -> None:
    print(s[:8])


def enlarge(s: str) -> None:
    print(s + ("Z" * (8 - len(s))))


def main() -> None:
    args = sys.argv[1:]
    if len(args) < 1:
        print("none")
        return

    for a in args:
        if len(a) > 8:
            shrink(a)
        elif len(a) < 8:
            enlarge(a)
        else:
            print(a)


if __name__ == "__main__":
    main()
