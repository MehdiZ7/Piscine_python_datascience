def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a callable applying function to the previous result."""
    def inner() -> float:
        """Apply function to the current value and return it."""
        nonlocal x
        x = function(x)
        return x
    return inner
