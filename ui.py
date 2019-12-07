import pygame


class UI:
    display_surf = None

    def __init__(self):
        self.running = True
        self.size = self.width, self.height = 600, 600
        self.state = [[Button((0,0)),Button((0,1)),Button((0,2))],
                      [Button((1,0)),Button((1,1)),Button((1,2))],
                      [Button((2,0)),Button((2,1)),Button((2,2))]]

        pygame.init()
        UI.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        UI.display_surf.fill((255, 255, 255))
        pygame.draw.line(UI.display_surf, pygame.Color("black"), (self.width / 3, 0), (self.width / 3, self.height), 2)
        pygame.draw.line(UI.display_surf, pygame.Color("black"), (self.width * 2 / 3, 0),(self.width * 2 / 3, self.height), 2)
        pygame.draw.line(UI.display_surf, pygame.Color("black"), (0, self.height / 3), (self.width, self.height / 3),2)
        pygame.draw.line(UI.display_surf, pygame.Color("black"), (0, self.height * 2 / 3),(self.width, self.height * 2 / 3), 2)

    def render(self, game):
        for index_y, row in enumerate(self.state):
            for index_x, button in enumerate(row):
                button.state = game.state[index_y, index_x]
                button.render()

        pygame.display.update()


class Button:

    def __init__(self, position):
        self.state = None
        self.position = position
        self.size = 200
        self.x = (self.position[0] * self.size)
        self.y = (self.position[1] * self.size)
        self.rect = pygame.Rect(self.x, self.y, 200, 200)

    def render(self):
        color = (255,255,255)
        if self.state == 1:
            color = (255, 0, 0)
        if self.state == 2:
            color = (0, 0, 255)

        pygame.draw.rect(UI.display_surf, color, (self.x+50, self.y+50, 100, 100))