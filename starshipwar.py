# === IMPORT LIBRARY ===
import sys         # Untuk keluar dari game, contoh: sys.exit()
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import time        # Untuk delay (jika dibutuhkan)
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

# === INISIALISASI GAME PYGAME ===
pygame.init()  # Wajib dipanggil sebelum menggunakan modul Pygame
pygame.display.set_caption('Starship War')  # Judul jendela game

# === KONFIGURASI LAYAR (Display Configuration) ===
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Ukuran layar utama
pygame.mouse.set_visible(False)  # Sembunyikan kursor saat game berlangsung

# === KONSTANTA PATH GAMBAR (Image Resources) ===
PLAYER_IMAGE_PATH = 'Tubes/img/playership2.png'
ENEMY1_IMAGE_PATH = 'Tubes/img/enemy_1.png'
ENEMY2_IMAGE_PATH = 'Tubes/img/enemy_2.png'
SIDE_ENEMY_IMAGE_PATH = 'Tubes/img/enemy_3.png'

PLAYER_BULLET_IMAGE = 'Tubes/img/pbullet.png'
ENEMY_BULLET_IMAGE = 'Tubes/img/enemy_bullet.png'
SIDE_ENEMY_BULLET_IMAGE = 'Tubes/img/enemy_side_bullet.png'

# === SUARA / AUDIO (Sound Resources & Playback) ===
pygame.mixer.music.load('Tubes/sound/music.wav')
pygame.mixer.music.play(-1)  # Loop background music terus menerus

EXPLOSION_SOUND = pygame.mixer.Sound('Tubes/sound/audio_explosion.wav')
LASER_SOUND = pygame.mixer.Sound('Tubes/sound/audio_laser.wav')
GAME_OVER_SOUND = pygame.mixer.Sound('Tubes/sound/Game Over Theme.mp3')

# === FRAME CONTROL (Waktu & Kecepatan Game) ===
GAME_CLOCK = pygame.time.Clock()
GAME_FPS = 60  # Frames per second, untuk mengatur kelancaran game

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
sprite_group = pygame.sprite.Group()  # Jika ada pengelompokan semua objek nanti

# === KELAS-KELAS GAME (Game Classes) ===

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
        # Radius bintang acak: ukuran antara 1 atau 2 piksel (jadi tampak seperti bintang kecil)
        self.radius = random.randint(1, 2)
        # Gambar bintang berupa lingkaran putih kecil (dengan transparansi)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)        
        # Menentukan posisi awal secara acak di layar
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        # Kecepatan jatuh bintang secara acak, agar terlihat seperti kedalaman yang berbeda
        self.speed = random.uniform(0.5, 2.0)

    def update(self):
        self.rect.y += self.speed
        # Jika bintang melewati bawah layar, pindahkan ke atas secara acak
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.speed = random.uniform(0.5, 2.0)

# === KELAS PLAYER (Player Class) ===
"""
    Class untuk mengatur logika utama karakter pemain:
    - Pergerakan mengikuti mouse
    - Efek transparan saat respawn
    - Menembak peluru
    - Status hidup/mati & respawn
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey('black')  # Hitam jadi transparan
        self.rect = self.image.get_rect()
        # Status player
        self.alive = True
        self.count_to_live = 0 # Hitung mundur respawn
        self.activate_bullet = True
        self.alpha_duration = 0 # Durasi efek transparan

    def update(self):
        if self.alive:
            # Efek transparan pas respawn agar player tidak langsung ditembaki musuh
            self.image.set_alpha(70)
            self.alpha_duration += 1
            if self.alpha_duration > 170:
                self.image.set_alpha(255)
            # Gerakkan player ke posisi mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x = mouse_x - 12
            self.rect.y = mouse_y + 30

        else:
            # Saat player mati, tampilkan ledakan lalu delay respawn
            self.alpha_duration = 0
            explosion = Explosion(self.rect.x + 30, self.rect.y + 35)
            explosion_group.add(explosion)
            sprite_group.add(explosion)
            # Sembunyikan player keluar layar
            self.rect.y = SCREEN_HEIGHT + 200
            self.count_to_live += 1
            # Respawn jika waktu cukup
            if self.count_to_live > 80:
                self._respawn()

    def shoot(self):
        """
        Menembakkan peluru ke atas jika peluru aktif.
        Peluru keluar dari posisi mouse.
        """
        if self.activate_bullet:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Bullet(
                img='Tubes/img/pbullet.png',
                x=mouse_x + 10,
                y=mouse_y,
                speed=-10,
                group=player_bullet_group,
                size=(8, 20)
            )
            LASER_SOUND.play()      

    def dead(self):
        """ Mengatur status player mati dan mematikan peluru"""
        self.alive = False
        self.activate_bullet = False

    def _respawn(self):
        """ Mengatur status player hidup kembali dan mengaktifkan peluru """
        self.alive = True
        self.count_to_live = 0
        self.activate_bullet = True

# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
"""
    Class dasar untuk musuh.
    Bisa digunakan sebagai vertical mover, horizontal mover, atau lainnya.
    Mengatur posisi, gerakan, dan logika tembakan.
