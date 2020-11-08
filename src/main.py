import requests
import logging
import argparse
import time
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
        action="store_true",
    )

    parser.add_argument(
        "--chat-id",
        help="chat_id (ask @MyChatInfoBot bot)",
        type=int,
        default=os.getenv("CHAT_ID", None),
    )

    parser.add_argument(
        "--author",
        help="Posts author",
        default=os.getenv("AUTHOR", None),
    )

    parser.add_argument(
        "--title",
        help="Fancy html title",
        default=os.getenv("TITLE", None),
    )

    parser.add_argument(
        "--loop",
        help="Seconds to sleep in the endless loop (no loop is 0)",
        type=int,
        default=os.getenv("SLEEP", None),
    )

    parser.add_argument(
        "--output-html",
        help="Output html file",
        default=os.getenv("OUTPUT_HTML", "/usr/share/nginx/html/index.html"),
    )

    parser.add_argument(
        "--db-file",
        help="sqlite database file",
        default=os.getenv("DB_FILE", "/data/db.sqlite"),
    )
   
    return parser.parse_args()


def main(args):
    while True:
        tg_api = telegram_api.TelegramApi()
        updates = tg_api.get_updates()

        if updates:
            ws = website.Website(args.db_file)
            ws.insert(updates)

            with open(args.output_html, "w") as fout:
                print(ws.render(args.chat_id, args.author, args.title), file=fout)

        if args.loop:
            logging.info(f"Sleeping {args.loop} seconds before next iteration")
            time.sleep(args.loop)
        else:
            break


if __name__ == "__main__":
    args = parse_arguments()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="[%(filename)s:%(lineno)d] %(levelname)-8s [%(asctime)s]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    main(args)