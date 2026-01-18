import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Retail_Transaction_Dataset.csv")
pd.set_option('display.max_columns', None)

print(df.head())
print(df.info())
print(df.describe())

#Veri tipi donusumleri
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
df['CustomerID'] = df['CustomerID'].astype(str)

# Ondalıklı (float) sayıları yuvarladım
df['Price'] = df['Price'].round(2)
df['TotalAmount'] = df['TotalAmount'].round(2)
df['DiscountApplied(%)'] = df['DiscountApplied(%)'].round(2)



print(df.info())
print(df[['Price', 'DiscountApplied(%)', 'TotalAmount']].head(30))
print(df[['Price', 'DiscountApplied(%)', 'TotalAmount']].describe())

#------------------------------------------------------------
# Yeni sutun olusturma
# 1. Ay ismini ekleyelim yeni bir sutun (Ocak, Şubat...)
df['Month'] = df['TransactionDate'].dt.month_name()

# 2. Gün ismini ekleyelim  yeni bir sutun(Pazartesi, Salı...)
df['Day_Name'] = df['TransactionDate'].dt.day_name()

# 3. Saat bilgisini ekleyelim yeni bir sutun (0-23 arası sayı)
df['Hour'] = df['TransactionDate'].dt.hour

print(df[['TransactionDate', 'Month', 'Day_Name', 'Hour']].head())


# Gruplama
gunluk_satis = df.groupby('Day_Name')['TotalAmount'].sum().sort_values(ascending=False)
print("--- Günlük Toplam Ciro ---")
print(gunluk_satis)

saatlik_islem = df.groupby('Hour')['CustomerID'].count()
print("\n--- Saatlere Göre İşlem Sayısı ---")
print(saatlik_islem)

odeme_analizi = df.groupby('PaymentMethod')['TotalAmount'].sum()
print("\n--- Ödeme Yöntemine Göre Toplam Ciro ---")
print(odeme_analizi)

# Günlere göre grupla ve toplam tutarı topla
gunluk_kazanc = df.groupby('Day_Name')['TotalAmount'].sum().sort_values(ascending=False)
print("--- Günlük Toplam Kazanç ---")
print(gunluk_kazanc)


#-----------------------------------------------------------------
# Özetler

# Tüm veri setinin toplam cirosu
toplam_ciro = df['TotalAmount'].sum()

# Toplam satılan ürün miktarı
toplam_adet = df['Quantity'].sum()

# Toplam benzersiz müşteri sayısı
toplam_musteri = df['CustomerID'].nunique()

print(f"--- GENEL PERFORMANS ÖZETİ ---")
print(f"Toplam Ciro: {toplam_ciro:,.2f} TL")
print(f"Toplam Satılan Ürün: {toplam_adet:,} adet")
print(f"Toplam Benzersiz Müşteri: {toplam_musteri:,}")
print(f"Sipariş Başına Ortalama Tutar: {(toplam_ciro / len(df)):.2f} TL")

df.to_csv("Satis_Analizi.csv", index=False)








