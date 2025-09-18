import sys
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        print("parameters :", len(args))
        for i in args:
            print(f"{i} :" , len(i))
main()