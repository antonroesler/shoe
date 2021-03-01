import sys
from .module import functions
from .manual import man_page


def main():
    args = sys.argv[1:]
    if args:
        f_name = args[0]
        if f_name in functions:
            call_function(f_name, args)
        else:
            call_function("info", [0, f_name])  # TODO: Find better solution
    else:
        man_page()


def call_function(f_name, args):
    if len(args) > 1:
        functions[f_name](args[1:])
    else:
        functions[f_name]()


if __name__ == '__main__':
    main()