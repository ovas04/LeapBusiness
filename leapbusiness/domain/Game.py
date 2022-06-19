from dataclasses import dataclass, field
from datetime import date
from statistics import mean, mode, pstdev
from scipy.stats import t
from .Tag import Tag
from .Platform import Platform
from .Category import Category
from .Genre import Genre
from .Data_Metacritic import DataMetacritic
from .Data_SteamPriceHistory import DataSteamPriceHistory
from .Data_SteamCharts import DataSteamCharts
import math


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
    total_recommendations: int = field(init=False, default=None)
    lower_price: float = field(init=False, default=None)
    upper_price: float = field(init=False, default=None)
    mean_price: float = field(init=False, default=None)
    total_sales: float = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.total_recommendations = self.positive + self.negative

        if(self.prices != None):
            array_prices = []
            for i in self.prices:
                array_prices.append(i.price)

            mean_prices = mean(array_prices)
            pstdev_prices = pstdev(array_prices)
            value_critic = t.ppf(0.95, mean_prices)
            population = len(self.prices)
            upper_price = mean_prices + value_critic * \
                (pstdev_prices/math.sqrt(population))
            lower_price = mean_prices - value_critic * \
                (pstdev_prices/math.sqrt(population))

            if(not math.isnan(lower_price)):
                self.lower_price = lower_price
            if(not math.isnan(upper_price)):
                self.upper_price = upper_price
            self.mean_price = mean_prices

            self.total_sales = self.followers * 9.6 * 0.2 * self.mean_price
