import sys
def main():
    args = sys.argv[1:]
    word = input("What was the parameter? ")
    if len(args) != 1:
        print("none")
    elif args[0] == word:
        print("Good job!")
    elif args[0] != word:
        print("Nope, sorry...")
main()