# core/game.py

# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

from core.config import GAME_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_CLOCK, GAME_FPS
from core.utils import *
from core.resources import *
from core.game import *

from entities import *
from entities.enemies import *

class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.paused = False
        self.game_over = False

        self.font = pygame.font.SysFont('arial', 36)
        self.big_font = pygame.font.SysFont('arial', 72)

        # === Background Star ===
        self.background_stars = pygame.sprite.Group()
        for _ in range(100):  # Jumlah bintang latar
            star = BackgroundStar()
            self.background_stars.add(star)

        # === Player ===
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

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
        self.background_stars.update()
        self.all_sprites.update()

    def draw(self):
        GAME_SCREEN.fill((0, 0, 0))
        self.background_stars.draw(GAME_SCREEN)
        self.all_sprites.draw(GAME_SCREEN)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.paused = not self.paused
            elif event.type == MOUSEBUTTONDOWN:
                self.player.shoot()

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