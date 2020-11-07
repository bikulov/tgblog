import requests
import logging
import argparse
import os

import website
import telegram_api


def parse_arguments():
    parser = argparse.ArgumentParser(
        "Generate HTML page from Telegram channel",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.set_defaults(func=None)
    parser.add_argument(
        "--verbose",
        help="Verbose logging",
        action="store_true"
    )

    parser.add_argument(
        "--chat-id",
        help="chat_id (ask @MyChatInfoBot bot)",
        type=int
    )

    parser.add_argument(
        "--author",
        help="Posts author"
    )

    parser.add_argument(
        "--title",
        help="Fancy html title"
    )
   
    return parser.parse_args()

def main(args):

    tg_api = telegram_api.TelegramApi()
    
    ws = website.Website()
    ws.insert(tg_api.get_updates())

    print(ws.render(args.chat_id, args.author, args.title))


if __name__ == "__main__":
    args = parse_arguments()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(filename)s:%(lineno)d] %(levelname)-8s [%(asctime)s]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    main(args)