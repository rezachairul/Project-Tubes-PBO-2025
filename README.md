# 🚀 Starship War

**Starship War** adalah game arcade sederhana bertema luar angkasa yang dikembangkan menggunakan Python dan pustaka **Pygame**. Pemain mengendalikan pesawat luar angkasa untuk menembak dan menghindari serangan musuh yang datang dari atas layar.

## 🎮 Fitur Utama

- Kontrol pesawat dengan tombol panah kiri dan kanan
- Menembak peluru ke musuh
- Level meningkat setiap 10 skor
- Tampilan antarmuka awal (main menu) dan game over
- Nyawa terbatas (3 kali kesempatan)

## 🧰 Teknologi yang Digunakan

- Python 3
- Pygame

## 📦 Instalasi

1. Pastikan Python 3 sudah terinstal di perangkatmu.
2. Install `pygame` jika belum:
   ```bash
   pip install pygame
   ```
3. Jalankan file game:
   ```bash
   python starshipwar.py
   ```

## 🕹️ Kontrol Game

- ⬅️ Kiri: Gerakkan pesawat ke kiri
- ➡️ Kanan: Gerakkan pesawat ke kanan
- ⬆️ Atas: Tembakkan peluru
- Enter: Mulai game dari menu utama
- ESC: Keluar dari permainan

## 📈 Mekanisme Permainan

- Musuh akan muncul secara acak dari atas layar.
- Jika peluru mengenai musuh, skor bertambah.
- Setiap kelipatan 10 skor, level permainan meningkat.
- Musuh yang tidak dihancurkan dan melewati bawah layar akan mengurangi nyawa pemain.
- Permainan berakhir jika nyawa habis.

## 📂 Struktur File

- `starshipwar.py`: File utama game yang memuat semua logika permainan.

## ✍️ Credits

Game ini dikembangkan untuk tugas kuliah **Pemrograman Berorientasi Objek (PBO)**.