"""
class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, image_path, movement_type='vertical', shoot_interval=1500, speed=1, start_pos=None, size=(50, 50)):
        super().__init__()
        original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, size)
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
         # === Posisi awal ===
        if start_pos:
            self.rect.x, self.rect.y = start_pos
        else:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-500, 0)
        # === Parameter Pergerakan & Tembakan ===
        self.movement_type = movement_type
        self.speed = speed
        self.direction = 1
        self.shoot_interval = shoot_interval
        # self.bullet_type = 'enemy_bullet'
        self.last_shot_time = pygame.time.get_ticks() + random.randint(0, 1000)  # biar beda-beda
        
    def update(self):
        self._move()
        self._shoot()
    
    def _move(self):
        if self.movement_type == 'vertical':
            self.rect.y += self.speed
            if self.rect.y > SCREEN_HEIGHT:
                # Reset ke atas layar
                self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
                self.rect.y = random.randint(-150, -50)
        elif self.movement_type == 'horizontal-loop':
            self.rect.x += self.direction * self.speed
            if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
                self.direction *= -1
                self.rect.y += 40 # turun sedikit setiap belokan, biar kesannya 'ngedekat'

    def _shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time >= self.shoot_interval:
            self.last_shot_time = now
            # Tentukan peluru berdasarkan tipe gerakan
            if self.movement_type == 'horizontal-loop':
                self._fire_bullet(SIDE_ENEMY_BULLET_IMAGE, offset_x=-8, offset_y=10)
            else: # vertical
                self._fire_bullet(ENEMY_BULLET_IMAGE, offset_x=-0, offset_y=10)

    def _fire_bullet(self, image, offset_x=0, offset_y=10):
        # Menembakkan peluru dari posisi musuh"
        Bullet(
            img=image,
            x=self.rect.centerx + offset_x,
            y=self.rect.bottom + offset_y,
            speed=5,
            group=enemy_bullet_group
        )

# === KELAS BULLET (Peluru) ===
"""
Peluru yang ditembakkan oleh musuh.
- Memiliki kecepatan dan ukuran tertentu
- Membuat efek ledakan ketika mengenai target
"""
class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, group, size=(15, 30), center=False):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(img).convert_alpha(), size
        )
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

        if center:
            self.rect.center = (x, y)
        else:
            self.rect.x = x
            self.rect.y = y

        self.speed = speed

        group.add(self)
        sprite_group.add(self)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

# === KELAS EXPLOSION (Ledakan) ===
"""
    Class untuk efek ledakan saat musuh terkena peluru.
    - Memiliki beberapa frame untuk animasi ledakan
    - Membuat efek suara ledakan
