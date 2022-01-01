import pygame

class Button: 

    def __init__(self, x, y, width, height, text, action):
        self.action = action
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.state = 1
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.rect = pygame.Rect(x, y, width, height)
    
    def handle_event(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if self.rect.collidepoint(event.pos): 
                    self.action() 
    
    def render(self, game): 
        pygame.draw.rect(game.screen, (0, 0, 0), self.rect, 4)
        text_surface = self.font.render(self.text, False, (0, 0, 0))
        game.screen.blit(text_surface, (self.x, self.y))

    def disable(self): 
        self.state = 0
    
    def enable(self):
        self.state = 1