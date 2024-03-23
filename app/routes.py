from app import app, db
from flask import jsonify, request, session
from uiElements.Button import Button
from uiElements.UiElement import UIElement
from uiElements.UIClick import UIClick
from uiElements.Container import Container
from uiElements.Card import Card
from uiElements.Screen import Screen
from uiElements.LazyColumn import LazyColumn
from uiElements.TextField import TextField
from uiElements.EditTextField import EditTextField
from uiElements.Navigation import Navigation


def getJsonResult(obj):
    # {obj.__class__.__name__.lower(): toDict(obj)}
    return toDict(obj)


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
    mainNavigation = Navigation(
        screens_par=[
            Screen(
                content_par=LazyColumn(0,
                                       [
                                           Card(
                                               ord_par=0,
                                               texts_par=[TextField(0, "Проверка123")],
                                               edits_par=[
                                                   EditTextField(2, "Привет", "hello", "test"),
                                                   EditTextField(1, "Пока", "hello1", "test23")
                                               ],
                                               buttons_par=[
                                                   Button(
                                                       2,
                                                       "Проверка",
                                                       "test",
                                                       "Navigate"
                                                   )
                                               ],
                                               images_par=[],
                                               route_par="",
                                               type_par=""
                                           ),

                                           Card(
                                               ord_par=0,
                                               texts_par=[TextField(0, "Проверка12")],
                                               edits_par=[
                                                   EditTextField(2, "Привет", "hello", "test"),
                                                   EditTextField(1, "Пока", "hello1", "test23")
                                               ],
                                               buttons_par=[
                                                   Button(
                                                       2,
                                                       "Проверка",
                                                       "",
                                                       "Create"
                                                   )
                                               ],
                                               images_par=[],
                                               route_par="",
                                               type_par=""
                                           ),
                                       ]
                                       ),
                title_par="Test1",
                route_par="test",
                parameters_par=[]
            )
        ],
        start_route_par="test"
    )

    return getJsonResult(mainNavigation)
