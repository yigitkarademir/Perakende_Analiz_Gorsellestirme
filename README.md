📊 Perakende Satış Veri Analizi ve İnteraktif Dashboard
Bu çalışma, Kaggle üzerinden aldığım "Retail Transaction Dataset" verilerini Python (Pandas) ile işleyip temizledikten sonra Power BI ile görselleştirdiğim bir projedir. Amacım, bir işletmenin satışlarını zaman, ürün türü ve konuma göre inceleyerek veriden anlamlı sonuçlar çıkarmaktı.

🛠️ Neler Yaptım?
1. Python ile Veri Hazırlığı (ETL)
analiz.py dosyasında ham veri seti üzerinde şu işlemleri gerçekleştirdim:

Veri Tipi Düzenlemeleri: Tarih verilerini bilgisayarın anlayacağı datetime formatına çevirdim ve fiyat gibi ondalıklı sayıları daha düzenli görünmesi için yuvarladım.

Yeni Sütunlar Oluşturma: Satış tarihinden yola çıkarak; Ay, Gün İsmi ve Saat gibi yeni bilgiler türettim. Bu sayede "Hangi saatte daha çok satış yapıyoruz?" gibi sorulara cevap bulabildim.

Gruplama ve Hesaplama: Günlük toplam kazançları ve ödeme yöntemlerine göre ciro dağılımlarını Pandas kütüphanesi ile hesapladım.

2. Power BI ile Görselleştirme
Temizlediğim verileri Power BI'a aktararak şu interaktif görselleri hazırladım:

Özet Kartlar: Toplam ciro, satılan ürün miktarı ve müşteri sayısı gibi ana rakamları en üste yerleştirdim.

Zaman Trendleri: Satışların saatlik değişimini bir alan grafiği, haftalık dağılımını ise sütun grafiği ile gösterdim.

Isı Haritası: Satışların dünyadaki yoğunluğunu görmek için harita üzerinden "sıcaklık" analizi ekledim.

Filtreler (Slicers): Raporu inceleyen kişinin istediği ayı veya günü seçerek rakamları anlık değiştirebilmesini sağladım.

📈 Neler Fark Ettim?
En Çok Satan Kategori: Verilere baktığımda "Books" (Kitap) kategorisinin ciroda diğerlerine göre önde olduğunu gördüm.

Yoğun Saatler: Satışların gün içinde nasıl dalgalandığını ve hangi saatlerde "zirve" yaptığını belirleyerek dükkanın en hareketli zamanlarını ortaya çıkardım.

Bölgesel Dağılım: Isı haritası sayesinde satışların hangi bölgelerde toplandığını görsel olarak kanıtladım.

💻 Kullandığım Araçlar
Python: Pandas, Numpy

Power BI: Power Query ve Dashboard Tasarımı


Veri Kaynağı: [Kaggle Retail Transaction Dataset](https://www.kaggle.com/datasets/fahadrehman07/retail-transaction-dataset)
