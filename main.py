#Tubes PBO
# Kelompok V

#===============================================================================

# from email.mime import image # import image


import sys # Untuk keluar dari program
import random # Digunakan untuk memilih angka/lokasi acak (spawn musuh, peluru, dll)
import time # Untuk jeda waktu, jika dibutuhkan
import pygame # Pustaka utama untuk membuat game
from pygame.locals import * # Import konstanta dari pygame (misal QUIT, KEYDOWN, K_LEFT, dst)
 
pygame.init() # Wajib dipanggil sebelum memakai modul-modul pygame

# Set judul window
pygame.display.set_caption('Starship War')  # Menampilkan judul game di jendela

# string path ke file gambar
player_ship = 'Tubes/img/playership2.png' 
enemy_ship = 'Tubes/img/enemy_1.png'
enemy2_ship = 'Tubes/img/enemy_2.png'
sideenemy_ship = 'Tubes/img/enemy_3.png'
player_bullet = 'Tubes/img/pbullet.png'
enemy_bullet = 'Tubes/img/enemy_bullet.png'
sideenemy_bullet = 'Tubes/img/enemy_side_bullet.png'

# Load dan play background music + efek suara
music = pygame.mixer.music.load('Tubes/sound/music.wav')
pygame.mixer.music.play(-1)
exp_sound = pygame.mixer.Sound('Tubes/sound/audio_explosion.wav')
laser_sound = pygame.mixer.Sound('Tubes/sound/audio_laser.wav') 
gameover_sound = pygame.mixer.Sound('Tubes/sound/Game Over Theme.mp3')

# set the screen size
# screen = pygame.display.set_mode((0,0), FULLSCREEN)
screen = pygame.display.set_mode((pygame.display.Info().current_w - 100, pygame.display.Info().current_h - 100)) 
s_width, s_height = screen.get_size()

# initialize clock
clock = pygame.time.Clock() 
FPS = 60 

# Buat sprite groups
background_group = pygame.sprite.Group() 
player_group = pygame.sprite.Group() 
enemy_group = pygame.sprite.Group() 
sideenemy_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
playerbullet_group = pygame.sprite.Group()
enemybullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
sideenemybullet_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()

# set the mouse cursor to invisible
pygame.mouse.set_visible(False)
 
class Background(pygame.sprite.Sprite): # class for the background
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.Surface([x,y])
        self.image.fill('white')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

 
    def update(self):
        self.rect.y += 1
        self.rect.x += 1 
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)
         
class player(pygame.sprite.Sprite): # class for the player
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')
        self.alive = True
        self.count_to_live = 0
        self.activate_bullet = True
        self.alpha_duration = 0
  

    def update(self):
        if self.alive:
            self.image.set_alpha(70)
            self.alpha_duration += 1
            if self.alpha_duration > 170:
                self.image.set_alpha(255)
            mouse = pygame.mouse.get_pos()
            self.rect.x = mouse[0] - 12
            self.rect.y = mouse[1] + 30
        else:
            self.alpha_duration = 0
            expl_x = self.rect.x + 30
            expl_y = self.rect.y + 35
            explosion = Explosion(expl_x, expl_y)
            explosion_group.add(explosion)
            sprite_group.add(explosion)
            pygame.time.delay(10)
            self.rect.y = s_height + 200
            self.count_to_live += 1
            if self.count_to_live > 80:
                self.alive = True
                self.count_to_live=0
                self.activate_bullet = True
     
    def shoot(self): # shoot the bullet
        if self.activate_bullet:
            bullet = PlayerBullet('Tubes/img/pbullet.png')
            mouse = pygame.mouse.get_pos()
            bullet.rect.x = mouse[0] + 10
            bullet.rect.y = mouse[1]
            playerbullet_group.add(bullet)
            sprite_group.add(bullet)

    def dead(self): # when the player is dead
        self.alive = False
        self.activate_bullet = False

