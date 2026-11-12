# Bölüm 7: Botun gözleri — Bitcoin fiyatını internetten okur
# Kurulum gerekmez: sadece Python (python.org). Ek paket yok.
import json
import time
import urllib.request

ADRES = "https://data-api.binance.vision/api/v3/ticker/price?symbol=BTCUSDT"

def fiyat_oku():
    cevap = urllib.request.urlopen(ADRES).read()  # internete sor
    veri = json.loads(cevap)  # cevabı çöz
    return float(veri["price"])  # fiyatı al

while True:
    fiyat = fiyat_oku()
    print("Bitcoin şu an:", round(fiyat, 2), "dolar")
    time.sleep(10)  # 10 sn bekle
