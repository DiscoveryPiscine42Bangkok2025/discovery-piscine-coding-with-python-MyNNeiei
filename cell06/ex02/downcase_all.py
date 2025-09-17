import sys
def downcase_all():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        args_downcase = [x.lower() for x in args]
        print(" \n".join(args_downcase))
downcase_all()