class Enemy(player): # class for the enemy
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, s_width)
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self): # update the enemy
        self.rect.y += 1
        if self.rect.y > s_height:
            self.rect.x = random.randrange(0, s_width)
            self.rect.y = random.randrange(-2000, 0)
        self.shoot()

    def shoot(self): # shoot the bullet
        if self.rect.y in (0, 50, 200, 400):
            enemybullet = EnemyBullet('Tubes/img/enemy_bullet.png')
            enemybullet.rect.x = self.rect.x + 25
            enemybullet.rect.y = self.rect.y + 35
            enemybullet_group.add(enemybullet)
            sprite_group.add(enemybullet)

class SideEnemy(Enemy): # class for the side enemy
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = -200
        self.rect.y = 200
        self.move = 1

    def update(self): # update the side enemy
        self.rect.x += self.move
        if self.rect.x > s_width + 200:
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1
        self.shoot()

    def shoot(self):
        if self.rect.x % 100 == 0:
            sideenemybullet = EnemyBullet('Tubes/img/enemy_side_bullet.png')
            sideenemybullet.rect.x = self.rect.x + 50
            sideenemybullet.rect.y = self.rect.y + 60
            sideenemybullet_group.add(sideenemybullet)
            sprite_group.add(sideenemybullet)

class Enemy2(player):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, s_width)
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += 1
        if self.rect.y > s_height:
            self.rect.x = random.randrange(0, s_width)
            self.rect.y = random.randrange(-2000, 0)
        self.shoot()

    def shoot(self):
        if self.rect.y in (0, 50,200, 400, 600):
            enemybullet = EnemyBullet(enemy_bullet)
            enemybullet.rect.x = self.rect.x + 25
            enemybullet.rect.y = self.rect.y + 35
            enemybullet_group.add(enemybullet)
            sprite_group.add(enemybullet)

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')
        self.alive = True

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

class EnemyBullet(PlayerBullet):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y += 3
        if self.rect.y > s_height:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img_list = []
        for i in range(1, 6):
            img = pygame.image.load(f'Tubes/img/exp{i}.png').convert()
            img.set_colorkey('black')
            img = pygame.transform.scale(img, (120,120))
            self.img_list.append(img)
        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.count_delay = 0
        

    def update(self):
        exp_sound.play()
        self.count_delay += 1
        if self.count_delay >= 12:
            if self.index < len(self.img_list) - 1:
                self.count_delay = 0
                self.index += 1
                self.image = self.img_list[self.index]
        if self.index >= len(self.img_list) - 1:
            if self.count_delay >= 12:
                self.kill()


