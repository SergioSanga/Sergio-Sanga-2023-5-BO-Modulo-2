import pygame
import os
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu("WELCOME TO THE GAME", self.screen)
        self.death_count = 0
        self.score = 0
        self.highest_score = 0
        self.total_deaths = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.death_count = 0
        self.enemy_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

        # Check for collisions between player bullets and enemies
        for bullet in self.bullet_manager.player_bullets:
            for enemy in self.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullet_manager.player_bullets.remove(bullet)
                    self.enemy_manager.enemies.remove(enemy)
                    self.update_score()

        # Check for collisions between enemy bullets and player
        for bullet in self.bullet_manager.enemy_bullets:
            if bullet.rect.colliderect(self.player.rect):
                self.bullet_manager.enemy_bullets.remove(bullet)
                self.player_hit()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_total_deaths()  # Mostrar el total de muertes en el juego
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        font = pygame.font.Font(FONT_STYLE, 24)

        if self.death_count == 0:
            # Mostrar el mensaje inicial del menú
            self.menu.draw(self.screen)
        else:
            # Mostrar "Game Over" y otras estadísticas
            game_over_text = font.render('GAME OVER', True, (0, 0, 0))
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (half_screen_width, half_screen_height - 30)

            # Mostrar la puntuación del jugador
            score_text = font.render(f'Your score: {self.score}', True, (0, 0, 0))
            score_rect = score_text.get_rect()
            score_rect.center = (half_screen_width, half_screen_height + 10)

            # Mostrar la puntuación más alta
            self.highest_score = max(self.score, self.highest_score)
            highest_score_text = font.render(f'Highest score: {self.highest_score}', True, (0, 0, 0))
            highest_score_rect = highest_score_text.get_rect()
            highest_score_rect.center = (half_screen_width, half_screen_height + 50)

            # Mostrar el total de muertes
            deaths_text = font.render(f'Total deaths: {self.total_deaths}', True, (0, 0, 0))
            deaths_rect = deaths_text.get_rect()
            deaths_rect.center = (half_screen_width, half_screen_height + 90)

            # Dibujar las estadísticas en la pantalla
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(highest_score_text, highest_score_rect)
            self.screen.blit(deaths_text, deaths_rect)

        icon = self.image = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))

        self.menu.update(self)

    def update_score(self):
        self.score += 1

    def player_hit(self):
        self.death_count += 1
        self.total_deaths += 1
        print(f"Total deaths: {self.total_deaths}")


    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_total_deaths(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Total deaths: {self.total_deaths}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 100)
        self.screen.blit(text, text_rect)

