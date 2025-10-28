# Kurulum Rehberi - Tekeliler Tekstil E-Ticaret Sitesi

## 📋 Gereksinimler

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 10/11, macOS, Linux
- **Python**: 3.8 veya üzeri
- **RAM**: En az 2GB
- **Disk Alanı**: En az 100MB

### Yazılım Gereksinimleri
- Python 3.8+
- pip (Python paket yöneticisi)
- Modern bir web tarayıcısı (Chrome, Firefox, Safari, Edge)

## 🚀 Adım Adım Kurulum

### 1. Python Kurulumu

#### Windows
1. [Python.org](https://www.python.org/downloads/) adresinden Python'ı indirin
2. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
3. Kurulumu tamamlayın
4. Terminal'de kontrol edin:
   ```bash
   python --version
   ```

#### macOS
```bash
# Homebrew ile
brew install python3
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Proje Dosyalarını İndirme

Projeyi bilgisayarınıza indirin veya klonlayın:
```bash
# Git ile
git clone [proje-url]
cd deneme6

# veya ZIP dosyasını indirip çıkarın
```

### 3. Sanal Ortam Oluşturma (Önerilen)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

Sanal ortam aktif olduğunda terminal başında `(venv)` yazısını görmelisiniz.

### 4. Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

### 5. Uygulamayı Çalıştırma

#### Yöntem 1: start.bat (Windows - En Kolay)
```bash
start.bat
```

#### Yöntem 2: Python ile Doğrudan
```bash
python app.py
```

#### Yöntem 3: Flask CLI
```bash
flask run
```

### 6. Tarayıcıda Açma

Uygulama başladıktan sonra tarayıcınızda şu adresi açın:
```
http://localhost:5000
```

veya

```
http://127.0.0.1:5000
```

## 🔧 Yapılandırma

### Port Değiştirme

Varsayılan port (5000) kullanımda ise, `app.py` dosyasının son satırını düzenleyin:

```python
# app.py dosyasının sonunda
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Port'u değiştirin
```

### Debug Modunu Kapatma (Production için)

```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🐛 Sorun Giderme

### Sorun 1: "Python bulunamadı" Hatası

**Çözüm:**
- Python'ın PATH'e eklendiğinden emin olun
- Terminal'i yeniden başlatın
- Windows'ta: `py` komutu ile deneyin

### Sorun 2: "pip bulunamadı" Hatası

**Çözüm:**
```bash
python -m ensurepip --upgrade
```

### Sorun 3: "Flask bulunamadı" Hatası

**Çözüm:**
```bash
pip install Flask==3.0.0
```

### Sorun 4: Port Kullanımda

**Çözüm:**
- Başka bir port kullanın (yukarıdaki yapılandırmaya bakın)
- veya kullanımdaki uygulamayı kapatın:

**Windows:**
```bash
netstat -ano | findstr :5000
taskkill /PID [PID_NUMARASI] /F
```

**macOS/Linux:**
```bash
lsof -ti:5000 | xargs kill -9
```

### Sorun 5: Static Dosyalar Yüklenmiyor (404 Hatası)

**Çözüm:**
- `static` klasörünün varlığını kontrol edin
- Klasör yapısının doğru olduğundan emin olun:
  ```
  deneme6/
  ├── static/
  │   ├── css/
  │   │   └── style.css
  │   └── js/
  │       └── main.js
  ```
- Tarayıcı önbelleğini temizleyin (Ctrl+Shift+Del)

### Sorun 6: JavaScript Hatası (changeSlide is not defined)

**Çözüm:**
- `static/js/main.js` dosyasının mevcut olduğunu kontrol edin
- Tarayıcı konsolunu açın (F12) ve hataları kontrol edin
- Tarayıcı önbelleğini temizleyin

### Sorun 7: Sayfa Stilsiz Görünüyor

**Çözüm:**
- `static/css/style.css` dosyasının varlığını kontrol edin
- Tarayıcı geliştirici araçlarında (F12) Network sekmesini kontrol edin
- Tarayıcıyı yenileyin (Ctrl+F5 - hard refresh)

## 📱 Mobil Test

Yerel ağınızdaki diğer cihazlardan test etmek için:

1. Bilgisayarınızın IP adresini öğrenin:

**Windows:**
```bash
ipconfig
```

**macOS/Linux:**
```bash
ifconfig
```

2. `app.py` dosyasında `host='0.0.0.0'` olduğundan emin olun

3. Mobil cihazınızdan şu adresi açın:
```
http://[BILGISAYAR_IP]:5000
```

Örnek: `http://192.168.1.100:5000`

## 🔒 Güvenlik Notları

### Development (Geliştirme) Ortamı
- Debug modu AÇIK
- Host: 0.0.0.0 (tüm bağlantıları kabul eder)
- Güvenlik önlemleri minimal

### Production (Canlı) Ortamı İçin
1. Debug modunu kapatın
2. Secret key'i güçlü bir değere değiştirin
3. HTTPS kullanın
4. Güvenlik duvarı yapılandırın
5. Production sunucu kullanın (Gunicorn, uWSGI)
6. Reverse proxy kullanın (Nginx, Apache)

## 📚 Ek Kaynaklar

- [Flask Dokümantasyonu](https://flask.palletsprojects.com/)
- [Python Dokümantasyonu](https://docs.python.org/)
- [HTML/CSS/JavaScript - MDN](https://developer.mozilla.org/)

## ✅ Kurulum Kontrol Listesi

- [ ] Python 3.8+ yüklü
- [ ] pip güncel
- [ ] Proje dosyaları indirildi
- [ ] Sanal ortam oluşturuldu (opsiyonel ama önerilen)
- [ ] requirements.txt yüklendi
- [ ] Uygulama başarıyla başlatıldı
- [ ] http://localhost:5000 açıldı
- [ ] Ana sayfa düzgün görünüyor
- [ ] Slider çalışıyor
- [ ] Ürünler sayfası açılıyor
- [ ] Arama çalışıyor
- [ ] Sepete ekleme çalışıyor

## 💡 İpuçları

1. **Sanal Ortam Kullanın**: Proje bağımlılıklarını izole eder
2. **requirements.txt'yi Güncel Tutun**: Yeni paket ekledikçe güncelleyin
3. **Git Kullanın**: Değişiklikleri takip edin
4. **Yedek Alın**: Önemli değişiklikler öncesi yedek alın
5. **Tarayıcı Önbelleğini Temizleyin**: CSS/JS değişikliklerinde

## 📞 Yardım

Sorun yaşıyorsanız:

1. **Terminal çıktısını kontrol edin**: Hata mesajları önemli ipuçları verir
2. **requirements.txt'yi yeniden yükleyin**: `pip install -r requirements.txt --force-reinstall`
3. **Sanal ortamı yeniden oluşturun**: Bazen en etkili çözüm
4. **Python versiyonunu kontrol edin**: 3.8+ olmalı
5. **İnternet bağlantısını kontrol edin**: CDN'ler için gerekli (Font Awesome)

---

**Başarılar! 🎉**

Kurulum tamamlandıktan sonra `http://localhost:5000` adresinden güzel e-ticaret sitenize ulaşabilirsiniz.

