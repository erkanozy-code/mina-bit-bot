# Bölüm 8: Şemsiye kodu — son 100 günün ortalaması: bugün güneşli mi, yağmurlu mu?
# Kurulum gerekmez: sadece Python (python.org). Ek paket yok.
import json
import urllib.request

ADRES = "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=101"

def kapanislari_oku():
    cevap = urllib.request.urlopen(ADRES).read()  # internete sor
    mumlar = json.loads(cevap)  # cevabı çöz: 101 günlük mum
    mumlar = mumlar[:-1]  # bugünün mumu bitmedi, onu at
    kapanislar = []  # boş bir liste
    for mum in mumlar:
        kapanislar.append(float(mum[4]))  # 5. bilgi = kapanış fiyatı
    return kapanislar

kapanislar = kapanislari_oku()
ortalama = sum(kapanislar) / len(kapanislar)  # topla, gün sayısına böl
dun = kapanislar[-1]  # listenin sonuncusu = dünkü kapanış

print("Gün sayısı:", len(kapanislar))
print("100 günlük ortalama:", round(ortalama, 2), "dolar")
print("Dünkü kapanış:", round(dun, 2), "dolar")

if dun > ortalama:
    print("Hava GÜNEŞLİ: şemsiye kapalı, Bitcoin'de kal.")
else:
    print("Hava YAĞMURLU: şemsiye açık, kasaya geç.")
