import requests
import pandas as pd
import re
import matplotlib.pyplot as plt

# 📌 Stack Overflow API'den veri çekme
def stackoverflow_veri_cek(tag, adet=1500):
    BASE_URL = "https://api.stackexchange.com/2.3/questions"
    params = {
        "order": "desc",
        "sort": "creation",
        "tagged": tag,
        "site": "stackoverflow",
        "pagesize": 100
    }

    sorular = []
    while len(sorular) < adet:
        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            print("API isteği başarısız oldu!")
            break
        data = response.json()
        items = data.get("items", [])
        sorular.extend(items)
        if not data.get("has_more", False):
            break
        params["page"] = params.get("page", 1) + 1

    return pd.DataFrame([{"title": s["title"]} for s in sorular[:adet]])

# 📌 Genişletilmiş Sentiment Kelime Listeleri
pozitif_kelimeler = [
    "great", "good", "excellent", "nice", "awesome", "love", "best", "fast",
    "successful", "helpful", "amazing", "perfect", "clear", "smooth", "efficient",
    "brilliant", "easy", "useful", "correct", "impressive", "reliable", "fun",
    "cool", "fantastic", "wonderful", "positive", "powerful", "flexible", "stable",
    "seamless", "intuitive", "smart", "well", "super", "amazing", "greatest",
    "improvement", "strong", "like", "appreciate", "genius", "safe", "trustworthy",
    "speedy", "robust", "simplified", "user-friendly", "bright", "pleased", "faster",
    "satisfying", "hassle-free", "bug-free", "glad", "love it", "enjoyable", "lightweight"
]

negatif_kelimeler = [
    "bad", "worst", "error", "fail", "problem", "issue", "bug", "slow", "complicated",
    "difficult", "confusing", "frustrating", "annoying", "broken", "crash", "unstable",
    "waste", "hard", "incorrect", "unresponsive", "poor", "conflict", "glitch", "terrible",
    "horrible", "disappointed", "messy", "outdated", "lag", "inconsistent", "missing",
    "awful", "failure", "not working", "disaster", "trash", "useless", "weak", "downgrade",
    "unreliable", "nightmare", "dumb", "slowdown", "pathetic", "crappy", "trouble",
    "clunky", "buggy", "overcomplicated", "tedious", "painful", "nonsense", "nonfunctional"
]

# 📌 Kelime Gruplarını Eklemek için Yeni Liste
pozitif_kelime_gruplari = [
    "don't like", "not good", "not working", "could be better", "doesn't help"
]

negatif_kelime_gruplari = [
    "not good", "not working", "doesn't work", "problem with", "not helpful"
]

# 📌 Sentiment hesaplama fonksiyonu
def sentiment_hesapla(title):
    title = title.lower()  # Küçük harfe çevir
    title = re.sub(r'[^\w\s]', '', title)  # Noktalama işaretlerini temizle

    # Basit kelime sayımı
    pozitif_sayac = sum(title.count(kelime) for kelime in pozitif_kelimeler)
    negatif_sayac = sum(title.count(kelime) for kelime in negatif_kelimeler)

    # Kelime grubu kontrolü
    for grup in pozitif_kelime_gruplari:
        if grup in title:
            pozitif_sayac += 1

    for grup in negatif_kelime_gruplari:
        if grup in title:
            negatif_sayac += 1

    # Eğer pozitif veya negatif varsa ona göre sınıflandır
    if pozitif_sayac > negatif_sayac:
        return "Pozitif"
    elif negatif_sayac > pozitif_sayac:
        return "Negatif"
    else:
        return "Nötr"  # Eğer hiçbiri değilse nötr olarak kabul edilir

# 📌 Stack Overflow'dan veri çekme
tag = "python"
print(f"'{tag}' etiketi ile Stack Overflow'dan 1500 soru çekiliyor...")
df_sorular = stackoverflow_veri_cek(tag)

# 📌 İlk 20 sonucu yazdırma
print("\nİlk 20 soru başlığı:")
print(df_sorular["title"].head(20))

# 📌 Sentiment analizi uygulama
df_sorular["sentiment"] = df_sorular["title"].apply(sentiment_hesapla)

# 📌 Analiz sonuçlarını görselleştirme
plt.figure(figsize=(12, 5))

# 📊 Bar Grafiği
plt.subplot(1, 2, 1)
df_sorular["sentiment"].value_counts().plot(kind="bar", color=["green", "red", "gray"])
plt.xlabel("Sentiment Türü")
plt.ylabel("Sayı")
plt.title(f"'{tag}' Etiketi için Sentiment Analizi (Bar Grafiği)")
plt.xticks(rotation=0)

# 🥧 Pasta Grafiği
plt.subplot(1, 2, 2)
df_sorular["sentiment"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["green", "red", "gray"])
plt.ylabel("")  # Y ekseni başlığını kaldır

plt.suptitle(f"'{tag}' Etiketi için Sentiment Analizi (Bar & Pasta Grafiği)")
plt.show()

# 📌 Sonuçları ekrana yazdır
print("\nSentiment analizi sonuçları (İlk 20 soru):")
print(df_sorular[["title", "sentiment"]].head(20))  # İlk 20 sonucu gör
