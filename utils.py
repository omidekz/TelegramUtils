from telegram import *

from typing import Tuple

from TelegramUtils.CustomExceptions import *


class Utils:
    def __init__(self, update: Update):
        self.update = update

    def first_name(self) -> str:
        """
        Return the first name
        :return: str
        """
        return self.update.message.chat.first_name

    def last_name(self) -> str:
        """
        Return last name
        :return:
        """
        return self.update.message.chat.last_name

    def names(self) -> Tuple[str, str]:
        """
        Return a Tuple of str, len=2
        Tuple(first_name, last_name)
        :return: tuple(str, str)
        """
        return self.first_name(), self.last_name()

    def chat_id(self) -> str:
        """
        Return Chat_id of User or Gp or...
        :return: str
        """
        return str(self.update.message.chat.id)

    def username(self) -> str:
        """
        Return the user name if existent else return None
        :return: str
        """
        return str(self.update.message.chat.username)

    def message_id(self) -> str:
        """
        Return the message id
        :return: str
        """
        return self.update.message.message_id

    def text(self) -> str:
        """
        If update has a text message => Return the text
        :return: str
        """
        return self.update.message.text

    def is_audio(self) -> bool:
        return self.update.message.audio is not None

    def audio(self, raise_exception=True) -> Audio:
        if not self.is_audio() and raise_exception:
            raise NoAudio("This update has no Audio file")
        return self.update.message.audio

    def audio_artist(self) -> str:
        return self.audio().performer

    def audio_title(self) -> str:
        return self.audio().title

    def audio_thumb(self) -> PhotoSize:
        return self.audio().thumb

    def audio_file(self) -> File:
        return self.audio().get_file()

    def audio_download(self, path=None) -> None:
        self.audio_file().download(path)

    def audio_size(self):
        return self.audio_file().file_size


    @staticmethod
    def mention(markdown_message, user_id) -> str:
        """
        Return a mention by chat_id
        :param markdown_message:
        :param user_id:
        :return: str
        """
        return "[%s](tg://user?id=%s)" % (str(markdown_message), str(user_id))

    def mention_this(self, text) -> str:
        """
        Mention the owner of update
        :param text:
        :return: str
        """
        return self.mention(text, self.chat_id())
