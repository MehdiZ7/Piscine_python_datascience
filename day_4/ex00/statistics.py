from typing import Any


def moy(values: list, n: int) -> float:
    """Return the arithmetic mean of the given values."""
    return sum(values) / n


def med(values: list, n: int) -> int | float:
    """Return the median of the given values."""
    s = sorted(values)
    if n % 2 == 1:
        median = s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2
    return median


def percentile(values: list, p: float, n: int) -> float:
    """Return the percentile p of the given values."""
    s = sorted(values)
    k = (n - 1) * p
    low = int(k)
    high = min(low + 1, n - 1)

    res = s[low] + (s[high] - s[low]) * (k - low)
    return res


def var(values: list, n: int) -> float:
    """Return the population variance of the given values."""
    m = moy(values, n)
    variance = sum((x - m) ** 2 for x in values) / n
    return variance


def std(values: list, n: int) -> float:
    """Return the population standard deviation of the given values."""
    return var(values, n) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and print the requested statistics."""
    n = len(args)
    for x in kwargs.values():
        if x == "mean":
            if n == 0:
                print("ERROR")
            else:
                print(f"mean : {moy(list(args), n)}")
        elif x == "median":
            if n == 0:
                print("ERROR")
            else:
                print(f"median : {med(list(args), n)}")
        elif x == "quartile":
            if n == 0:
                print("ERROR")
            else:
                q1 = percentile(args, 0.25, n)
                q3 = percentile(args, 0.75, n)
                print(f"quartile : {[q1, q3]}")
        elif x == "var":
            if n == 0:
                print("ERROR")
            else:
                print(f"var : {var(args, n)}")
        elif x == "std":
            if n == 0:
                print("ERROR")
            else:
                print(f"std : {std(args, n)}")
