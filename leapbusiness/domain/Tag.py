from dataclasses import dataclass


@dataclass(slots=True)
class Tag:
    desc: str
    id: int
