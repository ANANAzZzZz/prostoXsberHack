from uiElements.UiElement import UIElement


class EditTextField(UIElement):
    def __init__(self, ord_par, value_par, key_par, hint_par):
        super().__init__(ord_par)
        self.value = value_par
        self.key = key_par
        self.hint = hint_par
