import jinja2
import logging
import json
import datetime

import database


class Website:

    def __init__(self):
        self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
        self.db = database.Database()


    def insert(self, updates):
        for upd in updates:
            logging.debug(f"Update will be inserted: {upd}")
            self.db.insert([upd])

    def render(self, chat_id, author, title):
        posts = self.db.get_all(chat_id)
        template = self.jinja_env.get_template("index.j2")

        return template.render(title=title, author=author, posts=posts)
