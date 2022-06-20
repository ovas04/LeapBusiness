from dataclasses import dataclass


@dataclass(slots=True)
class Genre:
    id: int
    desc: str
