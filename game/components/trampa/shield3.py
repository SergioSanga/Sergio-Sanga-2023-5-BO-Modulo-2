from game.components.trampa.power_up3 import PowerUps3
from game.utils.constants import SHIELD3, SHIELD_TYPE3
import pygame

class Shield3(PowerUps3):
    def __init__(self):
        super().__init__(SHIELD3, SHIELD_TYPE3)
        self.image = pygame.transform.scale(SHIELD3, (self.image.get_width() // 30, self.image.get_height() // 30))