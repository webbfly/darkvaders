import pygame


class Laser:

    def __init__(self, game, x, y, speed, shooter):
        self.game = game
        self.image = pygame.Surface((5, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.damage = 20
        self.shooter = shooter

    def update(self):
        if self.shooter == "player":
            self.rect.y -= self.speed
        elif self.shooter == "enemy":
            self.rect.y += self.speed

        self.check_collision()

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def check_collision(self):
        if self.shooter == "player":
            for enemy in self.game.enemies:
                if isinstance(enemy, Laser):
                    continue

                if self.rect.colliderect(enemy.rect):
                    enemy.take_damage(self.damage)
                    self.game.enemies.remove(self)
                    break
        elif self.shooter == "enemy":
            if self.rect.colliderect(self.game.player.rect):
                self.game.player.take_damage(self.damage)
                self.game.state = "menu"
