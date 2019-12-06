import pygame


class App:
    display_surf = None
    turn = 0

    def __init__(self):
        self.running = True
        self.size = self.width, self.height = 600, 600
        self.state = [[Button((0,0)),Button((0,1)),Button((0,2))],
                      [Button((1,0)),Button((1,1)),Button((1,2))],
                      [Button((2,0)),Button((2,1)),Button((2,2))]]

    def on_init(self):
        pygame.init()
        App.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

        App.display_surf.fill((255, 255, 255))
        pygame.draw.line(App.display_surf, pygame.Color("black"), (self.width / 3, 0), (self.width / 3, self.height), 2)
        pygame.draw.line(App.display_surf, pygame.Color("black"), (self.width*2/3, 0), (self.width*2/ 3, self.height), 2)

        pygame.draw.line(App.display_surf, pygame.Color("black"), (0, self.height / 3), (self.width, self.height / 3), 2)
        pygame.draw.line(App.display_surf, pygame.Color("black"), (0, self.height * 2 / 3), (self.width, self.height * 2 / 3), 2)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for row in self.state:
                for button in row:
                    button.event(event)

    def on_loop(self):
        pass

    def on_render(self):
        for row in self.state:
            for button in row:
                button.render()

        pygame.display.update()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    @classmethod
    def updateTurn(cls):
        if cls.turn == 0:
            cls.turn = 1
        else:
            cls.turn = 0

class Button:

    def __init__(self, position):
        self.state = None
        self.position = position
        self.size = 200
        self.x = (self.position[0] * self.size)
        self.y = (self.position[1] * self.size)
        self.rect = pygame.Rect(self.x, self.y, 200, 200)

    def set_state(self, state):
        if self.state is None:
            self.state = state

    def event(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint((x,y)):
            self.set_state(App.turn)
            App.updateTurn()

    def render(self):
        if self.state is None:
            color = (255,255,255)
        if self.state == 0:
            color = (255, 0, 0)
        if self.state == 1:
            color = (0, 0, 255)

        pygame.draw.rect(App.display_surf, color, (self.x+50, self.y+50, 100, 100))

app = App()
app.on_execute()