# class/BackgroundStar.py

# === IMPORT LIBRARY ===
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import math        # Untuk operasi matematika seperti sin, cos, radians, dll (misalnya untuk gerakan melingkar)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

from core.config import SCREEN_WIDTH, SCREEN_HEIGHT

# === KELAS BACKGROUND STAR (Bintang Latar Belakang) ===
"""
    Class untuk membuat bintang-bintang latar belakang yang jatuh dari atas layar:
    - Posisi acak di layar
    - Kecepatan jatuh acak
    - Ukuran bintang acak (1-2 piksel)
"""
class BackgroundStar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Ukuran bintang (acak)
        self.radius = random.randint(1, 2) # Menghasilkan ukuran acak untuk bintang, antara 1 dan 2 piksel
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)
        
        # Posisi awal bintang (acak) Menentukan posisi acak untuk pusat orbit bintang di layar
        self.rect = self.image.get_rect() #Mendapatkan rect (kotak pembatas) dari gambar bintang.
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGHT)
        self.angle = random.uniform(0, 2 * math.pi)  # dalam radian

        # Jarak dari pusat (untuk gerakan melingkar)
        self.orbit_radius = random.randint(10, 100)
        self.rotation_speed = random.uniform(0.001, 0.01)

        # Twinkle effect
        self.alpha_base = random.randint(150, 255)
        self.twinkle_speed = random.uniform(0.05, 0.15)
        self.twinkle_angle = random.uniform(0, 2 * math.pi)

    def update(self):
        # Perbarui posisi melingkar
        self.angle += self.rotation_speed
        self.rect.x = int(self.center_x + self.orbit_radius * math.cos(self.angle))
        self.rect.y = int(self.center_y + self.orbit_radius * math.sin(self.angle))

        # Efek kedipan
        self.twinkle_angle += self.twinkle_speed
        alpha = self.alpha_base + int(50 * math.sin(self.twinkle_angle))
        alpha = max(50, min(255, alpha))
        self.image.set_alpha(alpha)