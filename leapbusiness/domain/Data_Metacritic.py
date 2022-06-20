from dataclasses import dataclass


@dataclass(slots=True)
class DataMetacritic:
    metaScore: int
    userScore: float
    genres: list[str]
