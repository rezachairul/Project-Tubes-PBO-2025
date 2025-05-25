# core/resources.py

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game

# === PATH GAMBAR (Image Resources) ===
# Player & Enemies
PLAYER_IMAGE = 'assets/img/playership.png'
PLAYER_IMAGE_SHIELD = 'assets/img/player_with_shield.png'
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
pygame.mixer.music.load('assets/sound/music-alien.mp3')
pygame.mixer.music.play(-1) # Loop backsound

# Sound Effect
EXPLOSION_SOUND = pygame.mixer.Sound('assets/sound/audio_explosion.wav')
BULLET_SOUND = pygame.mixer.Sound('assets/sound/audio_laser.wav')
GAME_OVER_SOUND = pygame.mixer.Sound('assets/sound/Game Over Theme.mp3')