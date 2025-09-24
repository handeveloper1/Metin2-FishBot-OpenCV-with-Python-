<img src="https://github.com/user-attachments/assets/f08818e9-f215-4d43-9cc9-e37ef5264e71" width="150"/>


# 🚀 Proje Başlangıç Rehberi

Bu proje, Python üzerinde çeşitli kütüphaneler kullanılarak geliştirilmiştir.  
Aşağıdaki adımları takip ederek gerekli bağımlılıkları yükleyebilir ve projeyi çalıştırabilirsiniz.
Proje temel kodları bana ait değildir. SimpleGui diye saçma paralı bir sistem kullanıyordu o kodları kaldırıp ktinkter kütüphanesini dahil ettim.

Kendi kullanım alanıma göre restore ettim. **Fish** Klasöründeki balıkları açması, **Drop** klasöründeki eşyaları atması gibi TAM AFK'da çalışacak bir demo elde ettim
Çarşamba günleri balık eventinde 01:00-13:00 arası (10:00'da bakım devreye giriyor) Bu süreçte haftada 1 kez olmak üzere 3 kez full balık tutup test ettim.
Yani kullanım sürem: çarşamba günleri 9saat aralıksız balık tuttu cumartesileri de oto puzzle ile oynattım (3. haftanın afk balık tutmasını tamamladım bakalım ne zaman ban atacaklar :d )

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

**Solucan**ı skillbar'a koyduğumuzda ve bittiğinde o slot boş kalıyordu. Bu yüzden balık tutarken inventory açık kalsın solucan.jpg'i bulup yem'e kendinisi tıklıyor.
**Minik Balık** ve **karides** gibi yemler düşerse eğer solucanı kullanmayıp bu yemleri kullanıyor bu yemlerin yüzde şansı daha fazla boş geçmiyor.

**Fish** klasöründeki balıkları fotolarından bulup açıyor. Ölü balıkları ikinci kısma koydum üst üste stakeleniyorlar
**Drop** klasöründeki eldiven pelerin şeyleri gece tam AFK olduğumuz için yere atması için ayarlı.

2 bilgisayarda test ettim görüntü güncellemem gerekmedi
-> Oyun çözünürlüğü **800x600**
-> Monitörümün çözünürlüğü **1920x1080**

24.09.2025 tarihi ile sorunsuz çalışıp balık tutmaktadır. Eğer devam edersem projeyi güncellerim. Açık kaynaklı source olduğu için siz de güncelleyebilirsiniz. 
Ban sorumluluğu kabul etmiyorum. 

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
<img src="https://github.com/user-attachments/assets/6c884222-2fae-4e90-9cc5-9faaf92590c3" width="150"/>

### Part1 ve Part2
<img width="140" height="281" alt="image" src="https://github.com/user-attachments/assets/01513b29-6065-4e36-997c-c885f0e1cf10" />

<img width="137" height="284" alt="image" src="https://github.com/user-attachments/assets/29f9b017-628d-40c7-8f14-af62a5389e1e" />


# 🎥 Demo Videosu

<p align="center">
  <a href="https://youtu.be/2nHrGuvzhnU" target="_blank">
    <img src="https://img.youtube.com/vi/2nHrGuvzhnU/maxresdefault.jpg" 
         alt="Proje Tanıtım Videosu" 
         width="600"/>
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/2nHrGuvzhnU" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" 
         alt="YouTube'da İzle" 
         width="120"/>
  </a>
</p>





## 💰 You can help me by Donating

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/handeveloper1)

## 📺 Check out my YouTube Channel

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@handeveloper1)


