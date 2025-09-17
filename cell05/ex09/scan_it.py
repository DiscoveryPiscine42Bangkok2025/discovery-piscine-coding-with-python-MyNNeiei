import sys
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        for i in range(len(args)-1, -1, -1):
            if args[i].islower():
                args[i] = args[i].upper()
main()

