from Screen import Screen
from typing import List


class Navigator:
    def __init__(self, screens_par: List[Screen], start_route_par):
        self.screens = screens_par
        self.startRote = start_route_par
