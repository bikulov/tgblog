import json
import logging
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Update(Base):
    __tablename__ = "updates"

    chat_id = Column(Integer, primary_key=True)
    message_id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    chat_title = Column(String)
    message = Column(String)

    json_data = Column(String)   

    def __repr__(self):
        return f"""<Update(
    chat_id={self.chat_id}
    message_id={self.message_id}
    date={self.date}
    chat_title={self.chat_title}
    message={self.message}
    {self.json_data}
)>"""
