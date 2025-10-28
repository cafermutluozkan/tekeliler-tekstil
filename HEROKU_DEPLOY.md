# 🚀 HEROKU DEPLOYMENT REHBERİ

## ✅ Eklenen Dosyalar

Heroku'da çalışması için aşağıdaki dosyalar eklendi:

### 1. **Procfile** 
```
web: gunicorn app:app
```
- Heroku'ya uygulamanın nasıl çalıştırılacağını söyler
- `gunicorn` production WSGI server kullanır
- `app:app` → `app.py` dosyasındaki `app` Flask instance'ını çalıştırır

### 2. **runtime.txt**
```
python-3.12.0
```
- Heroku'ya hangi Python versiyonunu kullanacağını söyler
- Python 3.12.0 kullanılacak

### 3. **requirements.txt** (Güncellendi)
```
Flask==3.0.0
Werkzeug==3.0.1
gunicorn==21.2.0  ← YENİ!
```
- `gunicorn` production server eklendi

### 4. **app.py** (Güncellendi)
```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
```
- Heroku'nun dinamik PORT değişkenini kullanır
- Debug mode kapatıldı (production için)

---

## 📋 HEROKU DEPLOYMENT ADIMLARI

### Yöntem 1: Heroku CLI ile Deploy (Önerilen)

#### 1. Heroku CLI Kurulumu
https://devcenter.heroku.com/articles/heroku-cli adresinden indirin

#### 2. Heroku'ya Giriş
```bash
heroku login
```

#### 3. Heroku App Oluştur
```bash
cd C:\Users\seyit\OneDrive\Masaüstü\deneme6
heroku create tekeliler-tekstil
```
veya kendi app isminizi belirleyin:
```bash
heroku create
```

#### 4. Heroku'ya Deploy
```bash
git push heroku main
```

#### 5. App'i Aç
```bash
heroku open
```

#### 6. Logları Görüntüle (Hata varsa)
```bash
heroku logs --tail
```

---

### Yöntem 2: GitHub Entegrasyonu ile Deploy (Kolay)

#### 1. Heroku Dashboard'a Git
https://dashboard.heroku.com/

#### 2. "New" → "Create new app"
- App ismi: `tekeliler-tekstil` (veya başka bir isim)
- Region: Europe
- "Create app"

#### 3. Deploy Sekmesi
- Deployment method: **GitHub** seçin
- Repository ara: `cafermutluozkan/tekeliler-tekstil`
- "Connect" butonuna tıkla

#### 4. Otomatik Deploy Aktif Et (Opsiyonel)
- "Enable Automatic Deploys" → Her GitHub push'ta otomatik deploy
- veya
- "Manual Deploy" → "Deploy Branch" ile manuel deploy

#### 5. Deploy Başlat
- Branch seç: `main`
- "Deploy Branch" butonuna tıkla

#### 6. Uygulamayı Aç
- Sağ üst köşede "Open app" butonuna tıkla

---

## 🔍 HATA ÇÖZÜMLERI

### Hata 1: "Application Error"
**Çözüm:**
```bash
heroku logs --tail
```
Logları kontrol edin, hatayı görün.

### Hata 2: "No web process running"
**Çözüm:**
```bash
heroku ps:scale web=1
```

### Hata 3: "Python version not available"
**Çözüm:** `runtime.txt`'yi düzenleyin:
```
python-3.11.7
```
veya
```
python-3.10.13
```

Heroku'nun desteklediği versiyonlar:
https://devcenter.heroku.com/articles/python-support#supported-runtimes

### Hata 4: "Module not found"
**Çözüm:** `requirements.txt`'de eksik paket var
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push heroku main
```

---

## ⚙️ ENVIRONMENT VARIABLES (Opsiyonel)

Hassas bilgiler için environment variable kullanın:

```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set FLASK_ENV=production
```

`app.py`'de kullanım:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-key')
```

---

## 📊 HEROKU KOMUTLARI

```bash
# App durumu
heroku ps

# Restart
heroku restart

# Loglar
heroku logs --tail

# Config değişkenleri
heroku config

# Shell aç
heroku run bash

# Database migrate (ileride)
heroku run python manage.py migrate
```

---

## 🎯 DEPLOYMENT CHECKLIST

- [x] ✅ Procfile oluşturuldu
- [x] ✅ runtime.txt oluşturuldu
- [x] ✅ gunicorn requirements.txt'ye eklendi
- [x] ✅ app.py PORT ayarı yapıldı
- [x] ✅ Debug mode kapatıldı
- [x] ✅ .gitignore var (gereksiz dosyalar push edilmeyecek)
- [x] ✅ GitHub'a push yapıldı

---

## 🌐 DEPLOYMENT SONRASI

Heroku URL'niz şöyle olacak:
```
https://tekeliler-tekstil.herokuapp.com
```
veya
```
https://YOUR-APP-NAME.herokuapp.com
```

---

## 💡 ÜCRETSİZ PLAN LİMİTLERİ

Heroku Free Tier (artık yok, Eco Dyno $5/ay):
- Eco Dyno: $5/ay
- 1000 saat/ay çalışma
- Uyku modu: 30 dakika aktivite yoksa uyur

**Alternatifler:**
- **Railway.app** → Free tier var
- **Render.com** → Free tier var
- **Fly.io** → Free tier var
- **PythonAnywhere** → Free tier var

---

## 🚨 ÖNEMLİ NOTLAR

1. **Secret Key:** Production'da güçlü bir secret key kullanın
2. **Database:** İleride PostgreSQL ekleyebilirsiniz
3. **Static Files:** Şu an static files Flask üzerinden sunuluyor (küçük projeler için OK)
4. **SSL:** Heroku otomatik HTTPS sağlar
5. **Domain:** Kendi domain'inizi bağlayabilirsiniz

---

📅 **Oluşturulma:** 28 Ekim 2025  
🔗 **GitHub:** https://github.com/cafermutluozkan/tekeliler-tekstil  
🚀 **Versiyon:** 2.2 (Heroku Ready)

