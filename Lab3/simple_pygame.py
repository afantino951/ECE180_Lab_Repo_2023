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

CIRCLE_RADIUS = int(ITEM_WIDTH/2 + 5)

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path) -> None:
        super(SpriteObject, self).__init__()
        self.surf = pygame.image.load(img_path).convert()
        self.click_surf = self.surf.copy()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (ITEM_WIDTH, ITEM_HEIGHT))
        self.rect = self.surf.get_rect(center=((SCREEN_WIDTH-(4*ITEM_WIDTH))/2, (SCREEN_HEIGHT-ITEM_HEIGHT)/2))
        self.clicked = False

        # self.click_surf = pygame.image.load(img_path).convert()
        # self.click_surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.click_surf = pygame.transform.scale(self.click_surf, (ITEM_WIDTH, ITEM_HEIGHT))

        pygame.draw.circle(self.click_surf, (255, 255, 255), (int(ITEM_WIDTH/2), int(ITEM_WIDTH/2)), CIRCLE_RADIUS, 4)

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

        self.surf = self.click_surf if self.clicked else self.surf


if __name__ == '__main__':
    # Initialize pygame
    pygame.init()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_sprite = SpriteObject(75, 75, "pygame_assets/rock.png")
    # my_sprite = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(my_sprite)

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
        my_sprite.update(event_list)

        # Fill the background with black
        screen.fill((0, 0, 0))

        # Draw all the sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        # Flip the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

    # Done! Time to quit.
    pygame.quit()