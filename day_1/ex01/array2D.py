class SizeError(Exception):
    """Raised when a list is empty or its rows have unequal lengths."""


def all_number(value: list) -> bool:
    """Return True if every value of a 2D list is an int or a float.

    Args:
        value: A list of rows, each row being a list of values."""
    if all(type(v) in (int, float) for row in value for v in row):
        return True
    return False


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list and return a slice of its rows.

    The input shape is printed before slicing, then the shape of the
    returned slice is printed. Slicing follows Python rules: start is
    included, end is excluded, negative indexes are allowed, and
    out-of-range bounds are clamped.

    Args:
        family: A non-empty rectangular 2D list of ints or floats.
        start: Index of the first row to keep.
        end: Index after the last row to keep.

    Returns:
        The rows family[start:end]. An empty slice is valid and has
        shape (0, number_of_columns).

    Raises:
        TypeError: If family is not a list, if a row is not a list, or
            if start or end is not an int.
        SizeError: If family is empty or if its rows do not all have
            the same length.
        ValueError: If a value is not an int or a float.
    """
    if not isinstance(family, list):
        raise TypeError("The family must be a list")
    if len(family) == 0:
        raise SizeError("The family can't be empty")
    if not all(isinstance(v, list) for v in family):
        raise TypeError("Every line of the family must be a list")
    if not all(len(v) == len(family[0]) for v in family):
        raise SizeError("Every line must be the same size")
    if not all_number(family):
        raise ValueError("Every value must be a number")
    if type(start) is not int or type(end) is not int:
        raise TypeError("Start and End must be an int")
    shape = (len(family), len(family[0]))
    print(f"My shape is : {shape}")
    result = family[start:end]
    shape = (len(result), len(family[0]))
    print(f"My new shape is : {shape}")
    return result


def main():
    """Run the module's self-tests, including error cases."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
        ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print(slice_me(family, 10, 20))

    try:
        slice_me("family", 0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me('family', 0, 2) -> {e}")

    try:
        slice_me([], 0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me([], 0, 2) -> {e}")

    try:
        slice_me([[1.80, 78.4], [2.15]], 0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me(ragged, 0, 2) -> {e}")

    try:
        slice_me([1.80, 78.4], 0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me([1.80, 78.4], 0, 2) -> {e}")

    try:
        slice_me([[1.80, "abc"], [2.15, 102.7]], 0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me([[1.80, 'abc'], ...], 0, 2) -> {e}")

    try:
        slice_me(family, 0.0, 2)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me(family, 0.0, 2) -> {e}")

    try:
        slice_me(family, 0, True)
    except (TypeError, SizeError, ValueError) as e:
        print(f"slice_me(family, 0, True) -> {e}")


if __name__ == "__main__":
    main()
