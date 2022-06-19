from dataclasses import dataclass
from datetime import date


@dataclass
class DataSteamPriceHistory:
    date_price: date
    price: float
