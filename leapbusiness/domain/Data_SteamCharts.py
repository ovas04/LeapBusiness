from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class DataSteamCharts:
    mounth: date
    avg_players: float
    peak_players: float
