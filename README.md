# Stack Overflow Sentiment Analizi

Bu proje, Stack Overflow API'sinden belirli bir etiket (tag) ile soru başlıklarını çekerek, bu başlıklar üzerinde sentiment analizi yapmaktadır. Analiz sonucunda başlıklar "Pozitif", "Negatif" veya "Nötr" olarak sınıflandırılır ve sonuçlar grafiklerle görselleştirilir.

## 📚 Proje İçeriği
- **Stack Overflow API kullanımı**: Belirli bir etiketle 1500 adet soru başlığı çekme
- **Sentiment analizi**: Pozitif ve negatif kelimelere dayalı basit analiz
- **Veri görselleştirme**: Bar ve pasta grafikleri ile analiz sonucu sunma

## 🛠 Kurulum
Projeyi çalıştırmak için aşağıdaki bağımlılıkları yüklemeniz gerekir:

```bash
pip install requests pandas matplotlib
```

## 📝 Kullanım
Python dosyasını çalıştırmadan önce analiz etmek istediğiniz Stack Overflow etiketini (tag) değiştirebilirsiniz. Varsayılan olarak **"python"** etiketi kullanılmıştır.

```python
# Analiz edilecek Stack Overflow etiketi
tag = "python"
```

Kodunuzu aşağıdaki komut ile çalıştırabilirsiniz:

```bash
python sentiment_analysis.py
```

## 📊 Çıktılar
Kod çalıştırıldıktan sonra:
1. Çekilen ilk 20 soru başlığı ekrana yazdırılır.
2. Başlıklara sentiment analizi uygulanır ve her biri **Pozitif**, **Negatif** veya **Nötr** olarak etiketlenir.
3. Analiz sonuçları bar ve pasta grafikleri ile görselleştirilir.

## 🌐 API Kullanımı
Kod, Stack Overflow API'sinden veri çekmek için aşağıdaki endpoint'i kullanır:
```
https://api.stackexchange.com/2.3/questions
```
Parametreler:
- `order=desc` (Son eklenenlerden başlayarak sıralama)
- `sort=creation` (Oluşturulma tarihine göre sıralama)
- `tagged=python` (İlgili etiket)
- `site=stackoverflow` (Stack Overflow verileri çekme)
- `pagesize=100` (Her istekte 100 veri çekme)

## 🌟 Örnek Sonuç
| Başlık | Sentiment |
|--------|----------|
| How to efficiently sort a dictionary in Python? | Pozitif |
| Python program crashes on startup | Negatif |
| Best way to iterate over a large dataset in pandas? | Pozitif |
| Unable to install NumPy on Windows | Negatif |

## ✅ Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Serbestçe kullanabilir, dağıtabilir ve geliştirebilirsiniz.

