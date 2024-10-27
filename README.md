# Trendyol Ürün Yorumları Çekme Aracı

Bu proje, Python ve Selenium kullanarak Trendyol üzerindeki ürünlere ait kullanıcı yorumlarını otomatik olarak çekmeyi amaçlamaktadır. Kod, ürünle ilgili tüm kullanıcı yorumlarını, kullanıcı adlarını, yorum tarihlerini ve yıldız değerlendirmelerini kolayca toplar ve CSV dosyasına kaydeder.

## Özellikler
- **Yorum Çekme**: Belirli bir Trendyol ürününe ait tüm yorumlar çekilir.
- **Kullanıcı Bilgileri**: Yorum yapan kullanıcı adları ve yorum tarihleri alınır.
- **Yıldız Değerlendirmeleri**: Her yoruma ait yıldız sayısı belirlenir ve kaydedilir.

## Nasıl Çalışır?
1. **URL Girin**: `url` değişkenine yorumlarını çekmek istediğiniz Trendyol ürün sayfasının linkini yapıştırın.
2. **Çalıştırın**: Script’i çalıştırarak veri çekme işlemini başlatın.
3. **Çıktı Dosyası**: Veriler `product_comments_with_ratings.csv` dosyasında saklanır.

## Gereksinimler
- Python 3
- Selenium
- ChromeDriver (versiyonu kullandığınız Chrome sürümüyle uyumlu olmalıdır)

## Kullanım Alanları
Bu araç, e-ticaret platformlarında müşteri geri bildirimlerini incelemek ve ürün hakkında kullanıcı görüşlerini değerlendirmek isteyenler için uygundur.

---

# Trendyol Product Review Scraper

This project aims to automatically scrape user reviews for products on Trendyol using Python and Selenium. The code collects all user reviews related to the product, along with usernames, review dates, and star ratings, and saves them in a CSV file for easy access.

## Features
- **Review Collection**: Retrieves all reviews for a specific product on Trendyol.
- **User Information**: Collects usernames and review dates.
- **Star Ratings**: Extracts and records the star rating for each review.

## How It Works
1. **Insert URL**: Paste the link of the Trendyol product review page into the `url` variable.
2. **Run the Script**: Execute the script to start the data collection process.
3. **Output File**: Data is saved in a CSV file named `product_comments_with_ratings.csv`.

## Requirements
- Python 3
- Selenium
- ChromeDriver (must match your installed Chrome version)

## Use Cases
This tool is suitable for analyzing customer feedback on e-commerce platforms and evaluating user opinions about products.
