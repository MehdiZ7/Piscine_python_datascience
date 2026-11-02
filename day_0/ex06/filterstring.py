import sys


def main():
    '''main function used to print a word after a filter function'''
    try:
        assert len(sys.argv) == 3
        nb = int(sys.argv[2])
        ret = [c for c in sys.argv[1].split() if (lambda x: len(x) > nb)(c)]
        print(ret)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