"""
class Explosion(pygame.sprite.Sprite):
    ANIMATION_DELAY = 12  # Delay antara frame animasi
    def __init__(self, x, y, size=(120, 120)):
        super().__init__()
        self.img_list = [
            pygame.transform.scale(
                self._load_image(f'Tubes/img/exp{i}.png'), size
            )
            for i in range(1, 6)
        ]
        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.count_delay = 0
        EXPLOSION_SOUND.play()
    def _load_image(self, path):
        img = pygame.image.load(path).convert()
        img.set_colorkey('black')
        return img
    def update(self):
        self.count_delay += 1
        if self.count_delay >= self.ANIMATION_DELAY:
            self.count_delay = 0
            self.index += 1
            if self.index < len(self.img_list):
                self.image = self.img_list[self.index]
            else:
                self.kill()

# class (BaseEnemy):
class VerticalEnemy(BaseEnemy):
    def __init__(self, start_pos=None):
        super().__init__(ENEMY1_IMAGE_PATH, movement_type='vertical', speed=0.5, size=(50, 50), start_pos=start_pos)

class HorizontalEnemy(BaseEnemy):
    def __init__(self, start_pos=None):
        super().__init__(ENEMY2_IMAGE_PATH, movement_type='horizontal-loop', speed=1, size=(50, 50), start_pos=start_pos)

class FastEnemy(BaseEnemy):
    def __init__(self, start_pos=None):
        super().__init__(SIDE_ENEMY_IMAGE_PATH, movement_type='vertical', speed=1.5, size=(50, 50), start_pos=start_pos)

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
    # === INISIALISASI GAME ===
    def __init__(self):
        self.lives = 5
        self.score = 0
        self.count_hit_enemy1 = 0
        self.count_hit_enemy2 = 0
        self.count_hit_sideenemy = 0
        self.font = pygame.font.Font("Tubes/font/Pixeled.ttf", 50)
        self.star_group = pygame.sprite.Group()

    # === MENAMPILKAN TULISAN DI LAYAR AWAL ===
    def start_text(self):
        font = pygame.font.Font("Tubes/font/ModernAesthetic-Personal.otf", 90)
        title_surface = font.render('Starship War', True, pygame.Color('white'))
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        GAME_SCREEN.blit(title_surface, title_rect)
        font1 = pygame.font.Font("Tubes/font/ModernAesthetic-Personal.otf", 50)
        font2 = pygame.font.Font("Tubes/font/HUTheGame.ttf", 30)
        text1_surface = font1.render('Press Enter to Start', True, pygame.Color('white'))
        text2_surface = font2.render('KELOMPOK V', True, pygame.Color('white'))
        text1_rect = text1_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        text2_rect = text2_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))
        GAME_SCREEN.blit(text1_surface, text1_rect)
        GAME_SCREEN.blit(text2_surface, text2_rect)

    # === MENAMPILKAN LAYAR AWAL ===
    def start_screen(self):
        sprite_group.empty()
        while True:
            GAME_SCREEN.fill((0, 0, 0))
            self.start_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        self.run_game()
            pygame.display.update()

    # === MENAMPILKAN GAME OVER ===
    def game_over(self):
        pygame.mixer.music.stop()
        GAME_OVER_SOUND.play()
        red = pygame.Color(255, 0, 0)
        white = pygame.Color(255, 255, 255)
        # "GAME OVER"
        font_big = pygame.font.Font("Tubes/font/SquareGame.otf", 90)
        game_over_surface = font_big.render('GAME OVER', True, red)
        game_over_rect = game_over_surface.get_rect(midtop=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        # Skor akhir
        font_score = pygame.font.Font("Tubes/font/SquareGame.otf", 40)
        score_surface = font_score.render(f'Final Score: {self.score}', True, white)
        score_rect = score_surface.get_rect(midtop=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        # Instruksi lanjut
        font_small = pygame.font.Font("Tubes/font/SquareGame.otf", 30)
        info_surface = font_small.render('Press SPACE to return to Start', True, white)
        info_rect = info_surface.get_rect(midtop=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))

        while True:
            GAME_SCREEN.fill((0, 0, 0))
            GAME_SCREEN.blit(game_over_surface, game_over_rect)
            GAME_SCREEN.blit(score_surface, score_rect)
            GAME_SCREEN.blit(info_surface, info_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        self.start_screen()

            pygame.display.update()

    # === MENAMPILKAN LAYAR PAUSE ===
    def pause_screen(self):
        pygame.mixer.music.stop()
        paused = True
        font = pygame.font.Font("Tubes/font/ModernAesthetic-Personal.otf", 70)
        pause_surface = font.render("PAUSED", True, pygame.Color('white'))
        pause_rect = pause_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        while paused:
            GAME_SCREEN.blit(pause_surface, pause_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.mixer.music.play(-1)
                    paused = False

    # === MENAMPILKAN BACKGROUND ===
    def create_background(self):
        for _ in range(20):
            star = BackgroundStar()
            self.star_group.add(star)
            sprite_group.add(star)

    # === MENAMPILKAN PLAYER ===
    def create_player(self):
        self.player = Player("Tubes/img/playership2.png")
        sprite_group.add(self.player)

    # === MENAMPILKAN ENEMY ===
    def create_enemy(self):
        for _ in range(7):
            enemy = VerticalEnemy(start_pos=(random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))
            sprite_group.add(enemy)
            enemy_group.add(enemy)

    def create_sideenemy(self):
        sideenemy = FastEnemy()
        sprite_group.add(sideenemy)
        sideenemy_group.add(sideenemy)

    def create_enemy2(self):
        for _ in range(3):
            enemy2 = HorizontalEnemy(start_pos=(random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))
            sprite_group.add(enemy2)
            enemy2_group.add(enemy2)

    def handle_player_collision(self, enemy_group, reset_position, death_penalty=True):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemy_group, False)
            if hits:
                for enemy in hits:
                    enemy.rect.x, enemy.rect.y = reset_position()
                if death_penalty:
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        self.game_over()

    # === MENAMPILKAN COLLISION PELURU ===
    def handle_bullet_collision(self, enemy_group, count_attr, threshold, score_inc, explosion_offset, reset_func):
        hits = pygame.sprite.groupcollide(enemy_group, player_bullet_group, False, True)
        for enemy in hits:
            setattr(self, count_attr, getattr(self, count_attr) + 1)
            if getattr(self, count_attr) >= threshold:
                expl_x = enemy.rect.x + explosion_offset[0]
                expl_y = enemy.rect.y + explosion_offset[1]
                explosion = Explosion(expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)
                enemy.rect.x, enemy.rect.y = reset_func()
                setattr(self, count_attr, 0)
                self.score += score_inc

    # === MENAMPILKAN COLLISION PELURU MUSUH ===
    def enemybullet_hits_player(self):
        hits = pygame.sprite.spritecollide(self.player, enemy_bullet_group, True)
        if hits and self.player.image.get_alpha() == 255:
            self.lives -= 1
            self.player.dead()
            if self.lives < 0:
                self.game_over()

    def sideenemy_hits_player(self):
        hits = pygame.sprite.spritecollide(self.player, sideenemy_bullet_group, True)
        if hits and self.player.image.get_alpha() == 255:
            self.lives -= 1
            self.player.dead()
            if self.lives < 0:
                self.game_over()

    # === MENAMPILKAN HUD (Heads Up Display) ===
    def display_hud(self):
        white = pygame.Color(255, 255, 255)
        small_font = pygame.font.SysFont("Arial", 24)  # lebih kecil dari sebelumnya
        
        lives_text = small_font.render("Lives: " + str(self.lives), True, white)
        score_text = small_font.render("Score: " + str(self.score), True, white)

        # Tampilkan di pojok kiri atas dengan jarak yang pas
        GAME_SCREEN.blit(lives_text, (10, 10))
        GAME_SCREEN.blit(score_text, (10, 40))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(LASER_SOUND)
                self.player.shoot()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.pause_screen()

    def run_collisions(self):
        self.handle_bullet_collision(enemy_group, 'count_hit_enemy1', 3, 10, (50, 50), lambda: (random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))
        self.handle_bullet_collision(sideenemy_group, 'count_hit_sideenemy', 15, 30, (60, 50), lambda: (-60, random.randrange(0, SCREEN_HEIGHT - 50)))
        self.handle_bullet_collision(enemy2_group, 'count_hit_enemy2', 5, 20, (50, 50), lambda: (random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))

        self.enemybullet_hits_player()
        self.sideenemy_hits_player()

        self.handle_player_collision(enemy_group, lambda: (random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))
        self.handle_player_collision(sideenemy_group, lambda: (-60, random.randrange(0, SCREEN_HEIGHT - 50)))
        self.handle_player_collision(enemy2_group, lambda: (random.randrange(0, SCREEN_WIDTH), random.randrange(-50, -10)))

    def run_update(self):
        sprite_group.update()
        sprite_group.draw(GAME_SCREEN)

    def run_game(self):
        self.create_background()
        self.create_player()
        self.create_enemy()
        self.create_sideenemy()
        self.create_enemy2()

        while True:
            GAME_SCREEN.fill('black')
            self.handle_events()
            self.run_collisions()
            self.display_hud()
            self.run_update()
            pygame.display.update()
            GAME_CLOCK.tick(GAME_FPS)

# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()
#========================================================================================