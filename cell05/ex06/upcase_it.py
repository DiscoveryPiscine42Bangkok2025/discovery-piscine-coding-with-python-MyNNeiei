import sys
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        args_upcase = [x.upper() for x in args]
        print(" ".join(args_upcase))
main()