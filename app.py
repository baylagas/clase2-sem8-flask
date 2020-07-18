from flask import Flask, render_template, request
from alumnologic import AlumnoLogic


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:  # "POST"
        name = request.form["name"]
        age = request.form["age"]
        logic = AlumnoLogic()
        rows = logic.insertNewAlumno(name, age)
        message = f"{rows} affected"
        return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
