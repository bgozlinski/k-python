from dataclasses import dataclass
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


generate_id()


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.active = True
        self.email_addresses = []
        self._search_string = f'{self.name} {self.address}'

    def __repr__(self):
        return f"{self.name} {self.address}"


p = Person(name="Jan", address="123 Main St.")
print(p)
p._search_string

from typing import List
from  dataclasses import dataclass, field

@dataclass(kw_only=True, slots=False)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: List[str] = field(default_factory=list)
    id: str = field(repr=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f'{self.name} {self.address}'


p = Person(name="Jan", address="123 Main St.")
print(p._search_string)

print(vars(p))  # (kw_only=True, slots=False)
