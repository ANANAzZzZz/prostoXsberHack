from app import app, db
from flask import jsonify, request, session
from uiElements.Button import Button
from uiElements.UiElement import UIElement
from uiElements.UIClick import UIClick


def convert_button_to_dict(button):
    button_dict = {}
    for attr in vars(button):
        attr_value = getattr(button, attr)
        if isinstance(attr_value, UIElement):
            UIElement_dict = vars(attr_value)
            button_dict[attr] = UIElement_dict
        else:
            button_dict[attr] = attr_value

    return button_dict


@app.route("/")
def index():
    test_button = Button(1, "test", "/", "stop")

    return convert_button_to_dict(test_button)

