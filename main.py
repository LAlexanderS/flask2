from flask import Flask
app = Flask(__name__)
n1 = '\n'
@app.route("/")
def main_page():
    return "Hello"


@app.route("/profile/")
def page_pers():
    return f'Имя кандидата: Позиция кандидата: Навыки кандидата: '

app.run()
