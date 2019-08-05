# Telegram Utils
* # method
    * `first_name()` -> `str`
    * `last_name()` -> `str`
    * `names()` -> `Tuple[str, str]`
    * `chat_id()` -> `str`
    * `username()` -> `str`
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
