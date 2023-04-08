import pygame
from player import Player
from enemy import Enemy
from random import randint
from menu import Menu


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Darkvaders")
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.enemies = [Enemy(self, i * 60 + 10, 40) for i in range(10)]
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.state = "game"
        self.menu = Menu(self)
        self.enemies = []
        self.lasers = []
        self.score = 0
        self.money = 0
        self.FPS = 60
        self.spawn_enemies()

    def spawn_enemies(self):
        self.enemies = []
        for i in range(5):
            for j in range(5):
                enemy = Enemy(self, 100 + 100 * i, 50 + 50 * j)
                self.enemies.append(enemy)

    def reset_game(self):
        self.player = Player(self)
        self.spawn_enemies()

    def run(self):
        while self.running:
            if self.state == "game":
                self.handle_events()
                self.update()
                self.draw()
            elif self.state == "menu":
                self.menu.handle_events()
                self.menu.update()
                self.menu.draw()

    def main_loop(self):
        while True:
            self.clock.tick(self.FPS)

            if self.state == "game":
                self.handle_events()
                self.update()
                self.draw()

            elif self.state == "menu":
                self.menu.handle_events()
                self.menu.update()
                self.menu.draw()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.state == "game":
            self.player.update()
            for enemy in self.enemies:
                enemy.update()
            for laser in self.lasers:
                laser.update()
            if len(self.enemies) == 0:
                self.state = "menu"

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw()
        self.display_info()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.flip()

    def display_info(self):
        info_text = f"Health: {self.player.health} | Laser Power: {self.player.laser_count} | Shooting Speed: {self.player.laser_speed} | Score: {self.score} | Money: {self.money}"
        info_label = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(info_label, (10, 10))
