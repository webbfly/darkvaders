import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.menu_options = [
            {"label": "Upgrade Health", "upgrade": "upgrade_health", "cost": 1},
            {"label": "Upgrade Laser", "upgrade": "upgrade_laser", "cost": 1},
            {"label": "Upgrade Shooting Speed",
                "upgrade": "upgrade_shooting_speed", "cost": 1}
        ]
        self.selected_option = 0

    def draw(self):
        for i, option in enumerate(self.menu_options):
            label = self.font.render(option["label"], True, (255, 255, 255))
            position = (self.game.screen.get_width() // 2 - label.get_width() // 2,
                        200 + 50 * i)
            self.game.screen.blit(label, position)

            if self.selected_option == i:
                pygame.draw.circle(self.game.screen, (255, 255, 255),
                                   (position[0] - 20, position[1] + label.get_height() // 2), 10)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.selected_option = (
                self.selected_option - 1) % len(self.menu_options)
        if keys[pygame.K_DOWN]:
            self.selected_option = (
                self.selected_option + 1) % len(self.menu_options)
        if keys[pygame.K_RETURN]:
            upgrade_function = self.menu_options[self.selected_option]["upgrade"]
            # print(upgrade_function)
            print(self.selected_option)
            upgrade_cost = self.menu_options[self.selected_option]["cost"]
            if self.game.money >= upgrade_cost:
                getattr(self.game.player, upgrade_function)()
                self.game.money -= upgrade_cost
                self.menu_options[self.selected_option]["cost"] += 1
                self.game.reset_game()
                self.game.state = "game"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
