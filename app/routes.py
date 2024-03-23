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
from werkzeug.security import check_password_hash
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

    return getJsonResult(mainNavigation)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_result = db.getUserByLogin(request.form['username'])
        # Проверка совпадения хэш-пароля из бд и введенного пользователем
        if user_result is None or not check_password_hash(user_result[2], request.form['password']):
            #flash('Неверное имя пользователя или пароль', 'error')
            return redirect('/login')

        id, login, password, role, is_banned = user_result
        # проверка на блоировку пользователя
        if user_result[4]:
            #flash('Данный пользователь заблокирован администратором', 'error')
            return redirect('/login')

        user = User(id, login, password, role)
        login_user(user, remember=login_form.remember_me.data)
        #flash(f'Вы успешно авторизованы, {current_user.login}', 'success')
        # переход на страницу пользователя
        return redirect('/main')
    return render_template('login.html', title='Авторизация', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/main')
def main():
    print('...')
