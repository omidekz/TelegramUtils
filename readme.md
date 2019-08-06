# Telegram Utils
- # Usage
   - `git clone https://github.com/omidekz/TelegramUtils.git`
   -  ```python
      from TelegramUtils import Utils
      def start(update: Update, context: Call...Context):
         utils = Utils(update)
         chat_id = utils.chat_id()
         text = utils.text() # i think he/she sent start command"
         if utils.is_audio():
            pass
         else:
            context.bot.sendMessage(chat_id, "Hi {}\nwelcome😀".format(utils.first_name()))
      ```
* # method
    * `first_name()` -> `str`
    * `last_name()` -> `str`
    * `names()` -> `Tuple[str, str]` (first_name, last_name)
    * `chat_id()` -> `str`chat_id the owner of update
    * `username()` -> `str` Note: can be None
    * `message_id()` -> `str`
    * `text()` -> `str`
    * `is_audio()` -> `bool`
    * `audio()` -> `telegram.Audio`[Or raise an NoAudio Exception]
    * `audio_artist()` -> `str`
    * `audio_title()` -> `str`
    * `audio_thumb()` -> `telegram.PhotoSize`
    * `audio_file()` -> `telegram.File`
    * `audio_download(path=None)` -> `None`
    * `audio_size()` -> :) don't know
    <br>`@staticmethod`
    * `mention(text, chat_id)` -> `str`
    * `mention_this(text)` -> `str`
