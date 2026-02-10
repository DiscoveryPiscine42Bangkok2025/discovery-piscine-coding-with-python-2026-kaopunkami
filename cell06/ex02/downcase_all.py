import sys


def downcase_it(s: str) -> str:
    return s.lower()


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    for a in args:
        print(downcase_it(a))


if __name__ == "__main__":
    main()