from dataclasses import dataclass, field
from datetime import date
from .Tag import Tag
from .Platform import Platform
from .Category import Category
from .Genre import Genre
from .Data_Metacritic import DataMetacritic
from .Data_SteamPriceHistory import DataSteamPriceHistory
from .Data_SteamCharts import DataSteamCharts


@dataclass
class Game:
    # SteamSpy data
    appId: int
    name: str
    publisher: list[str]
    positive: int
    negative: int
    languages: list[str]
    tags: list[Tag]
    followers: int
    # SteamAPI data
    required_age: str
    is_free: bool
    platforms: list[Platform]
    url: str
    categories: list[Category]
    genres: list[Genre]
    release_date: date  # format
    # DataMetacritic
    metacritic: DataMetacritic
    # DataSteamPriceHistory
    prices: list[DataSteamPriceHistory]
    # DataSteamCharts
    players: list[DataSteamCharts]
    # Custom data or unmapped
    total_recommendations: int = field(init=False)
    minor_price: float = field(init=False)
    upper_price: float = field(init=False)
    mean_price: float = field(init=False)
    total_sales: float = field(init=False)

    def __post_init__(self) -> None:
        self.total_recommendations = self.positive + self.negative
        self.minor_price = 1
        self.upper_price = 1
        self.mean_price = 1
        self.total_sales = 1
