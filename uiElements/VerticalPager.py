from uiElements.ListView import ListView
from uiElements.UiElement import UIElement
from typing import List


class VerticalPager(ListView):
    def __init__(self, ord_par, elements_par: List[UIElement]):
        super().__init__(ord_par, elements_par)
