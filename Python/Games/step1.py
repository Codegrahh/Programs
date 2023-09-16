import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the game windowre
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("My Pygame")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_width, current_height = pygame.display.get_surface().get_size()
    image = pygame.image.load("robot.png")
    # Calculate a scale factor based on the window's dimensions
    scale_factor_x = current_width / WIDTH
    scale_factor_y = current_height / HEIGHT
    image = pygame.transform.scale(image, (int(image.get_width() * scale_factor_x), int(image.get_height() * scale_factor_y)))
   
    # Get the rect (position and size) of the image
    image_rect = image.get_rect()

    # Position the image on the screen
    image_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Clear the screen
    screen.fill("white")  # Fill with black or your desired background color

    # Draw the image onto the screen
    screen.blit(image, image_rect)

    # Update the screen
    pygame.display.flip()



# Quit Pygame
pygame.quit()
sys.exit()