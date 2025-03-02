📝 Stack Overflow Sentiment Analiz Sistemi
Bu Python programı, Stack Overflow'dan veri çekip, bu verileri kullanarak sentiment analizi yapar. Kullanıcıların yazdığı soru başlıklarını analiz ederek, her bir başlık için "Pozitif", "Negatif" veya "Nötr" sonuçlar döndürür.

🎯 Proje Amacı
Bu proje, Stack Overflow'daki içerikleri analiz ederek, kullanıcıların yazdığı soru başlıklarını duygu durumlarına göre sınıflandırmak ve sonuçları görselleştirmektir.

🛠️ Kullanılan Teknolojiler
Python Programlama Dili
Pandas Kütüphanesi
Matplotlib Kütüphanesi
Requests Kütüphanesi
RegEx (Düzenli İfadeler)
Stack Overflow API
⚙️ Çalışma Prensibi
Program, Stack Overflow API'si kullanarak belirli bir etiketle ilişkilendirilmiş soruları çeker. Çekilen başlıklar, kelime listeleri kullanılarak analiz edilir ve başlıklar için sentiment analizi yapılır. Sonuçlar, bar grafiği ve pasta grafiği ile görselleştirilir.

📋 Temel Özellikler
Stack Overflow API'den veri çekme
Soru başlıklarına sentiment analizi uygulama
Sentiment sonuçlarını görselleştirme (Bar ve Pasta Grafiği)
Genişletilmiş pozitif ve negatif kelime grupları kullanma
Otomatik hata yönetimi
🖥️ Örnek Çıktı
markdown
Kopyala
Düzenle
'python' etiketi ile Stack Overflow'dan 1500 soru çekiliyor...

İlk 20 soru başlığı:
1. How to improve my python code?
2. Best practices for Python debugging
3. What is the best library for data analysis in Python?
...
...
İlk 20 soru başlığı için sentiment analizi sonuçları:
1. Pozitif
2. Negatif
3. Nötr
...
...

Sentiment analizi sonuçları (Grafik):
  - Bar Grafiği: Pozitif, Negatif ve Nötr kategorilerinin sayıları
  - Pasta Grafiği: Her kategorinin yüzdesel dağılımı
⚠️ Hata Yönetimi
API istek hatalarına karşı kontrol
Geçersiz veriler için kontrol
📜 Lisans
Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.

🚀 İyi çalışmalar! 😊
