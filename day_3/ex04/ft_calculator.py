class calculator:
    """A calculator for vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of two vectors."""
        res = 0
        for x, y in zip(V1, V2):
            res = res + x * y
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print the sum of two vectors."""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print the difference of two vectors."""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
