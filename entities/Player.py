# class/Player.py

# === IMPORT LIBRARY ===
import random      # Untuk angka atau pemilihan acak, misal spawn musuh/peluru
import pygame      # Library utama untuk membuat game
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

from core.utils import bullet_player_group, explosion_group
from core.resources import BULLET_SOUND, EXPLOSION_SOUND, GAME_OVER_SOUND, BULLET_PLAYER_IMAGE

from entities.Bullet import Bullet
from entities.Explosion import Explosion

# === KELAS PLAYER (Player Class) ===
"""
    Class untuk mengatur logika utama karakter pemain:
    - Pergerakan mengikuti mouse
    - Efek transparan saat respawn
    - Menembak peluru
    - Status hidup/mati & respawn
    - Buff: Shield (Perlindungan tambahan jika bisa kalahin 1 fast enemy) + Add Shoot (bisa nambah 1 tembakan (maks 3) jika bisa kalahin 1 bos)
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group, explosion_group, game):
        super().__init__()
        self.image_original = pygame.image.load('assets/img/playership.png').convert_alpha()
        self.image_original = pygame.transform.scale(self.image_original, (50, 50))

        self.image_shield = pygame.image.load('assets/img/player_with_shield.png').convert_alpha()
        self.image_shield = pygame.transform.scale(self.image_shield, (50, 50))

        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(400, 500))

        # self.rect = self.image.get_rect(center=(400, 500))
        self.explosion_group = explosion_group
        self.dead_animating = False

        self.game = game

        self.lives = 5
        self.score = 0
        self.shield = False
        self.max_shoot = 1
        self.current_shoot = 1
        self.bullet_group = bullet_group

        # Invulnerability
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.respawn_duration = 3000  # ms

        # Auto-invulnerability (buff ketika skor >= 500)
        self.auto_invulnerable = False
        self.auto_invul_start = 0
        self.auto_invul_duration = random.randint(5000, 10000)

        # Kedip-kedip efek
        self.visible = True
        self.blink_timer = 0
        self.blink_interval = 200  # ms

    def update(self):
        if self.dead_animating:
            # Tunggu sampai animasi ledakan selesai (tidak ada explosion)
            if len(self.explosion_group) == 0:
                self.dead_animating = False
                self.respawn()
            return  # skip update lain saat dead animasi
        
        # Ganti gambar berdasarkan status shield
        if self.shield:
            self.image = self.image_shield
            print("Shield ON")
        else:
            self.image = self.image_original

        # Ikuti mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y

        now = pygame.time.get_ticks()

        if self.invulnerable:
            # Blinking effect
            if now - self.blink_timer > self.blink_interval:
                self.blink_timer = now
                self.visible = not self.visible
                if self.visible:
                    self.image.set_alpha(128)
                else:
                    self.image.set_alpha(0)

            # Akhir invul berdasarkan tipe
            if self.auto_invulnerable:
                if now - self.auto_invul_start > self.auto_invul_duration:
                    self.auto_invulnerable = False
                    self.invulnerable = False
                    self.image.set_alpha(255)
            else:
                if now - self.invulnerable_timer > self.respawn_duration:
                    self.invulnerable = False
                    self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)

    def shoot(self):
        if self.lives <= 0 or self.dead_animating:
            return  # Tidak bisa menembak saat mati atau sedang animasi mati
        
        # Tambah peluru ke grup sesuai jumlah tembakan aktif
        for i in range(self.current_shoot):
            # bullet = Bullet(self.rect.centerx + (i - self.current_shoot // 2) * 10, self.rect.top)
            bullet = Bullet(
                x=self.rect.centerx + (i - self.current_shoot // 2) * 10,
                y=self.rect.top,
                direction=(0, -1),
                speed=10,
                damage=1,
                image=BULLET_PLAYER_IMAGE,
                is_player=True
            )
            self.bullet_group.add(bullet)
        BULLET_SOUND.play()

    def take_damage(self, damage=1):
        self.hit()

    def hit(self):
        if self.invulnerable:
            return

        if self.shield:
            self.shield = False
        else:
            self.lives -= 1
            EXPLOSION_SOUND.play()
            self.dead()

    def dead(self):
        if self.lives <= 0:
            self.game.game_over = True 
        self.dead_animating = True
        # Tambah animasi ledakan di posisi player
        explosion = Explosion(self.rect.centerx, self.rect.centery)
        self.explosion_group.add(explosion)
        self.image.set_alpha(0)  # sembunyikan player saat ledakan
        GAME_OVER_SOUND.play()

    def respawn(self):
        self.rect.center = (400, 500)
        self.invulnerable = True
        self.invulnerable_timer = pygame.time.get_ticks()
        self.blink_timer = pygame.time.get_ticks()

    def add_score(self, value):
        self.score += value
        if self.score >= 500 and not self.auto_invulnerable:
            self.activate_auto_invul()

    def add_life(self):
        self.lives += 1

    def gain_shield(self):
        self.shield = True

    def upgrade_shoot(self):
        if self.current_shoot < 3:
            self.current_shoot += 1
    
    def activate_auto_invul(self):
        self.auto_invulnerable = True
        self.invulnerable = True
        self.auto_invul_start = pygame.time.get_ticks()
        self.blink_timer = pygame.time.get_ticks()
        self.image.set_alpha(128)