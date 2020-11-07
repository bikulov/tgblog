import update
import datetime

def test_to_string():
    u = update.Update(
        chat_id="1",
        message_id="1",
        date=datetime.datetime(2020, 11, 8, 22, 00),
        chat_title="chat",
        message="hello",
        json_data="{}"
    )

    assert str(u) == """<Update(
    chat_id=1
    message_id=1
    date=2020-11-08 22:00:00
    chat_title=chat
    message=hello
    {}
)>"""