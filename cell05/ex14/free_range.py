import sys

def main():
    args = sys.argv[1:]
    list_range = []
    if len(args) == 0:
        print("none")
    else:
        if args[0] < args[1]:
            for i in range(int(args[0]), int(args[1])+1):
                list_range.append(i)
            print(list_range)
        else:
            for i in range(int(args[1]), int(args[0])+1):
                list_range.append(i)
            print(list_range)
main()