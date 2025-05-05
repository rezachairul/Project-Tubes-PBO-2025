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
BULLET_ENEMY_FAST_IMAGE = 'assets/img/bullet_enemy.png'
BULLET_ENEMY_HORIZONTAL_IMAGE = 'assets/img/bullet_enemy.png'
BULLET_ENEMY_VERTICAL_IMAGE = 'assets/img/bullet_enemy.png'
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
enemy_fast_group = pygame.sprite.Group()
enemy_vertical_group = pygame.sprite.Group()
enemy_horizontal_group = pygame.sprite.Group()
enemy_bos_group = pygame.sprite.Group()

bullet_player_group = pygame.sprite.Group()
bullet_enemy_fast_group = pygame.sprite.Group()
bullet_enemy_vertical_group = pygame.sprite.Group()
bullet_enemy_horizontal_group = pygame.sprite.Group()
bullet_enemy_bos_group = pygame.sprite.Group()

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
        super().__init__()
        self.lives = 5
        self.score = 0
        # self.image, self.rect, dll

    def update(self):
        # Gerakan dan aksi lainnya
        pass

    def shoot(self):
        # Nembak peluru
        pass

    def hit(self):
        # Kena musuh
        pass

    def dead(self):
        # Kondisi kalau nyawa habis
        pass

    def respawn(self):
        # Muncul kembali setelah mati (kalau ada fitur respawn)
        pass

    def add_score(self, value):
        # Tambah skor
        pass

    def add_life(self):
        # Tambah nyawa (misal setelah tembak FastEnemy)
        pass



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
        super().__init__(health=1, score_value=100)

class HorizontalEnemy(BaseEnemy):
    def __init__(self):
        super().__init__(health=2, score_value=200)

class FastEnemy(BaseEnemy):
    def __init__(self):
        super().__init__(health=1, score_value=300)

class BosEnemy(BaseEnemy):
    def __init__(self):
        super().__init__(health=10, score_value=1000)



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


# === KELAS EXPLOSION (Ledakan) ===
"""
    - Class untuk efek ledakan saat musuh terkena peluru.
    - Memiliki beberapa frame untuk animasi ledakan
    - Membuat efek suara ledakan
"""
# Script Kelas Explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = None  # Gambar atau animasi ledakan
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Posisi ledakan
        self.life_duration = 12  # Durasi hidup ledakan (misalnya berapa frame)
        self.timer = 0  # Timer untuk menghitung durasi hidup ledakan

    def update(self):
        # Update ledakan (mengurangi durasi hidup)
        self._countdown()

    def _countdown(self):
        # Menurunkan timer dan menghapus ledakan setelah waktu habis
        pass

    def deactivate(self):
        # Menonaktifkan ledakan setelah selesai (misalnya setelah animasi selesai)
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
        self.running = True
        self.playing = False
        self.paused = False
        self.game_over = False

        self.font = pygame.font.SysFont('arial', 36)
        self.big_font = pygame.font.SysFont('arial', 72)

        self.background_stars = pygame.sprite.Group()
        for _ in range(100):  # Jumlah bintang latar
            star = BackgroundStar()
            self.background_stars.add(star)

    def start_screen(self):
        while not self.playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    self.playing = True

            GAME_SCREEN.fill((0, 0, 0))
            self.background_stars.update()
            self.background_stars.draw(GAME_SCREEN)

            title = self.big_font.render("Stars Warship", True, (255, 255, 255))
            start_text = self.font.render("Press any key to start", True, (255, 255, 255))
            GAME_SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
            GAME_SCREEN.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

    def update(self):
        pass

    def draw(self):
        pass

    def handle_events(self):
        pass

    def check_collision(self):
        pass

    def spawn_enemies(self):
        pass

    def shoot_bullets(self):
        pass

    def game_loop(self):
        while self.running:
            self.handle_events()

            if self.paused:
                self.pause_screen()
                continue

            if self.game_over:
                self.game_over_screen()
                continue

            self.update()
            self.draw()
            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

    def pause_screen(self):
        pause_text = self.font.render("Paused - Press P to resume", True, (255, 255, 255))
        while self.paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_p:
                    self.paused = False

            GAME_SCREEN.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.update()
            GAME_CLOCK.tick(10)

    def game_over_screen(self):
        GAME_OVER_SOUND.play()
        over_text = self.big_font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        self.__init__()
                        self.start_screen()
                        self.game_loop()
                    elif event.key == K_q:
                        pygame.quit()
                        sys.exit()

            GAME_SCREEN.fill((0, 0, 0))
            self.background_stars.update()
            self.background_stars.draw(GAME_SCREEN)

            GAME_SCREEN.blit(over_text, (SCREEN_WIDTH // 2 - over_text.get_width() // 2, SCREEN_HEIGHT // 3))
            GAME_SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()