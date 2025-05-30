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
   python main.py
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
<pre>
📦stars warship
 ┣ 📂.git
 ┣ 📂assets
 ┃ ┣ 📂font
 ┃ ┃ ┣ 📜Gameplay.ttf
 ┃ ┃ ┣ 📜HUTheGame.ttf
 ┃ ┃ ┗ 📜PixelGameFont.ttf
 ┃ ┣ 📂img
 ┃ ┃ ┣ 📜bullet_enemy.png
 ┃ ┃ ┣ 📜bullet_enemy_bos.png
 ┃ ┃ ┣ 📜bullet_player.png
 ┃ ┃ ┣ 📜enemy_bos.png
 ┃ ┃ ┣ 📜enemy_fast.png
 ┃ ┃ ┣ 📜enemy_horizontal.png
 ┃ ┃ ┣ 📜enemy_vertical.png
 ┃ ┃ ┣ 📜exp1.png
 ┃ ┃ ┣ 📜exp2.png
 ┃ ┃ ┣ 📜exp3.png
 ┃ ┃ ┣ 📜exp4.png
 ┃ ┃ ┣ 📜exp5.png
 ┃ ┃ ┗ 📜playership.png
 ┃ ┣ 📂reference
 ┃ ┗ 📂sound
 ┃ ┃ ┣ 📜audio_explosion.wav
 ┃ ┃ ┣ 📜audio_laser.wav
 ┃ ┃ ┣ 📜Game Over Theme.mp3
 ┃ ┃ ┣ 📜music-alien.mp3
 ┃ ┃ ┗ 📜music.wav
 ┣ 📂core
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜config.py
 ┃ ┣ 📜game.py
 ┃ ┣ 📜resources.py
 ┃ ┗ 📜utils.py
 ┣ 📂entities
 ┃ ┣ 📂enemies
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜BaseEnemy.py
 ┃ ┃ ┣ 📜BosEnemy.py
 ┃ ┃ ┣ 📜FastEnemy.py
 ┃ ┃ ┣ 📜HorizontalEnemy.py
 ┃ ┃ ┗ 📜VerticalEnemy.py
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜BackgroundStar.py
 ┃ ┣ 📜Bullet.py
 ┃ ┣ 📜Explosion.py
 ┃ ┗ 📜Player.py
 ┣ 📜folder.txt
 ┣ 📜main.py
 ┣ 📜main_.py
 ┣ 📜README.md
 ┗ 📜uml_game.puml

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
Link Youtube Demo Game: [Star Warship](https://youtu.be/26ugjIAx2XI)
Link Laporan Akhir: [Laporan Akhir](https://www.overleaf.com/read/ckbfngyzchcn#cc9cba)

