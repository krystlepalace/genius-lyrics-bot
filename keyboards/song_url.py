from aiogram.utils.keyboard import InlineKeyboardBuilder


def song_url_button(url=None, title=None):
    builder = InlineKeyboardBuilder()
    builder.button(text=title,
                   url=url)

    return builder
