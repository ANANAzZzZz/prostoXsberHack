from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, PasswordField, validators)


# Форма регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Логин', [validators.Length(min=4, max=25), validators.InputRequired()])
    name = StringField('Имя', [validators.Length(min=4, max=25), validators.InputRequired()])
    lastname = StringField('Фамилия', [validators.Length(min=4, max=25), validators.InputRequired()])

    password = PasswordField('Пароль', [
        validators.InputRequired(),
        validators.Length(min=6, max=100),
    ])


# Форма авторизации
class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25), validators.InputRequired()])
    password = PasswordField('Пароль', [
        validators.InputRequired(),
        validators.Length(min=6, max=100),
    ])
    remember_me = BooleanField('Запомнить меня')