
# 🔍 Dizin Tarama Aracı (Directory Fuzzer)

Bu araç, belirtilen bir hedef URL için verilen wordlist dosyasını kullanarak olası dizinleri ve endpoint'leri bulmaya yarar. HTTP cevaplarını analiz eder ve wildcard yönlendirmelerini (örn: olmayan sayfaların hepsinin aynı response'u dönmesi) filtreleyerek gerçek dizinleri tespit eder.

## 🚀 Özellikler

- `200`, `301`, `302`, `403` durum kodlarına odaklanır.
- Wildcard yanıtlarını test ederek gereksiz dizinleri filtreler.
- Belirli saniye aralığında istek göndererek hız sınırlaması yapar.
- Bulunan dizinleri `result.txt` dosyasına kaydeder.

---

## 📦 Gereksinimler

- Python 3.x
- `requests` kütüphanesi (yüklemek için: `pip install requests`)

---

## 🧠 Kullanım

```bash
python dizin_tara.py
