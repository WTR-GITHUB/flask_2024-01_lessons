from db_main import app, Message, db

with app.app_context():
    antanas = Message.query.filter_by(name="Juozas").first()
    antanas.email = 'geras2.zmogus@lrs.lt'
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())