from typing import Any


def callLimit(limit: int):
    """Return a decorator limiting calls to a function."""
    count = 0

    def callLimiter(function):
        """Wrap function with a call limiter."""
        def limit_function(*args: Any, **kwds: Any):
            """Call function if the call limit is not exceeded."""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return None
            return function(*args, **kwds)
        return limit_function
    return callLimiter
