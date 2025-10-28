# Tekeliler Tekstil - Modern E-Ticaret Sitesi

Modern ve profesyonel bir halı, kilim ve perde satış sitesi.

![Status](https://img.shields.io/badge/Status-Çalışıyor-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Özellikler

### 🎯 Temel Özellikler
- 🎨 **Modern ve responsive tasarım** - Tüm cihazlarda mükemmel görünüm
- 🛍️ **Ürün katalog sistemi** - 6 kategorize edilmiş ürün
- 📱 **Mobil uyumlu** - Telefon, tablet ve masaüstü desteği
- 🔍 **Canlı arama** - Anlık ürün arama özelliği
- 💳 **Sepet yönetimi** - LocalStorage ile kalıcı sepet
- 📧 **İletişim formu** - AJAX ile form gönderimi
- ⭐ **Müşteri yorumları** - Sosyal kanıt bölümü
- 📊 **Ürün detay sayfaları** - Detaylı ürün bilgileri

### 🎭 Görsel Özellikler
- ✅ Otomatik dönen slider (3 slayt, 5 saniye)
- ✅ Hover animasyonları ve geçişler
- ✅ Modal pencere sistemi
- ✅ Notification (bildirim) sistemi
- ✅ Smooth scroll
- ✅ Intersection Observer animasyonları
- ✅ Responsive grid sistem

### 🛠️ Teknik Özellikler
- ✅ Flask 3.0.0 backend
- ✅ Jinja2 template engine
- ✅ Vanilla JavaScript (framework yok)
- ✅ CSS3 animations
- ✅ Font Awesome icons
- ✅ RESTful API endpoints
- ✅ JSON veri formatı

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Kurulum

1. **Paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

2. **Uygulamayı çalıştırın:**
```bash
python app.py
```

veya

```bash
start.bat  # Windows için
```

3. **Tarayıcınızda açın:**
```
http://localhost:5000
```

## 📁 Proje Yapısı

```
deneme6/
├── app.py                    # Flask backend
├── main.py                   # PyCharm örnek (kullanılmıyor)
├── requirements.txt          # Python bağımlılıkları
├── start.bat                 # Windows başlatma scripti
├── README.md                 # Bu dosya
├── BASLAT.txt               # Hızlı başlatma talimatı
├── HIZLI_BASLANGIC.txt      # Detaylı başlangıç rehberi
├── KURULUM_REHBERI.md       # Kurulum dokümantasyonu
├── GUNCELLEME_RAPORU.md     # Değişiklik kayıtları
├── templates/                # HTML şablonları
│   ├── base.html            # Ana layout
│   ├── index.html           # Ana sayfa
│   ├── products.html        # Ürün listesi
│   ├── product_detail.html  # Ürün detay
│   ├── about.html           # Hakkımızda
│   └── contact.html         # İletişim
└── static/                   # Statik dosyalar
    ├── css/
    │   └── style.css        # Tüm CSS stilleri
    └── js/
        └── main.js          # Tüm JavaScript kodu
```

## 🌐 Sayfalar ve Rotalar

| Sayfa | URL | Açıklama |
|-------|-----|----------|
| Ana Sayfa | `/` | Hero slider, özellikler, öne çıkan ürünler |
| Ürünler | `/products` | Tüm ürünlerin listesi |
| Halılar | `/products?category=hali` | Sadece halı kategorisi |
| Kilimler | `/products?category=kilim` | Sadece kilim kategorisi |
| Perdeler | `/products?category=perde` | Sadece perde kategorisi |
| Ürün Detay | `/product/<id>` | Tek ürün detayları |
| Hakkımızda | `/about` | Şirket bilgileri |
| İletişim | `/contact` | İletişim formu ve bilgiler |

### API Endpoints

| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/api/search?q=<query>` | GET | Ürün arama |
| `/api/contact` | POST | İletişim formu gönderimi |

## 🎨 Özellikler Detayları

### Hero Slider
- 3 otomatik dönen slayt
- Manuel ileri/geri navigasyon
- Dot navigasyon
- Hover'da durdurma
- 5 saniyelik otomatik geçiş

### Arama Sistemi
- Modal pencere tasarımı
- Canlı arama (300ms debounce)
- Gerçek zamanlı sonuç gösterimi
- Ürün görselleri ile birlikte sonuçlar

### Sepet Sistemi
- LocalStorage ile kalıcı saklama
- Sepet sayacı (badge)
- Notification bildirimleri
- Ürün ekleme/çıkarma

### Responsive Tasarım
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (<768px)
- Hamburger menü (mobil)

## 🛠️ Teknolojiler

### Backend
- **Flask 3.0.0** - Python web framework
- **Werkzeug 3.0.1** - WSGI utility library
- **Jinja2** - Template engine

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling & animations
- **JavaScript (ES6+)** - Functionality
- **Font Awesome 6.4.0** - Icons

### Diğer
- **Unsplash** - Placeholder images
- **LocalStorage** - Sepet verisi

## 📖 Dokümantasyon

- **BASLAT.txt** - Hızlı başlatma talimatları
- **HIZLI_BASLANGIC.txt** - Detaylı başlangıç rehberi
- **KURULUM_REHBERI.md** - Adım adım kurulum
- **GUNCELLEME_RAPORU.md** - Tüm değişiklikler ve düzeltmeler

## 🐛 Düzeltilen Hatalar

✅ **404 Hatası** - Static dosyalar düzgün yükleniyor
✅ **changeSlide is not defined** - JavaScript fonksiyonu eklendi
✅ **Slider çalışmıyor** - Otomatik slider sistemi eklendi
✅ **CSS yüklenmiyor** - Flask static routing düzeltildi

## 🔧 Yapılandırma

### Port Değiştirme
`app.py` dosyasının son satırını düzenleyin:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Port değiştirildi
```

### Debug Modu Kapatma
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🧪 Test

```bash
# Uygulamayı başlatın
python app.py

# Tarayıcıda test edin
http://localhost:5000

# Kontrol listesi:
✓ Slider otomatik dönüyor mu?
✓ Ürünler sayfası açılıyor mu?
✓ Arama çalışıyor mu?
✓ Sepete ekleme çalışıyor mu?
✓ Mobil menü çalışıyor mu?
```

## 📱 Mobil Test

Aynı WiFi ağındaki mobil cihazdan test etmek için:

1. Bilgisayarın IP adresini öğren:
```bash
ipconfig  # Windows
ifconfig  # macOS/Linux
```

2. Mobil tarayıcıda aç:
```
http://[BILGISAYAR_IP]:5000
```

## 🚧 Gelecek Geliştirmeler

### Backend
- [ ] Gerçek veritabanı (SQLite/PostgreSQL)
- [ ] Kullanıcı kayıt/giriş
- [ ] Admin paneli
- [ ] Ödeme entegrasyonu
- [ ] E-posta bildirimleri

### Frontend
- [ ] Sepet sayfası
- [ ] Checkout süreci
- [ ] Kullanıcı profili
- [ ] Ürün karşılaştırma
- [ ] Favori ürünler
- [ ] Ürün yorumları

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

## 👨‍💻 Geliştirici

Tekeliler Tekstil Development Team

## 📞 İletişim

- Email: info@tekeliler.com
- Tel: +90 555 123 45 67
- Adres: İstanbul, Türkiye

---

**⭐ Beğendiyseniz yıldız vermeyi unutmayın!**

**Son Güncelleme:** 28 Ekim 2025 | **Versiyon:** 1.0.0

## Sayfalar

- **Ana Sayfa**: Öne çıkan ürünler ve kategoriler
- **Ürünler**: Tüm ürünler ve filtreleme
- **Ürün Detayı**: Detaylı ürün bilgisi
- **Hakkımızda**: Şirket bilgileri
- **İletişim**: İletişim formu ve bilgiler

## Teknolojiler

- Flask (Python Web Framework)
- HTML5
- CSS3
- JavaScript
- Font Awesome
- Google Fonts

## Lisans

© 2025 Tekeliler Tekstil. Tüm hakları saklıdır.

