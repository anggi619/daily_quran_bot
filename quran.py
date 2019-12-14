import requests
import _json
import random

class Quran:
    def get_random_ayat(self):
        surah_index = random.randrange(1, 114)
        surah_req = requests.get("http://api.alquran.cloud/v1/surah/"+str(surah_index)+"/en.asad")
        surah_data = surah_req.json()
        num_of_ayah = surah_data["data"]["numberOfAyahs"]
        choosed_ayah = random.randrange(1, num_of_ayah)
        ayahs = []
        for item in surah_data["data"]["ayahs"]:
            surah_detail = {"index": None, "text": None}
            surah_detail['index'] = item['numberInSurah']
            surah_detail['text'] = item['text']
            ayahs.append(surah_detail)

        print("Loading surah "+ surah_data["data"]["englishName"] + " ayah number " + str(choosed_ayah))
        print(ayahs[choosed_ayah]["text"])
        surah_and_ayah = {"surah_name":surah_data["data"]["englishName"], "ayah":ayahs[choosed_ayah]["text"], "ayah_index":str(choosed_ayah)}
        return  surah_and_ayah

