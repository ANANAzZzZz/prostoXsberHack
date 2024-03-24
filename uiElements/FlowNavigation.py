from uiElements.Screen import Screen
from typing import List


class FlowNavigation:
    def __init__(self, screens: List[Screen], startRoute: str, routeFlow: str):
        self.screens = screens
        self.startRoute = startRoute
        self.routeFlow = routeFlow
