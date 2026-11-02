class SizeError(Exception):
    """Raised when two lists do not have the same length."""


def all_numbers(values: list) -> bool:
    """Return True if every value is an int or a float."""
    if all(type(v) in (int, float) for v in values):
        return True
    return False


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Compute the BMI of each person from paired height and weight.

    BMI is the weight in kilograms divided by the squared height in
    meters.

    Args:
        height: Heights in meters, as ints or floats.
        weight: Weights in kilograms, as ints or floats.

    Returns:
        A list of BMI values, one per person.

    Raises:
        TypeError: If height or weight is not a list.
        ValueError: If a list is empty, contains a non-numeric value, or
            contains a height or weight that is not strictly positive.
        SizeError: If height and weight do not have the same length.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Some arguments are not a list")
    if len(height) == 0 or len(weight) == 0:
        raise ValueError("Some lists are empty")
    if len(height) != len(weight):
        raise SizeError("Arguments are not the same size")
    if not all_numbers(height) or not all_numbers(weight):
        raise ValueError("Some arguments are not numbers")
    if any(v <= 0 for v in weight):
        raise ValueError("Weight can't be null or negative")
    if any(v <= 0 for v in height):
        raise ValueError("Height can't be null or negative")
    result = [w / (h ** 2) for w, h in zip(weight, height)]
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return whether each BMI is strictly above the limit.

    Args:
        bmi: BMI values, as ints or floats.
        limit: Threshold value. Floats are accepted even though the
            prototype declares an int.

    Returns:
        A list of booleans, True when the BMI is greater than the limit.

    Raises:
        TypeError: If bmi is not a list.
        ValueError: If bmi is empty, contains a non-numeric value, or if
            limit is not an int or a float.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI is not a list")
    if len(bmi) == 0:
        raise ValueError("BMI list is empty")
    if not all_numbers(bmi):
        raise ValueError("Some arguments are not numbers")
    if type(limit) not in (int, float):
        raise ValueError("The limit must be a number")
    result = [v > limit for v in bmi]
    return result


def main():
    """Run the module's self-tests, including error cases."""
    try:
        bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([2.71, 1.15], [165.3, 38.4]) -> {e}")

    try:
        give_bmi(0, [165.3, 38.4])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi(0, [165.3, 38.4]) -> {e}")

    try:
        give_bmi([], [])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([], []) -> {e}")

    try:
        give_bmi([2.12], [165.3, 38.4])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([2.12], [165.3, 38.4]) -> {e}")

    try:
        give_bmi([2.01, "abc"], [165.3, 38.4])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([2.01, 'abc'], [165.3, 38.4]) -> {e}")

    try:
        give_bmi([2.71, 0], [165.3, 38.4])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([2.71, 0], [165.3, 38.4]) -> {e}")

    try:
        give_bmi([2.71, 1.15], [165.3, 0])
    except (TypeError, SizeError, ValueError) as e:
        print(f"give_bmi([2.71, 1.15], [165.3, 0]) -> {e}")

    try:
        apply_limit("abc", 26)
    except (TypeError, SizeError, ValueError) as e:
        print(f"apply_limit('abc', 26) -> {e}")

    try:
        apply_limit([], 26)
    except (TypeError, SizeError, ValueError) as e:
        print(f"apply_limit([], 26) -> {e}")

    try:
        apply_limit([22.5, "abc"], 26)
    except (TypeError, SizeError, ValueError) as e:
        print(f"apply_limit([22.5, 'abc'], 26) -> {e}")

    try:
        apply_limit([22.5, 29.0], "26")
    except (TypeError, SizeError, ValueError) as e:
        print(f"apply_limit([22.5, 29.0], '26') -> {e}")


if __name__ == "__main__":
    main()
