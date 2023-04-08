import pygame
from laser import Laser

class Player:
    def __init__(self, game):
        self.game = game
        self.image = pygame.Surface((50, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        self.speed = 5
        self.cooldown = 0
        self.health = 1
        self.laser_count = 1
        self.laser_speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.cooldown == 0:
            self.shoot()
            self.cooldown = 20

        if self.cooldown > 0:
            self.cooldown -= 1

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def shoot(self):
        if self.laser_count == 1:
            laser = Laser(self.game, self.rect.centerx, self.rect.y, self.laser_speed, "player")
            self.game.enemies.append(laser)
        elif self.laser_count == 2:
            laser1 = Laser(self.game, self.rect.centerx - 15, self.rect.y, self.laser_speed, "player")
            laser2 = Laser(self.game, self.rect.centerx + 15, self.rect.y, self.laser_speed, "player")
            self.game.enemies.extend([laser1, laser2])

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.game.reset_game()
    
    def upgrade_health(self):
        self.health += 1

    def upgrade_laser(self):
        self.laser_count += 1

    def upgrade_shooting_speed(self):
        self.laser_speed += 2
