from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculation")
def calculation():
    return render_template("calculation.html")


@app.route("/<name>")
def home(name):
    return f"<h1>Čia {name} naujas puslapis</h1>"

@app.route("/names")
def name():
    vardai = ['Jonas', 'Antanas', 'Petras']
    return render_template("names.html", sarasas=vardai)

if __name__ == "__main__":
    app.run(debug=True)
