from dataclasses import dataclass


@dataclass(slots=True)
class Category:
    id: int
    desc: str
