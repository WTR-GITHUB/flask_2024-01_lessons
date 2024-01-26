from db_main import db, Message, app
from flask import request, render_template


@app.route("/login", methods=["GET", "POST"]) # type: ignore
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        check_email = Message.query.filter_by(email=email).first()
        if check_email is None:
            new_message = Message(name=name, email=email, message=message)
            db.session.add(new_message)
            db.session.commit()
            return render_template("greetings.html", var=name)
        else:
            return render_template("email.html", var=email)
    elif request.method == "GET":
        return render_template("login.html")


@app.route("/all", methods=["GET", "POST"])
def all():
    if request.method == "POST":
        email = request.form["email"]
        query = Message.query.filter_by(email=email).first()
        db.session.delete(query)
        db.session.commit()
    all_messages = Message.query.all()
    return render_template("all.html", all=all_messages)


if __name__ == "__main__":
    app.run(debug=True)
