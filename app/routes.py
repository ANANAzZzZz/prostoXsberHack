from flask import jsonify
from flask import request, redirect
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from TypeButton import TypeButton
from app import app, db
from forms import LoginForm
from uiElements.Button import Button
from uiElements.Card import Card
from uiElements.Column import Column
from uiElements.EditTextField import EditTextField
from uiElements.FlowNavigation import FlowNavigation
from uiElements.Image import Image
from uiElements.LazyColumn import LazyColumn
from uiElements.Navigation import Navigation
from uiElements.Row import Row
from uiElements.Screen import Screen
from uiElements.TextField import TextField
from user import User


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    treks = db.getTrack()

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
        return getJsonResult(FlowNavigation([Screen(
            LazyColumn(
                0,
                [
                    Card(ord_par=0,
                         texts_par=[
                             TextField(
                                 0,
                                 "Привет, " + user.name + " " + user.lastname
                             )
                         ],
                         route_par="",
                         type_par="",
                         route_navigation_par="",
                         images_par=[],
                         edits_par=[],
                         buttons_par=[]
                         ),
                    LazyColumn(
                        0,
                        [
                            TextField(0, "Треки"),
                            LazyColumn(1, list(
                                map(
                                    lambda task: Card(
                                        0,
                                        [],
                                        [],
                                        [],
                                        [],
                                        "",
                                        "",
                                        "",
                                        Row(
                                            0,
                                            [TextField(1, task["name"])],
                                            [],
                                            [],
                                            [Image(0, task["image"])]
                                        )
                                    ), treks)))
                        ]
                    )
                ],
            ),
            "Главный экран",
            "main",
            []
        ),
        ], "main", "mainFlow")), 200
        # jsonify(message='Пользователь авторизован'), 200
    return jsonify(message='Пост запрос не выполнен'), 400


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/getStartFlow')
def getStartFlow():
    param = request.args
    if param.get('param') != "mobile":
        return getJsonResult(FlowNavigation([
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            buttons_par=[
                                Button(
                                    1,
                                    "Начать",
                                    "",
                                    TypeButton.Navigate.name,
                                    "login"
                                )
                            ],
                            texts_par=[],
                            edits_par=[],
                            images_par=[Image(0, "https://i.ibb.co/vHF7c5J/LOGO11.png")]
                        )
                    ]
                ),
                "Splash",
                "splash",
                parameters_par=[]
            ),
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            edits_par=[
                                EditTextField(
                                    0,
                                    "",
                                    "username",
                                    "Логин"
                                ), EditTextField(
                                    1,
                                    "",
                                    "password",
                                    "Пароль"
                                )
                            ],
                            texts_par=[],
                            buttons_par=[

                            ],
                            images_par=[],
                            bottom=Row(
                                ord_par=0,
                                edits_par=[],
                                texts_par=[],
                                buttons_par=[Button(
                                    2,
                                    "Вход",
                                    "login",
                                    TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                    "mainFlow"
                                ),
                                    Button(
                                        3,
                                        "Зарегистрироваться",
                                        "",
                                        TypeButton.Navigate.name,
                                        "authorization"
                                    )],
                                images_par=[]
                            )
                        )
                    ]
                ),
                "Вход",
                "login",
                []
            ),
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            edits_par=[
                                EditTextField(
                                    0,
                                    "",
                                    "username",
                                    "Логин"
                                ),
                                EditTextField(
                                    1,
                                    "",
                                    "password",
                                    "Пароль"
                                ),
                                EditTextField(
                                    2,
                                    "",
                                    "name",
                                    "Имя"
                                ),
                                EditTextField(
                                    3,
                                    "",
                                    "lastname",
                                    "Фамилия"
                                ),
                            ],
                            texts_par=[],
                            buttons_par=[
                                Button(
                                    4,
                                    "Зарегестрироваться",
                                    "register",
                                    TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                    "mainFlow"
                                )
                            ],
                            images_par=[]
                        )
                    ]
                ),
                "Авторизация",
                "authorization",
                []
            )], "splash", "startFlow"))

    return getJsonResult(FlowNavigation([
        Screen(
            LazyColumn(
                0,
                [
                    Column(
                        ord_par=0,
                        buttons_par=[
                            Button(
                                1,
                                "Начать",
                                "",
                                TypeButton.Navigate.name,
                                "login"
                            )
                        ],
                        texts_par=[],
                        edits_par=[],
                        images_par=[Image(0, "https://i.ibb.co/vHF7c5J/LOGO11.png")]
                    )
                ]
            ),
            "Splash",
            "splash",
            parameters_par=[]
        ),
        Screen(
            LazyColumn(
                0,
                [
                    Column(
                        ord_par=0,
                        edits_par=[
                            EditTextField(
                                0,
                                "",
                                "username",
                                "Логин"
                            ), EditTextField(
                                1,
                                "",
                                "password",
                                "Пароль"
                            )
                        ],
                        texts_par=[],
                        buttons_par=[
                            Button(
                                2,
                                "Вход",
                                "login",
                                TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                "mainFlow"
                            ),
                            Button(
                                3,
                                "Зарегистрироваться",
                                "",
                                TypeButton.Navigate.name,
                                "authorization"
                            )
                        ],
                        images_par=[]
                    )
                ]
            ),
            "Вход",
            "login",
            []
        ),
        Screen(
            LazyColumn(
                0,
                [
                    Column(
                        ord_par=0,
                        edits_par=[
                            EditTextField(
                                0,
                                "",
                                "username",
                                "Логин"
                            ),
                            EditTextField(
                                1,
                                "",
                                "password",
                                "Пароль"
                            ),
                            EditTextField(
                                2,
                                "",
                                "name",
                                "Имя"
                            ),
                            EditTextField(
                                3,
                                "",
                                "lastname",
                                "Фамилия"
                            ),
                        ],
                        texts_par=[],
                        buttons_par=[
                            Button(
                                4,
                                "Зарегестрироваться",
                                "register",
                                TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                "mainFlow"
                            )
                        ],
                        images_par=[]
                    )
                ]
            ),
            "Авторизация",
            "authorization",
            []
        )], "splash", "startFlow"))


