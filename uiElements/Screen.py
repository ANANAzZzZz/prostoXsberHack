from ListView import ListView
from typing import List


class Screen:
    def __init__(self, content_par: ListView, title_par, route_par, parameters_par: List[str]):
        self.content = content_par
        self.title = title_par
        self.route = route_par
        self.parameters = parameters_par
