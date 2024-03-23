from app import app, db
from flask import jsonify, request, session
from uiElements.Button import Button
from uiElements.UiElement import UIElement
from uiElements.UIClick import UIClick
from uiElements.Container import Container
from uiElements.Card import Card


def getJsonResult(obj):
    return {obj.__class__.__name__.lower(): toDict(obj)}


def toDict(obj):
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(toDict(item))
        else:
            element = toDict(val)
        result[key] = element
    return result


@app.route("/")
def index():
    test_button = Button(1, "test", "/", "stop")
    test_card = Card(1, [], [], [test_button], [], "/", "play")

    return getJsonResult(test_card)
