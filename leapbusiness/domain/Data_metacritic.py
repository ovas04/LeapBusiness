from dataclasses import dataclass


@dataclass
class DataMetacritic:
    metaScore: int
    userScore: float
    genres: list[str]
