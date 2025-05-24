# class/HorizontalEnemy and Child class dari BaseEnemy

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from .BaseEnemy import BaseEnemy
from entities.Bullet import Bullet
from core.resources import (
    ENEMY_HORIZONTAL_IMAGE, 
    BULLET_ENEMY_HORIZONTAL_IMAGE,
    BULLET_SOUND
)

# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak secara horizontal (kiri/kanan).
'''

class HorizontalEnemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_HORIZONTAL_IMAGE, BULLET_ENEMY_HORIZONTAL_IMAGE, health=10, score_value=20)
        self.direction = 1  # 1 = kanan, -1 = kiri

    # Pergerakan musuh horizontal
    def _move(self):
        self.rect.x += 3 * self.direction
        # Bounce balik arah
        if self.rect.left <= 0 or self.rect.right >= 800:  # ganti sesuai lebar layar
            self.direction *= -1
            self.rect.y += 20  # sedikit turun
    
    # Tembakan
    def _fire_bullet(self):
        dx = 5 * self.direction  # sesuai arah gerak
        # bullet = Bullet(self.rect.centerx, self.rect.centery, dx, 0, self.bullet_image)
        bullet = Bullet(
            x=self.rect.centerx,
            y=self.rect.centery,
            direction=(dx, 0),  # Mengirimkan tuple (dx, 0) sebagai direction
            speed=0.5,
            damage=10,
            image=self.bullet_image,
            is_player=False,
            scale=(15, 25)
        )
        self.bullets.add(bullet)
        BULLET_SOUND.play()