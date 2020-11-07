from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from update import Update


class Database:
    def __init__(self, db_file=":memory:", echo=False):
        self.engine = create_engine(f"sqlite:///{db_file}", echo=echo)
        Update.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def insert(self, updates):
        for upd in updates:
            self.session.merge(upd)
        self.session.commit()

    def get_all(self, chat_id):
        return self.session.query(Update)\
            .filter(Update.chat_id == chat_id)\
            .order_by(Update.date.desc())\
            .all()
