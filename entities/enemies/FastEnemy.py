# class/FastEnemy and Child class dari BaseEnemy

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from .BaseEnemy import BaseEnemy
from entities.Bullet import Bullet
from core.resources import (
    ENEMY_FAST_IMAGE,
    BULLET_ENEMY_FAST_IMAGE,
    BULLET_SOUND
)


# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak dengan kecepatan tinggi.
'''

class FastEnemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_FAST_IMAGE, BULLET_ENEMY_FAST_IMAGE, health=15, score_value=30)

    # Pergerakan musuh cepat
    def _move(self):
        self.rect.y += 5  # cepat turun
    
    # Tembakan
    def _fire_bullet(self):
        # bullet = Bullet(self.rect.centerx, self.rect.bottom, 0, 7, self.bullet_image)
        bullet = Bullet(
            x=self.rect.centerx,
            y=self.rect.bottom,
            direction=(0, 1),  # Mengirimkan tuple (0, 1) sebagai direction untuk peluru vertikal
            speed=7,
            damage=10,
            image=self.bullet_image,
            is_player=False,
            scale=(15, 25)
        )
        self.bullets.add(bullet)
        BULLET_SOUND.play()