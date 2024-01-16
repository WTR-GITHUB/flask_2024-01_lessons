from db_main import app, Message

with app.app_context():
    all_messages = Message.query.all()
    for i in all_messages:
        print(i.message)

    message_antanas = Message.query.filter_by(name="Antanas")
    print(message_antanas[0].message)

    # message_1 = Message.query.get(1)
    # print(message_1)

# Jonas - jonas@mail.com
