from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run("127.0.0.1", 8080)