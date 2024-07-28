from random import choice
import telebot
import yaml
from libs.button_lib import ButtonLib


# module connections

def restart():
    int("Restart")


class Core:

    def __init__(self, user_config) -> None:
        self.user_config = user_config
        self.data_config = {}

        with open(self.user_config) as file_config:
            self.data_config = yaml.safe_load(file_config)

        self.current_version = self.data_config["version"]
        self.__token = ""
        with open(self.data_config["token_path"], 'r') as file:
            self.__token = file.read().replace('\n', '')
        self.bot = telebot.TeleBot(self.__token)

        # connetctions vars:
        self.tl = ButtonLib(self.bot)

    def voices(self, get_text, send_id_text):

        # core commands
        if get_text in self.data_config["hi"]:
            self.bot.send_message(send_id_text, choice(self.data_config["hi_bot"]))
        elif get_text.lower() == "avrora, restart":
            restart()

        # conections commands
        # for i in range(len(self.data_config["buttons"])):
        if get_text.lower() == self.data_config["buttons"][0].lower():
            # for x in os.listdir(f"./src/videos/btn{i + 1}"):
            #     print(x)
            #     self.bot.send_document(send_id_text,
            #                            open(f"./src/videos/btn{i + 1}/{x}", 'rb'))
            self.bot.send_message(send_id_text, choice(self.data_config["group"]))
        else:
            self.bot.send_message(send_id_text, "ERROR")

    # function connections
    def video_btn(self):
        self.tl.starting()

    def info(self):
        print(self.current_version)
