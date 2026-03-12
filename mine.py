from flask import Flask, render_template, redirect

from static.form.login_form import LoginForm

from data import db_session

app = Flask(__name__)

app.config["SECRET_KEY"] = "password123"





@app.route("/")
def main():
    return "Миссия Колонизация Марса"

@app.route("/index")
def index():
    return render_template("base.html", title="Заготовка")

@app.route("/promotion")
def promotion():
    return ("<p>Человечество вырастает из детства.</p>"
            "<p>Человечеству мала одна планета.</p>"
            "<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>"
            "<p>И начнем с Марса!</p>"
            "<p>Присоединяйся!</p>")

@app.route("/image_mars")
def image_mars():
    return render_template("image_mars.html")

@app.route("/promotion_image")
def promotion_image():
    return render_template("promotion_image.html")

@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html", title="Отбор астронавтов")

@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)

@app.route("/answer")
@app.route("/auto_answer")
def answer():
    context = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
    }
    return render_template("auto_answer.html", **context)

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    app.run("127.0.0.1", 8080)