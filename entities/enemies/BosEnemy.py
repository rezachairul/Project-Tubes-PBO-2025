# class/BosEnemy and Child class dari BaseEnemy

# === IMPORT LIBRARY ===
import math                 # library untuk operasi matematika
import pygame               # Library utama untuk membuat game
import random               # Library untuk membuat acak
from pygame.locals import * # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from .BaseEnemy import BaseEnemy
from entities.Bullet import Bullet
from core.resources import (
    ENEMY_BOS_IMAGE,
    BULLET_ENEMY_BOS_IMAGE,
    BULLET_SOUND
)
from core.config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh jenis bos dengan perilaku lebih kompleks.
    - Bisa memiliki pola gerakan dan tembakan yang lebih rumit.
'''

class BosEnemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_BOS_IMAGE, BULLET_ENEMY_BOS_IMAGE, health=25, score_value=50)
        self.angle = 0
        self.vx = random.choice([-2, 2])
        self.vy = 2
        self.score_value = 50

        # Cooldown timer untuk tembakan spiral
        self.fire_delay = 5000  # 5000 ms = 5 detik
        self.last_fire_time = pygame.time.get_ticks()

    # pergerakan bos musuh (segala arah)
    def _move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT // 2:
            self.vy *= -1

    # Tembakan
    def _fire_bullet(self):
        now = pygame.time.get_ticks()
        if now - self.last_fire_time < self.fire_delay:
            return  # Belum waktunya nembak

        self.last_fire_time = now  # Reset timer
        speed = 4
        bullet_count = 24  # Banyak peluru per spiral
        angle_gap = 360 / bullet_count

        for i in range(bullet_count):
            angle_deg = self.angle + i * angle_gap
            angle_rad = math.radians(angle_deg)
            dx = math.cos(angle_rad)
            dy = math.sin(angle_rad)
            bullet = Bullet(
                x=self.rect.centerx,
                y=self.rect.centery,
                direction=(dx, dy),
                speed=speed,
                damage=20,
                image=self.bullet_image,
                is_player=False,
                scale=(10, 15)
            )
            self.bullets.add(bullet)

        self.angle = (self.angle + 15) % 360  # agar spiral berputar
        BULLET_SOUND.play()