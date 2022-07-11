from dataclasses import dataclass


@dataclass(slots=True)
class DataMetacritic:
    metaScore: int = None
    userScore: float = None
    genres: list[str] = None
