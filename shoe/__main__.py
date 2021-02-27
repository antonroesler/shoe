import sys
from .helloworld import hi

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    hi()

if __name__ == '__main__':
    main()