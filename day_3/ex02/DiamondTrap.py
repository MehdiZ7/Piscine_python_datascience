from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represent the king Joffrey."""

    def get_eyes(self):
        """Return the colour of the king's eyes."""
        return self.eyes

    def set_eyes(self, value):
        """Set the colour of the king's eyes."""
        self.eyes = value

    def get_hairs(self):
        """Return the colour of the king's hairs."""
        return self.hairs

    def set_hairs(self, value):
        """Set the colour of the king's hairs."""
        self.hairs = value
