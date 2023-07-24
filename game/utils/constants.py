import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_FILE = os.path.join(IMG_DIR, "Music/lady-of-the-80x27s-128379.mp3")
MUSIC_FILE2 = os.path.join(IMG_DIR, "Music/SpaceLaserShot PE1095407.mp3")
# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SHIELD2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield2.png'))
SHIELD3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/trampa.png'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GO = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

TR = pygame.image.load(os.path.join(IMG_DIR, 'Other/trampa.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
DEFAULT_TYPE2 = "default"
SHIELD_TYPE2 = 'shield'
DEFAULT_TYPE3 = "default"
SHIELD_TYPE3= 'shield'
DEFAULT_TYPE4 = "default"
SHIELD_TYPE4= 'shield'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_3.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'