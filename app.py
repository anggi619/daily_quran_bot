from quran import Quran
import time
from twitter import Twitter
from media import Media

# Changed english quran to indonesian quran

md = Media()
tw = Twitter()
quran = Quran()
surahs = quran.fetch_surah_data()

def start():
    while True:
        try:
            md.download_image()
            data = quran.get_ayah()
            surah_name = surahs[data["index_surah"]-1]["name"]
            print("Surah name is "+str(surah_name))
            ayah_text = data["ayah"]["text"]
            ayah_index = data["ayah"]["index"]
            print("Ayah ke "+str(ayah_index)+ " and isi "+ str(ayah_text))
            md.process_image(ayah_text, surah_name, ayah_index)
            tw.post_tweet_with_media()
            time.sleep(14400)
        except Exception as ex:
            print("Exception!")
            print(ex)
            time.sleep(90)
            pass


if __name__ == "__main__":
    start()