# class/BaseEnemy and Child class (VerticalEnemy, HorizontalEnemy, FastEnemy, BosEnemy)

# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import math        # Untuk operasi matematika seperti sin, cos, radians, dll (misalnya untuk gerakan melingkar)
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module




from entities.Bullet import Bullet
from entities.Explosion import Explosion


# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
"""
    - Class dasar untuk musuh.
    - Bisa digunakan sebagai vertical mover, horizontal mover, atau lainnya.
    - Mengatur posisi, gerakan, dan logika tembakan.
"""
class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, health=1, score_value=100):
        super().__init__()
        self.health = health
        self.score_value = score_value

    def update(self):
        self._move()
        self._shoot()

    def _move(self):
        pass

    def _shoot(self):
        pass

    def _fire_bullet(self):
        pass

    def take_hit(self):
        # Dikena peluru player
        pass

    def dead(self):
        # Kalau health <= 0
        pass