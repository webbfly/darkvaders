import pygame
from random import randint
from laser import Laser


class Enemy:
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.Surface((40, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 1
        self.max_health = 100
        self.current_health = self.max_health

    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20

        if randint(0, 1000) < 5:  # 0.5% chance of shooting
            self.shoot()

    def shoot(self):
        laser = Laser(self.game, self.rect.centerx,
                      self.rect.y, self.speed, "enemy")
        self.game.enemies.append(laser)

    def die(self):
        self.game.score += 1
        self.game.money += 1
        self.game.enemies.remove(self)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.draw_health_bar()

    def draw_health_bar(self):
        health_percentage = self.current_health / self.max_health
        health_bar_width = 40
        health_bar_height = 5
        health_bar_color = (0, 255, 0)
        health_bar_background_color = (255, 255, 255)

        health_bar_x = self.rect.x
        health_bar_y = self.rect.y - health_bar_height - 2

        health_bar_background = pygame.Surface(
            (health_bar_width, health_bar_height))
        health_bar_background.fill(health_bar_background_color)
        self.game.screen.blit(health_bar_background,
                              (health_bar_x, health_bar_y))

        health_bar = pygame.Surface(
            (health_bar_width * health_percentage, health_bar_height))
        health_bar.fill(health_bar_color)
        self.game.screen.blit(health_bar, (health_bar_x, health_bar_y))

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.die()
            # self.game.enemies.remove(self)
