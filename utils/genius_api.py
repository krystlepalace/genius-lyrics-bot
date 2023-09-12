from config import CONFIG
import lyricsgenius as lg


class LyricsFinder:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(LyricsFinder, cls).__new__(cls)
            cls.__instance.init()

        return cls.__instance

    def init(self):
        self.genius = lg.Genius(CONFIG.genius_token.get_secret_value())

    async def search_song(self, name="", page=1):
        result = self.genius.search_songs(name, per_page=5, page=page)
        return result['hits']

    # current song: result['hits'][0<N<=5]["result"]
    # ["full_title"] or ["header_image_thumbnail_url"] or just ["id"]

    async def get_lyrics(self, song_id=None):
        return str(self.genius.lyrics(song_id))
