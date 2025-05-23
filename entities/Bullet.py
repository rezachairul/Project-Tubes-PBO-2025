# class/Bullet.py

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module
from core.utils import *
from core.resources import EXPLOSION_SOUND, BULLET_SOUND
# === KELAS BULLET (Peluru) ===
"""
    - Peluru yang ditembakkan oleh musuh dan player.
    - Memiliki kecepatan dan ukuran tertentu
    - Membuat efek ledakan ketika mengenai target
"""
# === KELAS BULLET (Peluru) ===
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, damage, image, is_player=False, scale=None):
        super().__init__()
        # self.image = pygame.image.load(image).convert_alpha()  # Gambar peluru (akan diubah sesuai jenisnya)
        
        # Cek apakah image adalah string (path), atau Surface langsung
        if isinstance(image, str):
            self.image = pygame.image.load(image).convert_alpha()
        elif isinstance(image, pygame.Surface):
            self.image = image
        else:
            raise ValueError("image harus berupa path string atau pygame.Surface")
        
        if scale:
            self.image = pygame.transform.scale(self.image, scale)


        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Posisi awal peluru
        self.direction = direction  # Arah tembakan (misalnya atas, bawah, kiri, kanan)
        self.speed = speed  # Kecepatan peluru
        self.damage = damage  # Damage yang diberikan peluru
        self.active = True  # Menyimpan status aktif peluru (terbentur atau tidak)
        self.is_player = is_player

    def update(self):
        # Update posisi peluru (bergerak sesuai arah)
        if self.active:
            self._move()
            if not self._on_screen():
                self.deactivate()

    def _move(self):
        # Menentukan gerakan peluru sesuai dengan arah
        dx, dy = self.direction
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    def _on_screen(self):
        screen_rect = pygame.display.get_surface().get_rect()
        return self.rect.colliderect(screen_rect)

    def check_collision(self, sprite_group):
        # Mengecek tabrakan dengan objek lain (misalnya musuh)
        return pygame.sprite.spritecollide(self, sprite_group, False)

    def hit(self):
        # Logika saat peluru terkena objek (misalnya musuh)
        self.explosion_sound = EXPLOSION_SOUND
        self.explosion_sound.play()
        self.deactivate()

    def deactivate(self):
        # Menonaktifkan peluru (misalnya ketika sudah keluar dari layar atau bertabrakan)
        self.active = False
        self.kill()
