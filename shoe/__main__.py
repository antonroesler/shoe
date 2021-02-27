import sys
from .module import f


def add(x):
    print(f"{x} kilometers added to shoe.")


def main():
    args = sys.argv[1:]
    func = f[args[0]]
    try:
        func(args[1:])
    except (IndexError, TypeError):
        func()




if __name__ == '__main__':
    main()