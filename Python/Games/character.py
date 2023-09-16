import pygame
import sys

pygame.init()

# Set up your window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickable Button")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.font = pygame.font.Font(None, 36)
        self.clicked = False

    def draw(self, screen):
        if self.clicked:
            pygame.draw.rect(screen, GRAY, self.rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.rect)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

button = Button(300, 250, 200, 100, "Click Me", WHITE, BLACK)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button.is_clicked(event.pos):
                    button.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if button.clicked and button.is_clicked(event.pos):
                    print("Button clicked!")
                button.clicked = False

    screen.fill(WHITE)
    button.draw(screen)
    pygame.display.flip()