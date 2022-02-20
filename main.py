from flask import Flask, render_template
from flask_wtf import FlaskForm
import json
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in str(prof) or 'строитель' in str(prof):
        sxema = ['Инженерные тренажеры', '/static/img/img.png']
    else:
        sxema = ['Научные симуляторы', '/static/img/img_1.png']
    return render_template('trainingg.html', image=sxema[1], text=sxema[0])


@app.route('/list_prof/<list>')
def show_list(list): # незнаю как указать путь до json файла, помогите пожалуйста
    tag = 0
    if list == 'ol':
        tag = 1
    elif list == 'ul':
        tag = 2
    with open("templates/list.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('list.html', news=news_list, tag=tag)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Авторизация', form=form)


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')

