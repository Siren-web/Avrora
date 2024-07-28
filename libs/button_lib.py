from telebot import types
import yaml


class ButtonLib:

    def __init__(self, sbot) -> None:
        self.sbot = sbot

        with open("./libs/config/user_config.yaml") as file_config:
            self.data_config = yaml.safe_load(file_config)

    def start_restart(self, message):
        final = "markup.add("

        for i in range(len(self.data_config["buttons"])):
            final += f"types.KeyboardButton(self.data_config['buttons'][{i}]), "
        final = final[:-2]
        final += ")"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        eval(final)
        self.sbot.send_message(message.chat.id,
                               text=self.data_config["start_message"].format(message.from_user),
                               reply_markup=markup)

    def starting(self):
        @self.sbot.message_handler(commands=['start'])
        def start(message: types.Message):
            self.start_restart(message)

        @self.sbot.message_handler(commands=['restart'])
        def restart(message):
            self.start_restart(message)

        @self.sbot.message_handler(commands=['help'])
        def help_info(message):
            pass
