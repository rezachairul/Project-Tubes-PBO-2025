# core/game.py

# === IMPORT LIBRARY ===
import sys                  # Untuk keluar dari game, contoh: sys.exit()
import pygame               # Library utama untuk membuat game
import random               # Library untuk membuat acak
from pygame.locals import * # Import konstanta pygame seperti QUIT, KEYDOWN, dll

from core.config import GAME_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_CLOCK, GAME_FPS
from core.utils import *
from core.resources import *
from core.game import *

from core.utils import bullet_player_group

from entities.BackgroundStar import *
from entities.Player import *
from entities.enemies import (
    VerticalEnemy,
    HorizontalEnemy,
    FastEnemy,
    BosEnemy
)

class Game:
    def _init_(self):
        self.running = True
        self.playing = False
        self.paused = False
        self.game_over = False

        self.big_font = pygame.font.Font('assets/font/Gameplay.ttf', 72)
        self.medium_font = pygame.font.Font('assets/font/PixelGameFont.ttf', 36)
        self.small_font = pygame.font.Font('assets/font/HUTheGame.ttf', 18)

        self.bullet_player_group = pygame.sprite.Group()
        self.player = Player(self.bullet_player_group)


        # === Background Star ===
        self.background_stars = pygame.sprite.Group()
        for _ in range(100):  # Jumlah bintang latar
            star = BackgroundStar()
            self.background_stars.add(star)

        # === Player ===
        # self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # === Enemies ===
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.all_sprites.add(*self.enemy_group)
        # Inisialisasi waktu spawn terakhir
        self.last_spawn_time = pygame.time.get_ticks()

        # === Kontrol Tahapan Musuh Berdasarkan Skor ===
        self.current_stage = 0             # Tahapan saat ini (0: awal, 1: setelah skor 1000, dst)
        self.boss_spawned = False          # Bos sudah muncul atau belum
        self.boss_defeated = False         # Bos sudah dikalahkan atau belum
        self.boss = None                   # Simpan bos aktif saat ini (kalau ada)


    # Start Screen
    def start_screen(self):
        while not self.playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.playing = True

            GAME_SCREEN.fill((0, 0, 0))
            self.background_stars.update()
            self.background_stars.draw(GAME_SCREEN)

            title = self.big_font.render("Stars Warship", True, (255, 255, 255))
            start_text = self.small_font.render("Press SPACE to start", True, (255, 255, 255))
            GAME_SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
            GAME_SCREEN.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

    def update(self):
        self.background_stars.update()
        self.all_sprites.update()
        self.bullet_player_group.update()
        now = pygame.time.get_ticks()
        
        # Kosongkan dulu grup peluru musuh
        self.enemy_bullet_group.empty()

        # Ambil peluru dari setiap musuh
        for enemy in self.enemy_group:
            enemy.bullets.update()
            self.enemy_bullet_group.add(enemy.bullets)

        now = pygame.time.get_ticks()
        if now - self.last_spawn_time > 2000:  # setiap 2 detik
            self.spawn_enemies()
            self.last_spawn_time = now
        
    def draw(self):
        GAME_SCREEN.fill((0, 0, 0))
        self.background_stars.draw(GAME_SCREEN)
        self.all_sprites.draw(GAME_SCREEN)
        self.bullet_player_group.draw(GAME_SCREEN)
        self.enemy_bullet_group.draw(GAME_SCREEN)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.paused = not self.paused
                elif event.key == K_ESCAPE:
                    self.confirm_quit_screen()
            elif event.type == MOUSEBUTTONDOWN:
                self.player.shoot()

    def check_collision(self):
        pass

    # def spawn_enemies(self):
    #     if len(self.enemy_group) < 6: # spawn 6 enemies at a time
    #         enemy_type = random.choice(['vertical', 'horizontal', 'fast', 'bos'])
    #         x = random.randint(50, SCREEN_WIDTH - 50)
    #         y = random.randint(50, SCREEN_HEIGHT - 50)

    #         if enemy_type == 'vertical':
    #             enemy = VerticalEnemy(x, y)
    #             enemy_vertical_group.add(enemy)
    #         elif enemy_type == 'horizontal':
    #             enemy = HorizontalEnemy(x, y)
    #             enemy_horizontal_group.add(enemy)
    #         elif enemy_type == 'fast':
    #             enemy = FastEnemy(x, y)
    #             enemy_fast_group.add(enemy)
    #         elif enemy_type == 'bos':
    #             enemy = BosEnemy(x, y)
    #             enemy_bos_group.add(enemy)
        
    #         # === Tambahkan ke semua grup utama ===
    #         self.enemy_group.add(enemy)
    #         self.all_sprites.add(enemy)
    #         sprite_group.add(enemy)

    def spawn_enemies(self):
        # Batasi jumlah musuh aktif (kecuali saat bos aktif)
        if len(self.enemy_group) >= 6 or self.boss_spawned:
            return

        # Ambil posisi spawn acak
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)

        score = self.player.score  # Ambil skor pemain saat ini

        # Tentukan jenis musuh berdasarkan skor
        if score < 250:
            enemy_type = 'vertical'
        elif score < 500:
            enemy_type = random.choice(['vertical', 'horizontal'])
        elif score < 1000:
            enemy_type = random.choice(['vertical', 'horizontal', 'fast'])
        elif score >= 1000 and not self.boss_spawned:
            # Spawn bos jika belum pernah
            enemy = BosEnemy(SCREEN_WIDTH // 2, 50)
            self.boss_spawned = True
            self.boss = enemy
            self.enemy_group.add(enemy)
            self.all_sprites.add(enemy)
            return
        else:
            enemy_type = random.choice(['vertical', 'horizontal', 'fast'])

        # Inisialisasi musuh sesuai jenis
        if enemy_type == 'vertical':
            enemy = VerticalEnemy(x, y)
            enemy_vertical_group.add(enemy)
        elif enemy_type == 'horizontal':
            enemy = HorizontalEnemy(x, y)
            enemy_horizontal_group.add(enemy)
        elif enemy_type == 'fast':
            enemy = FastEnemy(x, y)
            enemy_fast_group.add(enemy)

        # Tambahkan musuh ke grup utama
        self.enemy_group.add(enemy)
        self.all_sprites.add(enemy)
        sprite_group.add(enemy)


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

    # Pause Screen
    def pause_screen(self):
        pause_text = self.small_font.render("Paused - Press P to resume", True, (255, 255, 255))
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

    
    # Game Confirm Quit Screen
    def confirm_quit_screen(self):
        title = self.big_font.render("Are you sure?", True, (255, 255, 255))
        restart_text = self.medium_font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = self.medium_font.render("Press Q to Quit", True, (255, 255, 255))

        confirming = True
        while confirming:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        self._init_()
                        self.start_screen()
                        self.game_loop()
                    elif event.key == K_q:
                        pygame.quit()
                        sys.exit()

            GAME_SCREEN.fill((0, 0, 0))
            self.background_stars.update()
            self.background_stars.draw(GAME_SCREEN)

            GAME_SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3))
            GAME_SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
            GAME_SCREEN.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 60))

            pygame.display.update()
            GAME_CLOCK.tick(30)


    # Game Over Screen
    def game_over_screen(self):
        GAME_OVER_SOUND.play()
        over_text = self.big_font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.small_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_r:
                        self._init_()
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