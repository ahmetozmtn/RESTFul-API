# 🧪 Test Reports

## ✅ 1. Pozitif Senaryolar (Happy Path)
- [x] Kullanıcı ekleme (`POST /api/addData`)
- [x] Tüm kullanıcıları listeleme (`GET /api/getData`)
- [x] Kullanıcı güncelleme (`PUT /api/updateData/<id>`)
- [x] Kullanıcı silme (`DELETE /api/deleteData/<id>`)
- [x] Tüm kullanıcıları silme (`DELETE /api/allDelete`)

## ❌ 2. Negatif Senaryolar
- [ ] Eksik alanla kayıt ekleme → ❗ 200 dönüyor (Beklenen: 400/422)
- [ ] Boş alanla kayıt ekleme → ❗ 200 dönüyor (Beklenen: 400/422)
- [x] Var olmayan ID ile güncelleme → ✅ 404 dönüyor
- [ ] Var olmayan ID ile silme → ❗ 200 dönüyor (Beklenen: 400/404)

## 🗃️ 3. Veritabanı Doğrulama
- [x] Eklenen veriler DB'de kontrol edildi
- [x] Güncellenen veriler DB'de kontrol edildi
- [x] Silinen verilerin DB'den silindiği doğrulandı

## 📝 Ek Notlar
- Validasyon eksiklikleri mevcut.
- `username`, `password` gibi alanlar eksik bile olsa 200 dönebiliyor.
- `bcrypt` kullanımında eksik/boş şifre `500` hatasına sebep oluyor.


# Testlerin Çalıştırılması
1. Ortamı hazırla (Python, virtualenv, vs.)
2. Gerekli paketleri yükle: `pip install -r requirements.txt`
3. Testleri çalıştır: `pytest`
