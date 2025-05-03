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
pygame.mouse.set_visible(False)

# === PATH GAMBAR (Image Resources) ===
# Player & Enemies
PLAYER_IMAGE = ''
ENEMY_FAST_IMAGE = ''
ENEMY_HORIZONTAL_IMAGE = ''
ENEMY_VERTICAL_IMAGE = ''
ENEMY_BOS_IMAGE = ''

# Bullet
BULLET_PLAYER_IMAGE = ''
BULLET_ENEMY_FAST_IMAGE = ''
BULLET_ENEMY_HORIZONTAL_IMAGE = ''
BULLET_ENEMY_VERTICAL_IMAGE = ''
BULLET_ENEMY_BOS_IMAGE = ''

# === SUARA / AUDIO (Sound Resources & Playback) ===
pygame.mixer.music.load('')
pygame.mixer.music.play(-1) # Loop backsound

# Sound Effect
EXPLOSION_SOUND = pygame.mixer.Sound('')
BULLET_SOUND = pygame.mixer.Sound('')
GAME_OVER_SOUND = pygame.mixer.Sound('')

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


# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()