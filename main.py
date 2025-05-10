# main.py

from core.game import *

# === MAIN FUNCTION ===
# Fungsi utama untuk menjalankan game
if __name__ == '__main__':
    game = Game()
    game.start_screen()
    game.game_loop()