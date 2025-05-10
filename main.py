# main.py

# === IMPORT LIBRARY ===
from pygame.locals import *  # Import konstanta pygame seperti QUIT, KEYDOWN, dll

from core.config import GAME_SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_CLOCK, GAME_FPS
from core.utils import *
from core.resources import *
from core.game import *

from entities import *
from entities.enemies import *

# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()
    game.game_loop()