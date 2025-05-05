# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import math        # Untuk operasi matematika seperti sin, cos, radians, dll (misalnya untuk gerakan melingkar)
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# === INISIALISASI GAME PYGAME ===
pygame.init()  # Wajib dipanggil sebelum menggunakan modul Pygame
pygame.display.set_caption('Stars Warship')  # Judul jendela game

# === KONFIGURASI LAYAR (Display Configuration) ===
infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.mouse.set_visible(True) # Ganti ke False klo dh siap game nya

# === PATH GAMBAR (Image Resources) ===
# Player & Enemies
PLAYER_IMAGE = 'assets/img/playership.png'
ENEMY_FAST_IMAGE = 'assets/img/enemy_fast.png'
ENEMY_HORIZONTAL_IMAGE = 'assets/img/enemy_horizontal.png'
ENEMY_VERTICAL_IMAGE = 'assets/img/enemy_vertical.png'
ENEMY_BOS_IMAGE = 'assets/img/enemy_bos.png'

# Bullet
BULLET_PLAYER_IMAGE = 'assets/img/bullet_player.png'
BULLET_ENEMY_FAST_IMAGE = 'assets/img/bullet_enemy_fast.png'
BULLET_ENEMY_HORIZONTAL_IMAGE = 'assets/img/bullet_enemy_horizontal.png'
BULLET_ENEMY_VERTICAL_IMAGE = 'assets/img/bullet_enemy_vertical.png'
BULLET_ENEMY_BOS_IMAGE = 'assets/img/bullet_enemy_bos.png'

# === SUARA / AUDIO (Sound Resources & Playback) ===
pygame.mixer.music.load('assets/sound/music.wav')
pygame.mixer.music.play(-1) # Loop backsound

# Sound Effect
EXPLOSION_SOUND = pygame.mixer.Sound('assets/sound/audio_explosion.wav')
BULLET_SOUND = pygame.mixer.Sound('assets/sound/audio_laser.wav')
GAME_OVER_SOUND = pygame.mixer.Sound('assets/sound/Game Over Theme.mp3')

# === FRAME CONTROL (Waktu & Kecepatan Game) ===
GAME_CLOCK = pygame.time.Clock()
GAME_FPS = 60 # Frames per second, untuk mengatur kelancaran game

# === SPRITE GROUPS (Kumpulan Objek/Game Entities) ===
background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
sideenemy_group = pygame.sprite.Group()

player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
sideenemy_bullet_group = pygame.sprite.Group()

explosion_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()

# === Kelas-kelas pada Game (Game Class) ===
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


# === KELAS PLAYER (Player Class) ===
"""
    Class untuk mengatur logika utama karakter pemain:
    - Pergerakan mengikuti mouse
    - Efek transparan saat respawn
    - Menembak peluru
    - Status hidup/mati & respawn
    - Buff: Shield (Perlindungan tambahan)
"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass

    def shoot(self):
        pass

    def dead(self):
        pass

    def respawn(self):
        pass


# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
"""
    - Class dasar untuk musuh.
    - Bisa digunakan sebagai vertical mover, horizontal mover, atau lainnya.
    - Mengatur posisi, gerakan, dan logika tembakan.
"""
class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self):
        self._move()
        self._shoot()

    def _move(self):
        pass
    
    def _shoot(self):
        pass

    def _fire_bullet(self):
        pass

# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak secara vertikal (atas/bawah).
    - Digunakan untuk musuh yang bergerak secara horizontal (kiri/kanan).
    - Digunakan untuk musuh yang bergerak dengan kecepatan tinggi.
    - Digunakan untuk musuh jenis bos dengan perilaku lebih kompleks.
    - Bisa memiliki pola gerakan dan tembakan yang lebih rumit.
'''
class VerticalEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()

class HorizontalEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()

class FastEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()

class BosEnemy(BaseEnemy):
    def __init__(self):
        super().__init__()


# === KELAS BULLET (Peluru) ===
"""
    - Peluru yang ditembakkan oleh musuh dan player.
    - Memiliki kecepatan dan ukuran tertentu
    - Membuat efek ledakan ketika mengenai target
"""
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass


# === KELAS EXPLOSION (Ledakan) ===
"""
    - Class untuk efek ledakan saat musuh terkena peluru.
    - Memiliki beberapa frame untuk animasi ledakan
    - Membuat efek suara ledakan
"""
# Script Kelas Explosion
class Explosion(pygame.sprite.Sprite):
    ANIMATION_DELAY = 12 # Delay antara frame animasi
    def __init__(self):
        pass

    def _load_image(self):
        pass

    def update(self):
        pass


# === KELAS GAME (Game Class) ===
"""
    Kelas utama untuk mengatur logika game:
    - Mengatur tampilan HUD (Heads Up Display) dan background
    - Menampilkan layar awal
    - Mengatur tampilan dan pergerakan musuh
    - Mengatur tampilan dan pergerakan player
    - Mengatur peluru
    - Mengatur skor dan nyawa
    - Mengatur tampilan game over
    - Mengatur tampilan pause
"""

class Game:
    def __init__(self):
        self.star_group = pygame.sprite.Group()
        for _ in range(100):  # Jumlah bintang
            star = BackgroundStar()     # Pastikan class BackgroundStar kamu udah siap
            self.star_group.add(star)

    def start_screen(self):
        print("Start screen ditampilkan")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            # Gambar latar belakang hitam
            GAME_SCREEN.fill((0, 0, 0))

            # Update & gambar bintang-bintang
            self.star_group.update()
            self.star_group.draw(GAME_SCREEN)

            # Tampilkan teks judul
            font = pygame.font.SysFont(None, 60)
            text_surface = font.render("Stars Warship", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            GAME_SCREEN.blit(text_surface, text_rect)

            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()