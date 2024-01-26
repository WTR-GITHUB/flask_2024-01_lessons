import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculation")
def calculation():
    return render_template("calculation.html")


@app.route("/keliamieji")
def home():
    start = 1900
    end = 2100
    leap_year = []
    while start < end:
        if start % 4 == 0 and start % 100 != 0:
            leap_year.append(start)
        if start % 100 == 0 and start % 400 == 0:
            leap_year.append(start)
        start += 1

    return render_template(
        "keliamieji.html", keliamieji=leap_year, start=1900, end=2100
    )


@app.route("/tikrinti", methods=["GET", "POST"])
def check_year():
    if request.method == "POST":
        year_1 = int(request.form["metai"])
        if (year_1 % 4 == 0 and year_1 % 100 != 0) or (
            year_1 % 100 == 0 and year_1 % 400 == 0
        ):
            return render_template("tikrinti.html", yes=f"This is leap year: {year_1}")
        else:
            return render_template(
                "tikrinti.html", yes=f"This is not leap year: {year_1}"
            )
    else:
        return render_template("tikrinti.html")


@app.route("/names")
def name():
    vardai = ["Jonas", "Antanas", "Petras"]
    return render_template("names.html", sarasas=vardai)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", var=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
