import pygame

from unit import Unit
from events import Event

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 1000

# Colors
WHITE = (255, 255, 255)

# Colors
RED = (255, 0, 0)
SELECTED_COLOR_RED = (255, 255, 0)
GREEN = (0, 255, 0)
SELECTED_COLOR_GREEN = (0, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generals")
clock = pygame.time.Clock()

# Create groups
all_units = pygame.sprite.Group()
selected_units = pygame.sprite.Group()

# Create units
for i in range(2):
    unit = Unit(100 + i * 55, 100, RED, SELECTED_COLOR_RED, name=f"red{i}")
    all_units.add(unit)

# Create units
for i in range(2):
    unit = Unit(150 + i * 55, 200, GREEN, SELECTED_COLOR_GREEN,
                name=f"green{i}")
    all_units.add(unit)

events = Event()

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    running = events.handle_events(all_units, selected_units, running)

    # Update selected units
    for unit in all_units:
        unit.update()
        # unit.following()
        unit.collision(unit, all_units)
        # Draw units
        # unit.draw_units(screen, unit)
        unit.draw_units(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
