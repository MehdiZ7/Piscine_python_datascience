import os


def ft_tqdm(lst: range) -> None:
    '''Function that mimic the tqdm function'''
    try:
        total = len(lst)
        term_size = os.get_terminal_size().columns
        for index, c in enumerate(lst, 1):
            perc = int(index / total * 100)
            left = f"{perc}%|["
            right = f"]| {index}/{total}"
            middle_size = max(0, term_size - len(left) - len(right) - 1)
            full = int((middle_size - 1) * (index / total))
            middle = "=" * full + ">" + " " * (middle_size - full - 1)
            print(f"{left}{middle}{right}\r", end="")
            yield c
    except (ZeroDivisionError, OSError):
        print("AssertionError: Impossible")
