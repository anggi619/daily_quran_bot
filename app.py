from quran import Quran
import time
from twitter import Twitter
from media import Media

md = Media()
tw = Twitter()
quran = Quran()
def start():
    while True:
        try:
            md.download_image()
            surah_and_ayah = quran.get_random_ayat()
            print("Media has been downloaded!")
            print(surah_and_ayah["surah_name"])
            md.process_image(surah_and_ayah["ayah"], surah_and_ayah["surah_name"], surah_and_ayah["ayah_index"])
            tw.post_tweet_with_media()
            print("Sleeping...")
            time.sleep(14400)
        except Exception as ex:
            print("Exception!")
            print(ex)
            time.sleep(90)
            pass



if __name__ == "__main__":
    start()