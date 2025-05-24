# class/VerticalEnemy and Child class dari BaseEnemy

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from .BaseEnemy import BaseEnemy
from entities.Bullet import Bullet
from core.resources import (
    ENEMY_VERTICAL_IMAGE, 
    BULLET_ENEMY_VERTICAL_IMAGE,
    BULLET_SOUND
)
from core.config import (
    SCREEN_HEIGHT
)

# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak secara vertikal (atas/bawah).
'''

class VerticalEnemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_VERTICAL_IMAGE, BULLET_ENEMY_VERTICAL_IMAGE, health=10, score_value=10)
        self.score_value = 10

    # Pergerakan musuh vertikal
    def _move(self):
        self.rect.y += 2  # gerak vertikal pelan
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height  # reset ke atas layar

    
    # Tembakan
    def _fire_bullet(self):
        bullet = Bullet(
            self.rect.centerx, 
            self.rect.bottom,
            direction=(0, 5),
            speed=0.5,
            damage=10, 
            image=self.bullet_image, 
            is_player=False,
            scale=(15, 25)
        )
        self.bullets.add(bullet)
        BULLET_SOUND.play()