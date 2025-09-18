import sys,re

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    for i in args:
        if i.endswith("ism"):
            continue
        else:
            print(f"{i}ism")
main()