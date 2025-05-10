# 🚀 Star Warship

**Star Warship** adalah game arcade sederhana bertema luar angkasa yang dikembangkan menggunakan Python dan pustaka **Pygame**. Pemain mengendalikan pesawat luar angkasa untuk menembak dan menghindari serangan musuh yang datang dari atas layar.

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
- 🖱️ Gerakkan mouse ke kiri atau kanan untuk menggerakkan pesawat.
- 🔫 Peluru akan menembak secara otomatis.
- ⏎  Enter: Mulai game dari menu utama
- ⏸️ Tekan Spasi untuk pause/sementara berhenti.
- ⛔ ESC: Keluar dari permainan

---

## 📈 Mekanisme Permainan
- Musuh akan muncul secara acak dari atas layar.
- Jika peluru mengenai musuh, skor bertambah.
- Musuh yang tidak dihancurkan dan melewati bawah layar akan mengurangi nyawa pemain.
- Permainan berakhir jika nyawa habis.

---

## 📂 Struktur File
stars_warship/
 ├── main.py                 # File utama game yang memuat semua logika permainan
 ├── core/
 │   ├── config.py           # Konfigurasi umum (layar, FPS, dll)
 │   ├── resources.py        # Path gambar, suara, dan loading-nya
 │   ├── game.py             # Inisialisasi dan loop utama game (kalau kamu pisahkan main loop)
 │   ├── utils.py            # Fungsi bantu, misalnya konversi, atau tools lain
 ├── entities/
 │   ├── player.py           # Class Player
 │   ├── bullet.py           # Class Bullet
 │   ├── explosion.py        # Class Explosion
 │   ├── background_star.py  # Class BackgroundStar
 │   └── enemies/
 │       ├── base_enemy.py   # BaseEnemy
 │       ├── vertical.py     # VerticalEnemy
 │       ├── horizontal.py   # HorizontalEnemy
 │       ├── fast.py         # FastEnemy
 │       └── boss.py         # BossEnemy
 ├── assets/
 │   ├── img/
 │   │   └── ...             # Gambar sprite
 │   ├── sound/
 │   │   └── ...             # File audio
 │   └── font/
 │       └── ...             # File font
 └── README.md


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
