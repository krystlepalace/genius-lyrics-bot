from uuid import uuid4
import main
from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent, ChosenInlineResult
import lyricsgenius as lg
from utils.genius_api import LyricsFinder
from config import CONFIG
from keyboards import song_url

router = Router()
finder = LyricsFinder()
genius = lg.Genius(CONFIG.genius_token.get_secret_value(), timeout=40)


@router.inline_query()
async def show_results(inline_query: InlineQuery):
    songs = genius.search_songs(inline_query.query, per_page=5, page=1)['hits']

    results = []
    for song in songs:
        results.append(InlineQueryResultArticle(
            id=str(song['result']["id"]),
            title=song['result']["title"],
            description=song["result"]["artist_names"],
            input_message_content=InputTextMessageContent(
                message_text="Loading text...",
            ),
            reply_markup=song_url.song_url_button(url="genius.com",
                                  title=song['result']["full_title"]).as_markup()
        ))
    await inline_query.answer(results, is_personal=True)


@router.chosen_inline_result()
async def load_lyrics(
        chosen_result: ChosenInlineResult,
):
    l = str(genius.lyrics(int(chosen_result.result_id)))
    message = await main.bot.edit_message_text(
        inline_message_id=chosen_result.inline_message_id,
        text=l
    )
