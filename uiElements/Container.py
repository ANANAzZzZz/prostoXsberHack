from uiElements.UiElement import UIElement
from typing import List
from Button import Button
from Image import Image
from TextField import TextField
from EditTextField import EditTextField


class Container(UIElement):
    def __init__(self, ord_par, texts_par: List[TextField], edits_par: List[EditTextField],
                 buttons_par: List[Button], images_par: List[Image]):
        super().__init__(ord_par)
        self.texts = texts_par
        self.edits = edits_par
        self.buttons = buttons_par
        self.images = images_par
