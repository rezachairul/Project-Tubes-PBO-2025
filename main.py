# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
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
pygame.mouse.set_visible(True) # Ganti ke false klo dh siap game nya

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

# === Kelas-kelas pada Game (Game Class) ===




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
        pass

    def start_screen(self):
        print("Start screen ditampilkan")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            # Gambar latar belakang warna hitam
            GAME_SCREEN.fill((0, 0, 0))

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