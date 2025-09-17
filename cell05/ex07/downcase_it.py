import sys
def main():
    agrs = sys.argv[1:]
    if len(agrs) == 0:
        print("none")
    else:
        print(" ".join(agrs).lower())
main()