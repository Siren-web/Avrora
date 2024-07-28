"""
python -m PyInstaller --onefile Avrora.py
"""

from core import Core

debug_mode = True

start_avrora = Core(user_config="./libs/config/user_config.yaml")

# connector
start_avrora.video_btn()


@start_avrora.bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global start_avrora

    start_avrora.voices(message.text, message.chat.id)


def main():
    while True:
        try:
            print("Bot is started...")

            global start_avrora

            start_avrora.info()
            start_avrora.bot.message_handler(content_types=['text'])
            start_avrora.bot.polling(none_stop=True, interval=0)

        except Exception as e:
            if debug_mode:
                print(e)
            print("Restarting...")
            pass


if __name__ == "__main__":
    main()
