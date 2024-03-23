from uiElements.Screen import Screen
from typing import List


class Navigation:
    def __init__(self, screens_par: List[Screen], start_route_par):
        self.screens = screens_par
        self.startRoute = start_route_par
