# 🚀 Starship War

**Starship War** adalah game arcade sederhana bertema luar angkasa yang dikembangkan menggunakan Python dan pustaka **Pygame**. Pemain mengendalikan pesawat luar angkasa untuk menembak dan menghindari serangan musuh yang datang dari atas layar.

---

## 📌 Judul Proyek
**STAR WARSHIP** – Game Arcade Luar Angkasa

---

## 📃 Deskripsi Proyek
Game ini dirancang sebagai tugas akhir mata kuliah **Pemrograman Berorientasi Objek (PBO)** dengan tujuan melatih kemampuan dalam pengembangan game menggunakan Python. Pemain akan mengendalikan pesawat luar angkasa untuk bertahan dari serangan musuh, dan mengumpulkan skor.

---

## 🎮 Fitur Utama
- Kontrol pesawat dengan menggunakan Mouse
- Menembak peluru ke musuh
- Tampilan antarmuka awal (main menu) dan game over
- Nyawa terbatas (3 kali kesempatan)

---

## 🧰 Teknologi yang Digunakan
- Python 3
- Pygame

---

## 📦 Dependensi
Library yang diperlukan untuk menjalankan aplikasi:
```python
import sys         # Untuk keluar dari game
import random      # Untuk angka atau pemilihan acak
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame
```

---

## 📦 Instalasi
1. Pastikan Python 3 sudah terinstal di perangkatmu.
2. Install `pygame` jika belum:
   ```bash
   pip install pygame
   ```
3. Jalankan file game:
   ```bash
   python main.ipynb
   ```

---

## 🕹️ Cara Bermain Game
- ⬅️ Kiri: Gerakkan pesawat ke kiri
- ➡️ Kanan: Gerakkan pesawat ke kanan
- ⬆️ Atas: Tembakkan peluru
- Enter: Mulai game dari menu utama
- ESC: Keluar dari permainan

---

## 📈 Mekanisme Permainan
- Musuh akan muncul secara acak dari atas layar.
- Jika peluru mengenai musuh, skor bertambah.
- Setiap kelipatan 10 skor, level permainan meningkat.
- Musuh yang tidak dihancurkan dan melewati bawah layar akan mengurangi nyawa pemain.
- Permainan berakhir jika nyawa habis.

---

## 📂 Struktur File
- `main.ipynb`: File utama game yang memuat semua logika permainan.

---

## 👥 Kontributor
- Reza Chairul Manam
- Mulya Delani
- Tri Putri Sormin
- Annisa Salsabila
- Willy Syifa Luthfia

---

## 📚 Referensi
- [Pygame Documentation](https://www.pygame.org/docs/)
- Tutorial & Dokumentasi Python
- Materi Kuliah **Pemrograman Berorientasi Objek (PBO)**

---

## ✍️ Credits
Game ini dikembangkan untuk tugas kuliah **Pemrograman Berorientasi Objek (PBO)**.
