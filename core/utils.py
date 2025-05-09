# core/utils.py

# === IMPORT LIBRARY ===
import pygame      # Library utama untuk membuat game


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
