📥 Cylne Downloader – YouTube & TikTok Video/Audio Downloader (Termux)

Cylne Downloader adalah tools berbasis Python untuk mengunduh video atau audio dari TikTok, YouTube, dan platform lainnya secara langsung dari Termux Android.

🚀 Mendukung berbagai format: MP4, MP3, M4A
🔄 Auto fallback jika format utama gagal
📁 Bisa simpan ke lokasi bebas (default: /sdcard/Download)


📸 Tampilan

📥 CYLNE DOWNLOADER

🔗 Masukkan URL video (TikTok/YouTube): https://www.tiktok.com/...
📝 Nama file (tanpa ekstensi): videogokil
📁 Lokasi simpan (cth: /sdcard/Download): /sdcard/Download

🎞 Pilih format download:
[1] MP4 (video)
[2] MP3 (audio)
[3] M4A (audio)
Masukkan nomor: 1


📦 Instalasi

1. Buka Termux dan jalankan:

pkg update && pkg install python git -y
pip install yt-dlp rich
termux-setup-storage

2. Clone repo atau download manual:

git clone https://github.com/Cylne/cylne_downloader.git
cd cylne_downloader
python cylne_downloader.py

3. Atau jika file disimpan manual di /sdcard:

cd /sdcard/cylne_downloader/
python cylne_downloader.py



🧠 Fitur Unggulan

✅ Support YouTube, TikTok, Instagram, dll
✅ Pilihan format: MP4, MP3, M4A
✅ Auto retry jika format gagal
✅ Simpan ke folder bebas
✅ Rich UI (dengan warna, progress bar, dan prompt interaktif)


🛠️ File Struktur

/cylne_downloader/
├── cylne_downloader.py   # Main script
├── README.md             # Dokumentasi ini


💡 Catatan

Tidak butuh root

Direkomendasikan simpan ke /sdcard/Download agar mudah ditemukan

Script ini menggunakan yt-dlp, bukan youtube-dl (lebih lengkap & update)


⚠️ Disclaimer

Gunakan script ini untuk penggunaan pribadi dan edukatif. Kami tidak bertanggung jawab atas penyalahgunaan.


✨ Author

Cylne Tools
🛠️ Dibuat oleh: @Hiicylne
📍 Indonesia | Android + Termux Based
