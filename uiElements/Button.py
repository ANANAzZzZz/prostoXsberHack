from uiElements.UiElement import UIElement


class Button(UIElement):
    def __init__(self, ord_par, text_par, route_par, type_par):
        super().__init__(ord_par)
        self.text = text_par
        self.route = route_par
        self.type = type_par
