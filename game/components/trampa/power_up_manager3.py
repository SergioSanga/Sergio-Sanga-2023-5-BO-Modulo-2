import random
import pygame
from game.components.trampa.shield3 import Shield3
from game.components.bullets.bullet_manager import BulletManager
from game.utils.constants import SCREEN_HEIGHT, SPACESHIP_SHIELD

class PowerUpManager3():
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 30000)
        self.duration = random.randint(1, 1)

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            power_up = Shield3()
            power_up2 = BulletManager()
            self.when_appears = current_time + random.randint(5000, 30000)
            self.power_ups.append(power_up)

        for power_up in self.power_ups:
            power_up.update(game.game_speed)
            if power_up.rect.y >= SCREEN_HEIGHT:
                self.power_ups.remove(power_up)

            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = current_time
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = current_time + (self.duration * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    