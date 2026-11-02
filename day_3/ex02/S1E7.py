from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialise a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False

    def __str__(self):
        """Return a human-readable representation of the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Return the string representation of the character."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialise a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character through the class."""
        return cls(first_name, is_alive)

    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False

    def __str__(self):
        """Return a human-readable representation of the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Return the string representation of the character."""
        return self.__str__()
