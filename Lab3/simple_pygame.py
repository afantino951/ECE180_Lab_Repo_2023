"""
Source: https://realpython.com/pygame-a-primer/
"""

# Import the pygame module
import pygame

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ITEM_WIDTH = 128
ITEM_HEIGHT = 128

CIRCLE_RADIUS = int(ITEM_WIDTH/2 + 2)

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path) -> None:
        super(SpriteObject, self).__init__()
        self.surf = pygame.image.load(img_path).convert()
        self.click_surf = self.surf.copy()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (ITEM_WIDTH, ITEM_HEIGHT))
        self.past_surf = self.surf.copy()
        self.rect = self.surf.get_rect(center=(x, y))
        self.clicked = False

        self.click_surf = pygame.transform.scale(self.click_surf, (ITEM_WIDTH, ITEM_HEIGHT))
        pygame.draw.circle(self.click_surf, (255, 255, 255), (int(ITEM_WIDTH/2), int(ITEM_WIDTH/2)), CIRCLE_RADIUS, 4)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

        if self.clicked:
            self.surf = self.click_surf 
        else:
            self.surf = self.past_surf
        
        return self.clicked


if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    pygame.font.init()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_font = pygame.font.SysFont('Comic Sans MS', 50)


    my_sprite = SpriteObject(150, 255, "pygame_assets/rock.png")
    paper_icon = SpriteObject(300, 255, "pygame_assets/paper.png")
    scissor_icon = SpriteObject(450, 255, "pygame_assets/scissor.png")

    rps_sprites = pygame.sprite.Group()
    rps_sprites.add(my_sprite)
    rps_sprites.add(paper_icon)
    rps_sprites.add(scissor_icon)



    # Run until the user asks to quit
    running = True
    while running:
        # Look at every event in the queue
        event_list = pygame.event.get()
        for event in event_list:
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        # my_sprite.update(pressed_keys)

        # my_sprite.update(event_list)

        # Fill the background with black
        screen.fill((0, 0, 0))
        text_surface = my_font.render('Select Rock, Paper, or Scissors', False, (255, 255, 255))

        screen.blit(text_surface, (0, 100))

        # Draw all the sprites
        # NOTE: This only works if the sprites in all_sprites is a SpriteObject
        entity_clicked = False
        for entity in rps_sprites:
            if not entity_clicked:
                clicked = entity.update(event_list)
                entity_clicked = clicked if clicked else entity_clicked
            else:
               entity_clicked = True 

            screen.blit(entity.surf, entity.rect)
        
        # Flip the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

    # Done! Time to quit.
    pygame.quit()