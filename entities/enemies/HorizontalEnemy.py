# class/HorizontalEnemy and Child class dari BaseEnemy

from .BaseEnemy import BaseEnemy


# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak secara horizontal (kiri/kanan).
'''

class HorizontalEnemy(BaseEnemy):
    def __init__(self):
        super().__init__(health=10, score_value=1000)