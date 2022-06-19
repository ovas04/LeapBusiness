from dataclasses import dataclass
from datetime import date


@dataclass
class DataSteamCharts:
    mounth: date  # review
    avg_players: float
    peak_players: float
