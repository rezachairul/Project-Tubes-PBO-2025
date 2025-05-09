# class/Bullet.py

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# import module



# === KELAS BULLET (Peluru) ===
"""
    - Peluru yang ditembakkan oleh musuh dan player.
    - Memiliki kecepatan dan ukuran tertentu
    - Membuat efek ledakan ketika mengenai target
"""
# === KELAS BULLET (Peluru) ===
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, damage):
        super().__init__()
        self.image = None  # Gambar peluru (akan diubah sesuai jenisnya)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Posisi awal peluru
        self.direction = direction  # Arah tembakan (misalnya atas, bawah, kiri, kanan)
        self.speed = speed  # Kecepatan peluru
        self.damage = damage  # Damage yang diberikan peluru
        self.active = True  # Menyimpan status aktif peluru (terbentur atau tidak)

    def update(self):
        # Update posisi peluru (bergerak sesuai arah)
        self._move()

    def _move(self):
        # Menentukan gerakan peluru sesuai dengan arah
        pass

    def check_collision(self, sprite_group):
        # Mengecek tabrakan dengan objek lain (misalnya musuh)
        pass

    def hit(self):
        # Logika saat peluru terkena objek (misalnya musuh)
        pass

    def deactivate(self):
        # Menonaktifkan peluru (misalnya ketika sudah keluar dari layar atau bertabrakan)
        pass
