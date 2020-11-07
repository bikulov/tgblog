import datetime

import database
import update


def test_insert():
    db = database.Database()

    updates = [
        update.Update(
            chat_id="1",
            message_id="1",
            date=datetime.datetime(2020, 11, 8, 22, 00),
            chat_title="chat",
            message="hello",
            json_data="{}"
        ),
        update.Update(
            chat_id="1",
            message_id="2",
            date=datetime.datetime(2020, 11, 8, 22, 10),
            chat_title="chat",
            message="bye",
            json_data="{}"
        ),
        update.Update(
            chat_id="1",
            message_id="2",
            date=datetime.datetime(2020, 11, 8, 22, 10),
            chat_title="chat",
            message="bye",
            json_data="{}"
        ),
        update.Update(
            chat_id="2",
            message_id="1",
            date=datetime.datetime(2020, 11, 8, 22, 00),
            chat_title="chat",
            message="hello",
            json_data="{}"
        ),
    ]

    db.insert(updates)

    assert list(map(str, db.get_all("1"))) == list(map(str, [updates[1], updates[0]]))
    assert list(map(str, db.get_all("2"))) == list(map(str, [updates[-1]]))
    assert list(map(str, db.get_all("3"))) == []
