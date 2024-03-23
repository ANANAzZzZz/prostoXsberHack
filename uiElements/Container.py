from uiElements.UiElement import UIElement


class Container(UIElement):
    def __init__(self, ord_par):
        super().__init__(ord_par)

        # Todo - add other members


cont = Container(10)
print(cont.ord)
