from db_main import app, Message, db

with app.app_context():
    jonas = Message.query.filter_by(name="Jonas").first()
    db.session.delete(jonas)
    db.session.commit()
    print(Message.query.all())