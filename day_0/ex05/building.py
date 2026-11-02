import sys


def count(string: str):
    '''This function is used to count the types of letters
    and print them on screen'''
    up, low, punct, spa, dig = 0, 0, 0, 0, 0
    print(f"The text contains {len(string)} characters:")
    for c in string:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif not c.isalnum() and not c.isspace():
            punct += 1
        elif c.isspace():
            spa += 1
        elif c.isdigit():
            dig += 1
        else:
            continue
    print(up, "upper letters")
    print(low, "lower letters")
    print(punct, "punctuation marks")
    print(spa, "spaces")
    print(dig, "digits")


def main():
    """In this function we check the numbers of arguments
    then call the function count"""
    try:
        assert len(sys.argv) < 3, ("AssertionError: More than one "
                                   "argument is provided")
        if (len(sys.argv) == 2):
            count(sys.argv[1])
        else:
            print("What is the text to count?")
            line = sys.stdin.readline()
            count(line)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
