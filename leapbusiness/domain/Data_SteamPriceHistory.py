from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class DataSteamPriceHistory:
    date_price: date
    price: float
