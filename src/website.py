import jinja2
import logging
import json
import datetime
import os
import pathlib

import database


class Website:

    def __init__(self, db_file=":memory:"):
        loader = jinja2.FileSystemLoader(os.path.join(pathlib.Path(__file__).parent.absolute(), "templates"))
        self.jinja_env = jinja2.Environment(loader=loader)
        self.db = database.Database(db_file)

    def insert(self, updates):
        for upd in updates:
            logging.debug(f"Update will be inserted: {upd}")
            self.db.insert([upd])

    def render(self, chat_id, author, title):
        posts = self.db.get_all(chat_id)
        posts_count = len(posts)
        logging.info(f"Posts num {posts_count}")

        template = self.jinja_env.get_template("index.j2")

        return template.render(title=title, author=author, posts=posts)
