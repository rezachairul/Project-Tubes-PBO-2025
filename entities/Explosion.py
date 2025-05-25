# class/Explosion.py

# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import math        # Untuk operasi matematika seperti sin, cos, radians, dll (misalnya untuk gerakan melingkar)
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module

EXPLOSION_FRAMES = [pygame.image.load(f'assets/img/exp{i}.png') for i in range(5)]

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
        self.frames = EXPLOSION_FRAMES  # List gambar animasi
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.frame_timer = 0  # waktu antar frame
        self.frame_delay = 5  # jeda antar frame (semakin kecil, semakin cepat)

    def update(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index += 1

            if self.frame_index < len(self.frames):
                self.image = self.frames[self.frame_index]
            else:
                self.kill()  # Hapus ledakan setelah animasi selesai

    def deactivate(self):
        # Menonaktifkan ledakan setelah selesai (misalnya setelah animasi selesai)
        self.kill()