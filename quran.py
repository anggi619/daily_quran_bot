import requests
import random

class Quran:
    def fetch_surah_data(self):
        url = requests.get("https://al-quran-8d642.firebaseio.com/data.json")
        datas = url.json()
        surahs = []
        for item in datas:
            surah_detail = {'index': item['nomor'], 'name': item['nama']}
            surahs.append(surah_detail)
        return surahs

    def get_ayah(self):
        choosed_surah = random.randrange(1,114)
        print("Choosed surah "+ str(choosed_surah))
        url = requests.get("https://al-quran-8d642.firebaseio.com/surat/"+str(choosed_surah)+".json")
        datas = url.json()
        ayahs = []
        for item in datas:
            ayah_detail = {'index':item['nomor'], 'text':item['id']}
            ayahs.append(ayah_detail)

        choosed_ayah = random.randrange(len(ayahs))
        print("Choosed ayah "+str(choosed_ayah))
        data = {'index_surah':choosed_surah, 'ayah': ayahs[choosed_ayah]}
        return data