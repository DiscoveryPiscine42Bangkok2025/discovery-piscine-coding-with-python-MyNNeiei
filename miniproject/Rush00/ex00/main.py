from checkmate import checkmate

def main():
    checkmate(123)
    checkmate("")

    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)

    board2 = """\
..
.K"""
    checkmate(board2)

    board3 = """\
K...
..
...."""
    checkmate(board3)

    board4 = """\
K..
..."""
    checkmate(board4)

    board5 = """\
....
....
....
...."""
    checkmate(board5)

    board6 = """\
K...
....
....
...K"""
    checkmate(board6)

    board7 = """\
....
RK..
....
...."""
    checkmate(board7)

    board8 = """\
.R..
....
....
.K.."""
    checkmate(board8)

    board9 = """\
B...
....
....
...K"""
    checkmate(board9)

    board10 = """\
....
QK..
....
...."""
    checkmate(board10)

    board11 = """\
Q...
....
....
...K"""
    checkmate(board11)

    board12 = """\
....
....
....
...K"""

    board13 = """\
R.P.
....
....
...K"""
    checkmate(board13)

if __name__ == "__main__":
    main()