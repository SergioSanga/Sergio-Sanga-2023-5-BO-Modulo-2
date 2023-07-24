from game.components.power_shield.power_up2 import PowerUps2
from game.utils.constants import SHIELD2, SHIELD_TYPE2
import pygame

class Shield2(PowerUps2):
    def __init__(self):
        super().__init__(SHIELD2, SHIELD_TYPE2)
        self.image = pygame.transform.scale(SHIELD2, (self.image.get_width() // 25, self.image.get_height() // 25))