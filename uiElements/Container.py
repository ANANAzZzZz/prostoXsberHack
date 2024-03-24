from uiElements.UiElement import UIElement
from typing import List
from uiElements.Button import Button
from uiElements.Image import Image
from uiElements.TextField import TextField
from uiElements.EditTextField import EditTextField


class Container(UIElement):
    def __init__(self, ord_par, texts_par: List[TextField], edits_par: List[EditTextField],
                 buttons_par: List[Button], images_par: List[Image], bottom: UIElement = None):
        super().__init__(ord_par)
        self.texts = texts_par
        self.edits = edits_par
        self.buttons = buttons_par
        self.images = images_par
        self.bottom = bottom
