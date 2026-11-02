import sys


def main():
    '''This program translate an input into code morse'''
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    try:
        assert len(sys.argv) == 2
        error = False
        for c in sys.argv[1]:
            if (not c.isalnum() and not c.isspace()):
                error = True
        assert error is False
        line = sys.argv[1].upper()
        ret = ""
        for c in line:
            ret += NESTED_MORSE[c]
        print(ret.rstrip())
    except (AssertionError, KeyError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
