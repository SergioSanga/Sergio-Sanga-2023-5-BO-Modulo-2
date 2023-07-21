import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH/2) 
    Y_POS = 530

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.type = 'player'
        self.shooting_time = 30

    def update(self, user_input, game):
        self.shoot(user_input, game.bullet_manager)
        if user_input[pygame.K_LEFT]:
            if self.rect.left < 0:
               self.rect.x = SCREEN_WIDTH - self.SPACESHIP_HEIGHT
            else:  
               self.rect.x -= 10
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right > SCREEN_WIDTH:
               self.rect.x = 0
            else:  
               self.rect.x += self.speed

        if user_input[pygame.K_UP]:
           
            if (self.rect.top) > SCREEN_HEIGHT/2:
                self.rect.y -= self.speed

        elif user_input[pygame.K_DOWN]:
            if (self.rect.bottom) < SCREEN_HEIGHT:
                self.rect.y += self.speed


    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def shoot(self, user_input, bullet_manager):
        if user_input[pygame.K_SPACE]:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)