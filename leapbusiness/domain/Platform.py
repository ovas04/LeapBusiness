from dataclasses import dataclass


@dataclass(slots=True)
class Platform:
    desc: str
    state: bool
