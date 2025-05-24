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

from core.utils import bullet_player_group, explosion_group

from entities.BackgroundStar import *
from entities.Player import *
from entities.enemies import (
    VerticalEnemy,
    HorizontalEnemy,
    FastEnemy,
    BosEnemy
)

class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.paused = False
        self.game_over = False

        self.big_font = pygame.font.Font('assets/font/Gameplay.ttf', 72)
        self.medium_font = pygame.font.Font('assets/font/PixelGameFont.ttf', 36)
        self.small_font = pygame.font.Font('assets/font/HUTheGame.ttf', 26)

        self.bullet_player_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group() 
        self.player = Player(self.bullet_player_group, self.explosion_group, self)


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
        def draw_text_with_shadow(font, text, x, y, main_color, shadow_color=(0, 0, 0), offset=2):
            shadow = font.render(text, True, shadow_color)
            surface = font.render(text, True, main_color)
            GAME_SCREEN.blit(shadow, (x + offset, y + offset))
            GAME_SCREEN.blit(surface, (x, y))

        show_paused_demo = False
        show_move_demo = False
        last_mouse_pos = pygame.mouse.get_pos()

        while not self.playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.playing = True
                    elif event.key == K_p:
                        show_paused_demo = not show_paused_demo
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()


            GAME_SCREEN.fill((0, 0, 0))
            self.background_stars.update()
            self.background_stars.draw(GAME_SCREEN)

            # Judul
            title_text = "Stars Warship"
            title = self.big_font.render(title_text, True, (255, 255, 255))
            draw_text_with_shadow(self.big_font, title_text,
                                SCREEN_WIDTH // 2 - title.get_width() // 2,
                                SCREEN_HEIGHT // 4,
                                (255, 255, 255))

            # Teks berkedip
            if pygame.time.get_ticks() // 500 % 2 == 0:
                blink_text = "Press SPACE to start"
                blink = self.medium_font.render(blink_text, True, (255, 255, 0))
                GAME_SCREEN.blit(blink, (SCREEN_WIDTH // 2 - blink.get_width() // 2, SCREEN_HEIGHT // 2))

            # Instruksi
            instructions = [
                ("Use Mouse", " to move the player"),
                ("Press ", "ESC", " to pause the game"),
                ("Press ", "P", " to resume when paused")
            ]
            
            base_y = SCREEN_HEIGHT // 2 + 60
            line_spacing = 35

            for i, instr in enumerate(instructions):
                if len(instr) == 2:
                    text = self.small_font.render(instr[0] + instr[1], True, (255, 255, 255))
                    GAME_SCREEN.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, base_y + i * line_spacing))
                else:
                    pre, key, post = instr
                    pre_text = self.small_font.render(pre, True, (255, 255, 255))
                    key_text = self.small_font.render(key, True, (255, 255, 215))
                    post_text = self.small_font.render(post, True, (255, 255, 255))
                    
                    total_width = pre_text.get_width() + key_text.get_width() + post_text.get_width()
                    x = SCREEN_WIDTH // 2 - total_width // 2
                    y = base_y + i * line_spacing
                    
                    GAME_SCREEN.blit(pre_text, (x, y))
                    GAME_SCREEN.blit(key_text, (x + pre_text.get_width(), y))
                    GAME_SCREEN.blit(post_text, (x + pre_text.get_width() + key_text.get_width(), y))

            if show_paused_demo:
                pause_demo = self.small_font.render("Game Paused... Press P to resume", True, (255, 255, 100))
                GAME_SCREEN.blit(pause_demo, (SCREEN_WIDTH // 2 - pause_demo.get_width() // 2, base_y + line_spacing * 4))

            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)



    def update(self):
        self.background_stars.update()
        self.all_sprites.update()
        self.bullet_player_group.update()
        self.explosion_group.update()
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
        
        if self.boss_spawned and not self.boss.alive():
            self.boss_spawned = False
            self.player.score = 0  # atau sesuaikan logika jika tidak ingin reset score
            # Opsional: reset grup musuh
            for group in [enemy_vertical_group, enemy_horizontal_group, enemy_fast_group]:
                group.empty()

        
    def draw(self):
        GAME_SCREEN.fill((0, 0, 0))
        self.background_stars.draw(GAME_SCREEN)
        self.all_sprites.draw(GAME_SCREEN)
        self.bullet_player_group.draw(GAME_SCREEN)
        self.enemy_bullet_group.draw(GAME_SCREEN)
        self.explosion_group.draw(GAME_SCREEN)

         # Tampilan skor dan nyawa pakai font medium
        score_text = self.medium_font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.medium_font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        GAME_SCREEN.blit(score_text, (10, 10))
        GAME_SCREEN.blit(lives_text, (10, 50))

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
        # Cek peluru player vs musuh
        for bullet in self.bullet_player_group:
            hits = pygame.sprite.spritecollide(bullet, self.enemy_group, False)
            for enemy in hits:
                enemy.take_damage(bullet.damage)
                # bullet.kill()
                if enemy.health <= 0:
                    explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                    self.player.score += enemy.score_value
                    self.explosion_group.add(explosion)

                bullet.hit()          
        
        # Cek peluru musuh vs player
        if self.player.lives > 0: 
            hits = pygame.sprite.spritecollide(self.player, self.enemy_bullet_group, False)
            for bullet in hits:
                self.player.take_damage(bullet.damage)
                bullet.kill()

    # Batas jumlah musuh per jenis
    MAX_VERTICAL_ENEMIES = 5
    MAX_HORIZONTAL_ENEMIES = 3
    MAX_FAST_ENEMIES = 2

    def spawn_enemies(self):
        score = self.player.score

        # Cek apakah bos harus muncul
        if score >= 150 and not self.boss_spawned:
            enemy = BosEnemy(SCREEN_WIDTH // 2, 50)
            self.boss_spawned = True
            self.boss = enemy
            self.enemy_group.add(enemy)
            self.all_sprites.add(enemy)
            return

        # Tentukan jenis musuh yang akan muncul berdasarkan skor
        if score < 10:
            possible_types = ['vertical']
        elif score < 20:
            possible_types = ['vertical', 'horizontal']
        elif score < 30:
            possible_types = ['vertical', 'horizontal', 'fast']
        else:
            possible_types = ['vertical', 'horizontal', 'fast']

        random.shuffle(possible_types)

        for enemy_type in possible_types:
            if enemy_type == 'vertical' and len(enemy_vertical_group) < self.MAX_VERTICAL_ENEMIES:
                enemy = VerticalEnemy(random.randint(50, SCREEN_WIDTH - 50), 0)
                enemy_vertical_group.add(enemy)
                break
            elif enemy_type == 'horizontal' and len(enemy_horizontal_group) < self.MAX_HORIZONTAL_ENEMIES:
                enemy = HorizontalEnemy(0, random.randint(50, SCREEN_HEIGHT - 50))
                enemy_horizontal_group.add(enemy)
                break
            elif enemy_type == 'fast' and len(enemy_fast_group) < self.MAX_FAST_ENEMIES:
                enemy = FastEnemy(random.randint(50, SCREEN_WIDTH - 50), 0)
                enemy_fast_group.add(enemy)
                break
        else:
            return  # Tidak ada musuh yang bisa ditambahkan (semua penuh)

        self.enemy_group.add(enemy)
        self.all_sprites.add(enemy)
        sprite_group.add(enemy)


    # # Spwan Enemies
    # MAX_VERTICAL_ENEMIES = 5
    # MAX_HORIZONTAL_ENEMIES = 3
    # MAX_FAST_ENEMIES = 2
    # def spawn_enemies(self):
    #     # Batasi jumlah musuh aktif (kecuali saat bos aktif)
    #     if len(self.enemy_group) >= 10 or self.boss_spawned:
    #         return

    #     # Ambil posisi spawn acak
    #     x = random.randint(50, SCREEN_WIDTH - 50)
    #     y = random.randint(50, SCREEN_HEIGHT - 50)

    #     score = self.player.score  # Ambil skor pemain saat ini

    #     # Tentukan jenis musuh berdasarkan skor
    #     if score < 10:
    #         enemy_type = 'vertical'
    #     elif score < 20:
    #         enemy_type = random.choice(['vertical', 'horizontal'])
    #     elif score < 30:
    #         enemy_type = random.choice(['vertical', 'horizontal', 'fast'])
    #     elif score >= 200 and not self.boss_spawned:
    #         # Spawn bos jika belum pernah
    #         enemy = BosEnemy(SCREEN_WIDTH // 2, 50)
    #         self.boss_spawned = True
    #         self.boss = enemy
    #         self.enemy_group.add(enemy)
    #         self.all_sprites.add(enemy)
    #         return
    #     else:
    #         enemy_type = random.choice(['vertical', 'horizontal', 'fast'])

    #     # Inisialisasi musuh sesuai jenis
    #     if enemy_type == 'vertical':
    #         enemy = VerticalEnemy(x, y)
    #         enemy_vertical_group.add(enemy)
    #     elif enemy_type == 'horizontal':
    #         enemy = HorizontalEnemy(x, y)
    #         enemy_horizontal_group.add(enemy)
    #     elif enemy_type == 'fast':
    #         enemy = FastEnemy(x, y)
    #         enemy_fast_group.add(enemy)

    #     # Tambahkan musuh ke grup utama
    #     self.enemy_group.add(enemy)
    #     self.all_sprites.add(enemy)
    #     sprite_group.add(enemy)


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
            self.check_collision()
            self.draw()
            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

    # Pause Screen
    def pause_screen(self):
        pause_text = self.big_font.render("Paused", True, (255, 255, 255))
        pause_text = self.big_font.render("Press P to resume", True, (255, 255, 255))
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
        title = self.big_font.render("Are you sure Quit?", True, (255, 255, 255))
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
                        self.__init__()
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
        restart_text = self.medium_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        # Tambahkan skor terakhir
        final_score_text = self.medium_font.render(f"Your Score: {self.player.score}", True, (255, 255, 255))

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