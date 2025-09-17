import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        print(" \n".join(args).swapcase())
main()