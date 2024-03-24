from typing import List

from uiElements.UiElement import UIElement
from uiElements.Button import Button
from uiElements.Container import Container
from uiElements.EditTextField import EditTextField
from uiElements.Image import Image
from uiElements.TextField import TextField


class Row(Container):
    def __init__(self, ord_par, texts_par: List[TextField], edits_par: List[EditTextField],
                 buttons_par: List[Button], images_par: List[Image], bottom: UIElement = None):

        super().__init__(ord_par, texts_par, edits_par, buttons_par, images_par, bottom)
