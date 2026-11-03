import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-letter lowercase identifier."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with a generated login and identifier."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Set the login and the identifier after initialisation."""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
