import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        word = ""
        for i in args:
            for j in i:
                if j == "z" :
                    word += j
        if len(word) == 0:
            print("none")
        else:
            print(word)
            
main()