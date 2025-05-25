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

from core.config import (
    SCREEN_WIDTH
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
        self.speed = 3  # kecepatan gerak ke kanan

    def _move(self):
        self.rect.x += self.speed  # gerak ke kanan
        # Jika sudah keluar dari layar kanan
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = -self.rect.width  # muncul ulang dari kiri luar layar
            self.rect.y += 40  # bisa juga tambah turun agar nggak datar terus

    def _fire_bullet(self):
        bullet = Bullet(
            x=self.rect.centerx,
            y=self.rect.centery,
            direction=(5, 0),  # peluru ke kanan
            speed=0.5,
            damage=10,
            image=self.bullet_image,
            is_player=False,
            scale=(15, 25)
        )
        self.bullets.add(bullet)
        BULLET_SOUND.play()
