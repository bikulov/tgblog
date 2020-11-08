import os
import json
import requests
import logging
import datetime

import update

TELEGRAM_URL = "https://api.telegram.org/bot" 


class TelegramApi:
    def __init__(self, token=os.getenv("TELEGRAM_TOKEN")):
        self.token = token

    def get_updates(self):
        get_updates_url = f"{TELEGRAM_URL}{self.token}/getUpdates"
        for upd_dict in requests.get(get_updates_url).json().get("result"):
            yield self.__parse(upd_dict)

    def __parse(self, update_dict):
        logging.debug(update_dict)
        json_data = json.dumps(update_dict)

        for channel_post in ("channel_post", "edited_channel_post"):
            if channel_post in update_dict:
                data = update_dict[channel_post]

                chat_id = data.get("chat", {}).get("id")
                chat_title = data.get("chat", {}).get("title")
                message_id = data.get("message_id")
                date =  datetime.datetime.utcfromtimestamp(data.get("date", 0))
                message = data.get("text", "").replace("\n", "<br/>")

                return update.Update(
                    chat_id=chat_id,
                    message_id=message_id,
                    date=date,
                    chat_title=chat_title,
                    message=message,
                    json_data=json_data,
                )

        raise NotImplementedError(f"Parsing is not implemented yet for {update_dict}")
