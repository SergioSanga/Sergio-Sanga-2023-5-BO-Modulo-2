import pygame

from game.utils.constants import SCREEN_HEIGHT

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update()
            if bullet.rect.y >= SCREEN_HEIGHT:
                self.enemy_bullets.remove(bullet)

            elif bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.death_count += 1
                self.enemy_bullets.remove(bullet)
                game.playing = False
            else:
                self.shoot_enemy(bullet, game)
            

        for bullet in self.player_bullets:
            bullet.update()
            if bullet.rect.y < 0:
                self.player_bullets.remove(bullet)

    def shoot_enemy(self, bullet, game):
        for enemy in game.enemy_manager.enemies:
            if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                game.enemy_manager.enemies.remove(enemy)
                game.update_score()
                self.player_bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.player_bullets) < 1:
            self.player_bullets.append(bullet)