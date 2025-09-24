# 🚀 Proje Başlangıç Rehberi

Bu proje, Python üzerinde çeşitli kütüphaneler kullanılarak geliştirilmiştir.  
Aşağıdaki adımları takip ederek gerekli bağımlılıkları yükleyebilir ve projeyi çalıştırabilirsiniz.
Proje temel kodları bana ait değildir. SimpleGui diye saçma paralı bir sistem kullanıyordu o kodları kaldırıp ktinkter kütüphanesini dahil ettim.

Kendi kullanım alanıma göre restore ettim. **Fish** Klasöründeki balıkları açması, **Drop** klasöründeki eşyaları atması gibi TAM AFK'da çalışacak bir demo elde ettim
Çarşamba günleri balık eventinde 01:00-13:00 arası (10:00'da bakım devreye giriyor) Bu süreçte haftada 1 kez olmak üzere 2 kez full balık tutup test ettim.
Bu alanda kazanç görürsem muhtemelen metin2 farmına başlayabilirim. Aşağıda gerekli bilgilendirmeleri yapacağım:

---

## 📦 Gerekli Kütüphaneler

Proje için aşağıdaki Python kütüphanelerini yüklemeniz gerekir:

- 🔢 **numpy** → Sayısal işlemler
- 🎥 **opencv-python** → Görüntü işleme
- ⌨️ **PyDirectInput** → Klavye & mouse otomasyonu
- 🖥️ **pywin32** → Windows API entegrasyonu
- 🔍 **pytesseract** → OCR (görselden metin okuma)
- 🪟 **tkinter** → GUI (arayüz geliştirme)
- 📦 **pyinstaller** → Uygulamanızı .exe’ye dönüştürmeye yarar eğer farklı pclerde exe olarak çalıştırmak isterseniz diye bunu belirtiyorum.

---

## ⚙️ Kurulum

📌 Kütüphaneleri yüklemek için terminalde şu komutu çalıştırın:

<p align="center"> <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="120"/> </p>

```bash
pip install numpy opencv-python PyDirectInput pywin32 pytesseract tk pyinstaller
```

### 1️⃣ Sanal Ortam (opsiyonel ama önerilir)
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

##  🏗️ Çalıştırma

Oyunu 800x600 olarak çözünürlüğünü düşürün. Benim ekranım 1920x1080 çözünürlükte olduğu için **Fish** ve **Drop** klasöründeki görselleri ona göre ayarlardım. Eğer o görselleri görüp işlem yapmıyorsa printscreen ile ss alıp sadece balık gözükecek şekilde croplayıp **siz fotoğrafları güncelleyin** tabi ki daha yüksek çözünürlüklü bir monitörünüz varsa bu işlem gerekebilir.
2 bilgisayarda test ettim görüntü güncellemem gerekmedi
-> Oyun çözünürlüğü **800x600**
-> Monitörümün çözünürlüğü **1920x1080**

```bash
python hack.py
```

### Eğer projeyi .exe olarak almak isterseniz
```bash
pyinstaller --onefile hack.py
```


##  📸 Örnek Arayüz

<p align="center"> <img src="https://github.com/user-attachments/assets/4d65e1c5-39cb-4b53-a325-ed4271480149" width="500"/> </p>
<p align="center"> <img src="https://github.com/user-attachments/assets/c666cf78-a9b3-45cf-9caf-905a553249e9" width="500"/> </p>
<p align="center"> <img src="https://github.com/user-attachments/assets/9cb5e873-889d-4c7c-abd2-9f8a119726e9" width="500"/> </p>


##  📌 Ekstra Bilgiler

OCR kullanmak için Tesseract OCR kurulum exe'sini dosyalara ekledim fakat projedeki tesseract okuması aktif değil. Üzerinde çalışıp tekrar aktif ederim eğer bu işe devam edersem.Projenin orijinalinde bu kod vardı fakat deaktifti.
📥 İndirme Linki (Windows)
OpenCV ve numpy ile görüntü işleme yapabilirsiniz.
PyDirectInput ile oyun içi otomasyon mümkündür.


# 👑 Farm Testleri

2 part olarak farm attığım video'yu telif yememesi için sansürleyip youtube platformun'a atıyorum. 

## Gece 02:32'de başlayıp Sabah 10:00'da biten balık botuyla topladığım kutu sayısı
<p align="center"> <img src="https://github.com/user-attachments/assets/6c884222-2fae-4e90-9cc5-9faaf92590c3" width="500"/> </p>


