# class/BaseEnemy and Child class (VerticalEnemy, HorizontalEnemy, FastEnemy, BosEnemy)

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from core.resources import BULLET_SOUND, EXPLOSION_SOUND

from entities.Bullet import Bullet
from entities.Explosion import Explosion

# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
"""
    - Class dasar untuk musuh.
    - Bisa digunakan sebagai vertical mover, horizontal mover, atau lainnya.
    - Mengatur posisi, gerakan, dan logika tembakan.
"""
class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, bullet_image_path, health=1, score_value=100):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ukuran default
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = health
        self.score_value = score_value

        # Simpan path peluru enemy
        self.bullet_image_path = bullet_image_path
        self.bullet_image = pygame.image.load(self.bullet_image_path).convert_alpha()

        self.bullets = pygame.sprite.Group()
        self.last_shoot_time = pygame.time.get_ticks()
        self.shoot_cooldown = 1000  # ms

    def update(self): # Update posisi, tembakan dan peluru
        self._move()
        self._shoot()
        self.bullets.update()

    def _move(self): # Gerakan musuh (diimplementasi di child class).
        pass

    def _shoot(self): # Tembak peluru jika cooldown selesai.
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time >= self.shoot_cooldown:
            self._fire_bullet()
            self.last_shoot_time = now

    def _fire_bullet(self): # # Membuat dan menembakkan peluru ke bawah (default behavior)
        bullet = Bullet(self.rect.centerx, self.rect.bottom, direction=(0, 5), speed=5, damage=10, image=self.bullet_image, is_player=False)
        self.bullets.add(bullet)
        BULLET_SOUND.play()

    def take_damage(self, damage=1):
         return self.take_hit(damage)
        # self.take_hit() 

    def take_hit(self, damage=1): # Kurangi health musuh. Jika health habis, musuh mati.
        self.health -= damage
        if self.health <= 0:
            return self.dead()
        return None

    def dead(self): # Musuh mati, hapus dari game.
        EXPLOSION_SOUND.play()
        explosion = Explosion(self.rect.centerx, self.rect.centery)
        self.kill()
        return explosion