@app.route('/navigation')
def navigation():
    mainNavigation = Navigation(
        [FlowNavigation([
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            buttons_par=[
                                Button(
                                    1,
                                    "Начать",
                                    "",
                                    TypeButton.Navigate.name,
                                    "login"
                                )

                            ],
                            texts_par=[],
                            edits_par=[],
                            images_par=[Image(0, "https://i.ibb.co/vHF7c5J/LOGO11.png")]
                        )
                    ]
                ),
                "Splash",
                "splash",
                parameters_par=[]
            ),
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            edits_par=[
                                EditTextField(
                                    0,
                                    "",
                                    "username",
                                    "Логин"
                                ), EditTextField(
                                    1,
                                    "",
                                    "password",
                                    "Пароль"
                                )
                            ],
                            texts_par=[],
                            buttons_par=[
                                Button(
                                    2,
                                    "Вход",
                                    "login",
                                    TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                    "mainFlow"
                                ),
                                Button(
                                    3,
                                    "Зарегистрироваться",
                                    "",
                                    TypeButton.Navigate.name,
                                    "authorization"
                                )
                            ],
                            images_par=[]
                        )
                    ]
                ),
                "Вход",
                "login",
                []
            ),
            Screen(
                LazyColumn(
                    0,
                    [
                        Column(
                            ord_par=0,
                            edits_par=[
                                EditTextField(
                                    0,
                                    "",
                                    "username",
                                    "Логин"
                                ),
                                EditTextField(
                                    1,
                                    "",
                                    "password",
                                    "Пароль"
                                ),
                                EditTextField(
                                    2,
                                    "",
                                    "name",
                                    "Имя"
                                ),
                                EditTextField(
                                    3,
                                    "",
                                    "lastname",
                                    "Фамилия"
                                ),
                            ],
                            texts_par=[],
                            buttons_par=[
                                Button(
                                    4,
                                    "Зарегестрироваться",
                                    "register",
                                    TypeButton.Create.name + "/" + TypeButton.Navigate.name,
                                    "mainFlow"
                                )
                            ],
                            images_par=[]
                        )
                    ]
                ),
                "Авторизация",
                "authorization",
                []
            )], "splash", "startFlow"),
            FlowNavigation([Screen(
                LazyColumn(
                    0,
                    [
                        Card(ord_par=0,
                             texts_par=[
                                 TextField(
                                     0,
                                     "Привет, penis"
                                 )
                             ],
                             route_par="",
                             type_par="",
                             route_navigation_par="",
                             images_par=[],
                             edits_par=[],
                             buttons_par=[]
                             ),
                        LazyColumn(
                            0,
                            [
                                TextField(0, "Треки"),
                                LazyColumn(1, [])
                            ],
                        )
                    ],
                ),
                "Главный экран",
                "main",
                []
            ),
            ], "main", "mainFlow")
        ],
        "startFlow"
    )

    return getJsonResult(mainNavigation)


mainFlow = FlowNavigation([Screen(
    LazyColumn(
        0,
        [
            Card(ord_par=0,
                 texts_par=[
                     TextField(
                         0,
                         "Привет, penis"
                     )
                 ],
                 route_par="",
                 type_par="",
                 route_navigation_par="",
                 images_par=[],
                 edits_par=[],
                 buttons_par=[]
                 ),
            LazyColumn(
                0,
                [
                    TextField(0, "Треки")
                ]
            )
        ],
    ),
    "Главный экран",
    "main",
    []
),
], "main", "mainFlow")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if db.getUserByLogin(request.form["username"]):
            print("Пользователь существует")
            return jsonify(message="Пользователь существует"), 401
        if not db.addUser(request):
            print("неудачная попытка регистрации")
            return jsonify(message='неудачная попытка регистрации'), 401
        print("пользователь зарегистрирован")
        return getJsonResult(FlowNavigation([Screen(
            LazyColumn(
                0,
                [
                    Card(ord_par=0,
                         texts_par=[
                             TextField(
                                 0,
                                 "Привет, " + request.form['name'] + " " + request.form['lastname']
                             )
                         ],
                         route_par="",
                         type_par="",
                         route_navigation_par="",
                         images_par=[],
                         edits_par=[],
                         buttons_par=[]
                         ),
                    LazyColumn(
                        0,
                        [
                            TextField(0, "Треки"),
                            LazyColumn(1, [])
                        ]
                    )
                ],
            ),
            "Главный экран",
            "main",
            []
        ),
        ], "main", "mainFlow"))
        # jsonify(message='пользователь зарегистрирован'), 200
    return jsonify(message='Пост запрос не выполнен'), 400