class Game:
    def __init__(self):
        self.count_hit = 0
        self.count_hit2 = 0
        self.lives = 3
        self.score = 0
        self.font = pygame.font.Font('Tubes/font/Pixeled.ttf',25)
        self.start_screen()

    def start_text(self):
        font = pygame.font.Font('Tubes/font/ModernAesthetic-Personal.otf', 150)
        text = font.render('STARSHIP WAR', True, 'white')
        text_rect = text.get_rect(center=(s_width/2, s_height/2-80))
        screen.blit(text, text_rect)
        font1 = pygame.font.Font('Tubes/font/ModernAesthetic-Personal.otf', 50)
        font2 = pygame.font.Font('Tubes/font/ModernAesthetic-Personal.otf', 25)
        text1 = font1.render('Click ENTER', True, 'grey')
        text2 = font2.render('KELOMPOK V', True, 'white')
        text1_rect = text1.get_rect(center=(s_width/2, s_height/2+75))
        text2_rect = text2.get_rect(center=(s_width/2, s_height/2+350))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

    def start_screen(self):
        sprite_group.empty()
        while True: 
            screen.fill('black')
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
 
    def pause_text(self):
        font = pygame.font.Font('Tubes/font/ModernAesthetic-Personal.otf', 100)
        text = font.render('PAUSE GAME', True, 'orange')
        text_rect = text.get_rect(center=(s_width/2, s_height/2))
        screen.blit(text, text_rect)
 
    def pause_screen(self):
        self.__init_create = False
        while True: 
            self.pause_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
 
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == K_SPACE:
                        self.run_game()
 
            pygame.display.update()

    def create_background(self):
        for i in range(30):
            x = random.randint(2,8)
            background_image = Background(x,x)
            background_image.rect.x = random.randrange(0, s_width)
            background_image.rect.y = random.randrange(0, s_height)
            background_group.add(background_image)
            sprite_group.add(background_image)
    
    def create_player(self):
        self.player = player(player_ship)
        player_group.add(self.player)
        sprite_group.add(self.player)

    def create_enemy(self):
        for i in range(5):
            self.enemy = Enemy(enemy_ship)
            enemy_group.add(self.enemy)
            sprite_group.add(self.enemy)

    def create_sideenemy(self):
        for i in range (1):
            self.sideenemy = SideEnemy(sideenemy_ship)
            sideenemy_group.add(self.sideenemy)
            sprite_group.add(self.sideenemy)

    def create_enemy2(self):
        for i in range(2):
            self.enemy2 = Enemy2(enemy2_ship)
            enemy2_group.add(self.enemy2)
            sprite_group.add(self.enemy2)


    def playerbullet_hits_enemy(self):
        hits = pygame.sprite.groupcollide(enemy_group, playerbullet_group, False, True)
        for i in hits:
            self.count_hit += 1
            if self.count_hit == 3:
                expl_x = i.rect.x + 50
                expl_y = i.rect.y + 50
                explosion = Explosion (expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)
                i.rect.x = random.randrange(0, s_width)
                i.rect.y = random.randrange(-3000, -100)
                self.count_hit = 0
                self.score += 10

    def playerbullet_hits_sideenemy(self):
        hits = pygame.sprite.groupcollide(sideenemy_group, playerbullet_group, False, True)
        for i in hits:
            self.count_hit2 += 1
            if self.count_hit2 == 15:
                expl_x = i.rect.x + 60
                expl_y = i.rect.y + 50
                explosion = Explosion (expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)
                i.rect.x = -199
                self.count_hit2 = 0
                self.score += 30

    def playerbullet_hits_enemy2(self):
        hits = pygame.sprite.groupcollide(enemy2_group, playerbullet_group, False, True)
        for i in hits:
            self.count_hit += 1
            if self.count_hit == 5:
                expl_x = i.rect.x + 50
                expl_y = i.rect.y + 50
                explosion = Explosion (expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)
                i.rect.x = random.randrange(0, s_width)
                i.rect.y = random.randrange(-3000, -100)
                self.count_hit = 0
                self.score += 20              

    def enemybullet_hits_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemybullet_group, True)
            if hits:
                self.lives -= 1
                self.player.dead()
                if self.lives < 0:
                        pygame.mixer.music.stop()
                        gameover_sound.play()
                        red =pygame.Color(255,0,0)
                        my_font = pygame.font.Font("Tubes/font/ModernAesthetic-Personal.otf",90)
                        game_over_surface =  my_font.render('GAME OVER', True, red)
                        game_over_rect = game_over_surface.get_rect()
                        game_over_rect.midtop = (s_width/2, s_height/4)
                        screen.fill((0,0,0))
                        screen.blit(game_over_surface, game_over_rect)
                        pygame.display.flip()
                        time.sleep(11)
                        pygame.quit()
                        sys.exit()

    def sideenemy_hits_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, sideenemybullet_group, True)
            if hits:
                self.lives -= 1
                self.player.dead()
                if self.lives < 0:
                    pygame.mixer.music.stop()
                    gameover_sound.play()
                    red =pygame.Color(255,0,0)
                    my_font = pygame.font.Font("Tubes/font/.ttf",90)
                    game_over_surface =  my_font.render('GAME OVER', True, red)
                    game_over_rect = game_over_surface.get_rect()
                    game_over_rect.midtop = (s_width/2, s_height/4)
                    screen.fill((0,0,0))
                    screen.blit(game_over_surface, game_over_rect)
                    pygame.display.flip()
                    time.sleep(11)
                    pygame.quit()
                    sys.exit()

    def player_enemy_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemy_group, False)
            if hits:
                for i in hits:
                    i.rect.x = random.randrange(0, s_width)
                    i.rect.y = random.randrange(-3000, -100)
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        pygame.mixer.music.stop()
                        gameover_sound.play()
                        red =pygame.Color(255,0,0)
                        my_font = pygame.font.Font("Tubes/font/Pixeled.ttf",90)
                        game_over_surface =  my_font.render('GAME OVER', True, red)
                        game_over_rect = game_over_surface.get_rect()
                        game_over_rect.midtop = (s_width/2, s_height/4)
                        screen.fill((0,0,0))
                        screen.blit(game_over_surface, game_over_rect)
                        pygame.display.flip()
                        time.sleep(11)
                        pygame.quit()
                        sys.exit()

    def player_sideenemy_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, sideenemy_group, False)
            if hits:
                for i in hits:
                    i.rect.x = -199
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        pygame.mixer.music.stop()
                        gameover_sound.play()
                        red =pygame.Color(255,0,0)
                        my_font = pygame.font.Font("Tubes/font/Pixeled.ttf",90)
                        game_over_surface =  my_font.render('GAME OVER', True, red)
                        game_over_rect = game_over_surface.get_rect()
                        game_over_rect.midtop = (s_width/2, s_height/4)
                        screen.fill((0,0,0))
                        screen.blit(game_over_surface, game_over_rect)
                        pygame.display.flip()
                        time.sleep(11)
                        pygame.quit()
                        sys.exit()

    def player_enemy2_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemy2_group, False)
            if hits:
                for i in hits:
                    i.rect.x = random.randrange(0, s_width)
                    i.rect.y = random.randrange(-3000, -100)
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        pygame.mixer.music.stop()
                        gameover_sound.play()
                        red =pygame.Color(255,0,0)
                        my_font = pygame.font.Font("Tubes/font/Pixeled.ttf",90)
                        game_over_surface =  my_font.render('GAME OVER', True, red)
                        game_over_rect = game_over_surface.get_rect()
                        game_over_rect.midtop = (s_width/2, s_height/4)
                        screen.fill((0,0,0))
                        screen.blit(game_over_surface, game_over_rect)
                        pygame.display.flip()
                        time.sleep(11)
                        pygame.quit()
                        sys.exit()

    def create_lives(self):
        self.live_img = pygame.image.load(player_ship)
        self.live_img = pygame.transform.scale(self.live_img,(30,30))
        n = 0
        for i in range(self.lives):
            screen.blit(self.live_img, (0+n, s_height-750))
            n += 60

    def display_score(self):
        score_surf = self.font.render(f'Score: {self.score}', False, 'green')
        score_rect = score_surf.get_rect(topright=(s_width - 10, 10))
        screen.blit(score_surf, score_rect)


    

    def run_update(self):
        sprite_group.draw(screen)
        sprite_group.update()
 
    def run_game(self):
        self.create_background()
        self.create_player()
        self.create_enemy()
        self.create_sideenemy()
        self.create_enemy2()
        while True:
            screen.fill('black')
            self.playerbullet_hits_enemy()
            self.playerbullet_hits_sideenemy()
            self.playerbullet_hits_enemy2()
            self.enemybullet_hits_player()
            self.sideenemy_hits_player()
            self.player_enemy_crash()
            self.player_sideenemy_crash()
            self.player_enemy2_crash()
            self.create_lives()
            self.display_score()
            self.run_update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(laser_sound)
                    self.player.shoot()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
 
                    if event.key == K_SPACE:
                        self.pause_screen()
                    
            pygame.display.update()
            clock.tick(FPS)

def main():
    game = Game()
 
if __name__ == '__main__':
    main()