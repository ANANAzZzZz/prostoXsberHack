from uiElements.UiElement import UIElement


class Image(UIElement):
    def __init__(self, ord_par, url_par):
        super().__init__(ord_par)
        self.url = url_par
