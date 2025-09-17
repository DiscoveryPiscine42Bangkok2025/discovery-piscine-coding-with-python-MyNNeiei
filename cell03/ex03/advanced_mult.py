import sys

def main():
    args = sys.argv[1:]
    if len(args) != 0:
        print("none")
    else:
        number = 0
        while number < 11:
            print(f"Table de {number}: {number * 0} {number * 1} {number * 2} {number * 3} {number * 4} {number * 5} {number * 6} {number * 7} {number * 8} {number * 9} {number * 10}")
            number += 1   
main()