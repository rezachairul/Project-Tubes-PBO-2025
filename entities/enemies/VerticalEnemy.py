# class/VerticalEnemy and Child class dari BaseEnemy

from .BaseEnemy import BaseEnemy


# === KELAS BASE ENEMY (Kelas Dasar Musuh) ===
# class child enemy => (BaseEnemy):
'''
    - Kelas anak dari BaseEnemy.
    - Digunakan untuk musuh yang bergerak secara vertikal (atas/bawah).
'''

class VerticalEnemy(BaseEnemy):
    def __init__(self):
        super().__init__(health=10, score_value=1000)