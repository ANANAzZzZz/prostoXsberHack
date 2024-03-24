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
from flask_login import current_user, login_user, logout_user
from flask import render_template, url_for, request, flash, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from user import User
from forms import LoginForm, RegistrationForm


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
    print(generate_password_hash('abba'))
    return getJsonResult(mainNavigation)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == "POST":
        user_result = db.getUserByLogin(request.form['username'])

        # Проверка совпадения хэш-пароля из бд и введенного пользователем
        if user_result is None or not check_password_hash(user_result['password'], request.form['password']):
            return jsonify(message='Неверные учетные данные'), 401
        id, username, password, name, lastname = user_result
        # проверка на блоировку пользователя
        user = User(id, username, password, name, lastname)
        login_user(user, remember=login_form.remember_me.data)
        # переход на страницу пользователя
        return jsonify(message='Пользователь авторизован'), 200
    return jsonify(message='Пост запрос не выполнен'), 400


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/main')
def main():
    return "we logged in"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if not db.addUser(request):
            print("неудачная попытка регистрации")
            return jsonify(message='неудачная попытка регистрации'), 401
        print("пользователь зарегистрирован")
        return jsonify(message='пользователь зарегистрирован'), 200
    return jsonify(message='Пост запрос не выполнен'), 400
