from uiElements.UiElement import UIElement


class TextField(UIElement):
    def __init__(self, ord_par, value_par):
        super().__init__(ord_par)
        self.value = value_par
