from config import CONFIG
import lyricsgenius as lg

genius = lg.Genius(CONFIG.genius_token.get_secret_value())


async def search_song(name=""):
    song = genius.search_song(title=name)
    return song.lyrics
