from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Chrome seçeneklerini ayarla (bildirimleri devre dışı bırak)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# ChromeDriver ile tarayıcıyı başlat
service = Service(r"ChromeDriver Pcnizdeki Yolu Giriniz")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Tarayıcıyı tam ekran yap
driver.maximize_window()

# Hedef URL'yi aç
url = "https://www.trendyol.com/oxvin/walker-baggy-bol-paca-2-iplik-orta-kalinlikta-uzun-esofman-alti-orijinal-kalip-p-855410436/yorumlar?boutiqueId=61&merchantId=833224"
driver.get(url)

# Çerezleri kabul etme butonuna tıkla
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
).click()

# Tüm yorumları yüklemek için sayfayı aşağı kaydır
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Tüm ana yorum öğelerini bul
comment_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div')
total_comments = len(comment_elements)

# Her ana XPath öğesinin içine girerek kullanıcı adı, yorum, tarih ve yıldız bilgilerini çek
data = []
for i in range(1, total_comments + 1):
    kullanıcı_id = i
    try:
        # Kullanıcı adı çekme
        username_xpath = f'/html/body/div[1]/div[4]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[1]/div[2]/div[1]'
        username = driver.find_element(By.XPATH, username_xpath).text
    except:
        username = "N/A"  # Kullanıcı adı yoksa "N/A" ekle

    try:
        # Yorum metnini çekme
        comment_xpath = f'/html/body/div[1]/div[4]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[2]/p'
        comment = driver.find_element(By.XPATH, comment_xpath).text
    except:
        comment = "N/A"  # Yorum yoksa "N/A" ekle

    try:
        # Tarih bilgisini çekme
        date_xpath = f'/html/body/div[1]/div[4]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[1]/div[2]/div[2]'
        date = driver.find_element(By.XPATH, date_xpath).text
    except:
        date = "N/A"  # Tarih yoksa "N/A" ekle

    # Yıldız sayısını hesaplama
    star_xpath_base = f'/html/body/div[1]/div[4]/div/div/div/div/div[3]/div/div/div[3]/div[2]/div[{i}]/div[1]/div[1]/div'
    try:
        # Tüm "full" yıldız elemanlarını bul
        full_stars = driver.find_elements(By.XPATH, f"{star_xpath_base}/div[@class='star-w']/div[@class='full'][@style='width: 100%; max-width: 100%;']")
        star_count = len(full_stars)  # Yıldız sayısını dolu olanlarla eşleştir
    except:
        star_count = 0  # Yıldız bilgisi yoksa 0 yıldız ekle

    data.append({
        "Kullanıcı_id": kullanıcı_id,
        "Kullanıcı Adı": username,
        "Yorum": comment,
        "Tarih": date,
        "Yıldız Sayısı": star_count
    })

# Veriyi UTF-8 kodlamasıyla CSV'ye kaydet
df = pd.DataFrame(data)
df.to_csv('product_comments_with_ratings.csv', index=False, encoding='utf-8-sig')
print("Kullanıcı_id, Kullanıcı Adı, Yorum, Tarih ve Yıldız Sayısı bilgileri CSV dosyasına kaydedildi.")

# Tarayıcıyı kapat
driver.quit()
