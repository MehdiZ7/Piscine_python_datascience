from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    def __init__(self, first_name, is_alive=True):
        """Initialise a character with a first name and an alive state."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's health state to dead."""
        ...


class Stark(Character):
    """Represent a member of House Stark."""

    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False
