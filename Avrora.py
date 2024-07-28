"""
python -m PyInstaller --onefile athena.py
"""

from core import Core

debug_mode = True

start_athena = Core(user_config="./libs/config/user_config.yaml")

# connector
start_athena.video_btn()


@start_athena.bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global start_athena

    start_athena.voices(message.text, message.chat.id)


def main():
    while True:
        try:
            print("Bot is started...")

            global start_athena

            start_athena.info()
            start_athena.bot.message_handler(content_types=['text'])
            start_athena.bot.polling(none_stop=True, interval=0)

        except Exception as e:
            if debug_mode:
                print(e)
            print("Restarting...")
            pass


if __name__ == "__main__":
    main()
