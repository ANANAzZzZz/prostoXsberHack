from uiElements.UiElement import UIElement
from typing import List


class ListView(UIElement):
    def __init__(self, ord_par, elements_par: List[UIElement]):
        super().__init__(ord_par)
        self.elements = elements_par
