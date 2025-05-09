# class/Explosion.py

# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import math        # Untuk operasi matematika seperti sin, cos, radians, dll (misalnya untuk gerakan melingkar)
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module



# === KELAS EXPLOSION (Ledakan) ===
"""
    - Class untuk efek ledakan saat musuh terkena peluru.
    - Memiliki beberapa frame untuk animasi ledakan
    - Membuat efek suara ledakan
"""
# Script Kelas Explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = None  # Gambar atau animasi ledakan
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Posisi ledakan
        self.life_duration = 12  # Durasi hidup ledakan (misalnya berapa frame)
        self.timer = 0  # Timer untuk menghitung durasi hidup ledakan

    def update(self):
        # Update ledakan (mengurangi durasi hidup)
        self._countdown()

    def _countdown(self):
        # Menurunkan timer dan menghapus ledakan setelah waktu habis
        pass

    def deactivate(self):
        # Menonaktifkan ledakan setelah selesai (misalnya setelah animasi selesai)
        pass