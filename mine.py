from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data.db_session import create_session
from data.jobs import Jobs
from data.user import User
from form.jobs_form import JobsForm
from form.login_form import LoginForm

from data import db_session
from api import api

app = Flask(__name__)
app.register_blueprint(api)

app.config["SECRET_KEY"] = "password123"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    session = db_session.create_session()
    return session.get(User, user_id)


@app.route("/")
@app.route("/index")
def index():
    session = create_session()
    result = session.query(Jobs, User).join(
        User,
        Jobs.team_leader == User.id
    )
    return render_template("index.html", title="Главная страница", result=result)

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
        session = db_session.create_session()
        user = session.query(User).filter(
            User.email == login_form.email.data
        ).first()
        if user and user.check_password(login_form.password.data):
            login_user(user, login_form.remember_me)
            return redirect("/")
        else:
            return render_template("login.html", form=login_form,
                                   massage="Такого пользователя не существует")
    return render_template("login.html", form=login_form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/addjob", methods=["GET", "POST"])
@login_required
def addjob():
    jobs_form = JobsForm()
    if jobs_form.validate_on_submit():
        session = db_session.create_session()
        first_job = Jobs(
            job=jobs_form.job.data,
            team_leader=jobs_form.team_leader.data,
            work_size=jobs_form.work_size.data,
            collaborators=jobs_form.collaborators.data,
            is_finished=jobs_form.is_finished.data
        )

        session.add(first_job)
        session.commit()
        return redirect("/")
    return render_template("addjob.html", form=jobs_form, title="Adding a job")


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    app.run("127.0.0.1", 8080)