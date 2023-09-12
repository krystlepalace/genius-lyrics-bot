from uuid import uuid4

from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
import lyricsgenius as lg
from utils.genius_api import LyricsFinder
from config import CONFIG

router = Router()
finder = LyricsFinder()
genius = lg.Genius(CONFIG.genius_token.get_secret_value(), timeout=40)


@router.inline_query()
async def show_results(inline_query: InlineQuery):
    songs = genius.search_songs(inline_query.query, per_page=5, page=1)['hits']

    results = []
    for song in songs:
        results.append(InlineQueryResultArticle(
            id=str(uuid4()),
            title=song['result']["title"],
            description=song["result"]["artist_names"],
            input_message_content=InputTextMessageContent(
                message_text=str(genius.lyrics(song["result"]["id"]))
            )
        ))
    await inline_query.answer(results, is_personal=True)
