class calculator:
    """A calculator that applies scalar operations to a vector."""

    def __init__(self, values):
        """Initialise the calculator with a list of values."""
        self.values = values

    def __add__(self, other) -> None:
        """Add a scalar to each value and print the result."""
        self.values = [x + other for x in self.values]
        print(self.values)

    def __sub__(self, other) -> None:
        """Subtract a scalar from each value and print the result."""
        self.values = [x - other for x in self.values]
        print(self.values)

    def __mul__(self, other) -> None:
        """Multiply each value by a scalar and print the result."""
        self.values = [x * other for x in self.values]
        print(self.values)

    def __truediv__(self, other) -> None:
        """Divide each value by a scalar and print the result."""
        try:
            self.values = [x / other for x in self.values]
            print(self.values)
        except ZeroDivisionError:
            print("Error: Division by 0")
