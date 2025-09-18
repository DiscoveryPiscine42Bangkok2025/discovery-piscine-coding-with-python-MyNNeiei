from checkmate import checkmate

def main():
    checkmate(123) # Error
    checkmate("") # Error

    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) # Success

    board2 = """\
..
.K"""
    checkmate(board2) # Fail

    board3 = """\
K...
..
...."""
    checkmate(board3) # Error

    board4 = """\
K..
..."""
    checkmate(board4)# Error

    board5 = """\
....
....
....
...."""
    checkmate(board5) # Error

    board6 = """\
K...
....
....
...K"""
    checkmate(board6) # Error

    board7 = """\
....
RK..
....
...."""
    checkmate(board7) # Success

    board8 = """\
.R..
....
....
.K.."""
    checkmate(board8) # Success

    board9 = """\
B...
....
....
...K"""
    checkmate(board9) # Success

    board10 = """\
....
QK..
....
...."""
    checkmate(board10) # Success

    board11 = """\
Q...
....
....
...K"""
    checkmate(board11) # Success

    board12 = """\
....
....
....
...K"""
    checkmate(board12) # Fail

    board13 = """\
R.P.
....
....
...K"""
    checkmate(board13) # Fail

if __name__ == "__main__":
    main()