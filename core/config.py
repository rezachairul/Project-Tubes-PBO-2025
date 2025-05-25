# core/config.py

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN

# === INISIALISASI GAME PYGAME ===
pygame.init()  # Wajib dipanggil sebelum menggunakan modul Pygame
pygame.display.set_caption('Stars Warship')  # Judul jendela game

# === KONFIGURASI LAYAR (Display Configuration) ===
infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.mouse.set_visible(False) # Ganti ke False klo dh siap game nya

# === FRAME CONTROL (Waktu & Kecepatan Game) ===
GAME_CLOCK = pygame.time.Clock()
GAME_FPS = 60 # Frames per second, untuk mengatur kelancaran game