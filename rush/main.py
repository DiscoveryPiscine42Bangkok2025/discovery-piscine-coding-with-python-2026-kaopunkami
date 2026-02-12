from checkmate import checkmate

def main() -> None:
    boards = [
        # Board 1
        """\
R...
.K..
..P.
....\
""",
        # Board 2
        """\
....
.K..
...P
....\
""",
        # Board 3
        """\
.R..
....
.K..
....\
""",
        # Board 4
        """\
Q...
....
..K.
....\
""",

        # Board 5
        """\
..P.
....
..K.
R...\
""",
    ]

    for board in boards:
        checkmate(board)

if __name__ == "__main__":
    main()

