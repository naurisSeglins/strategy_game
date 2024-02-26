import pygame
import math

pygame.init()

# Constants
UNIT_SIZE = 50
MOVE_SPEED = 3


class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, color, selected_color, name):
        super().__init__()
        self.image = pygame.Surface((UNIT_SIZE, UNIT_SIZE))
        self.image.fill(color)
        self.original_color = color
        self.rect = self.image.get_rect(center=(x, y))
        self.selected = False
        self.target = None
        self.selected_color = selected_color
        self.follow = None
        self.name = name
        self.health = 10
        self.attack = None
        self.attacking = 29
        self.angle = 90
        self.move_speed = 3

    def update(self):
        if self.selected:
            self.image.fill(self.selected_color)
        else:
            self.image.fill(self.original_color)

        if self.target:
            dx = self.target[0] - self.rect.centerx
            dy = self.target[1] - self.rect.centery
            distance = math.hypot(dx, dy)
            if distance > MOVE_SPEED:
                self.rect.x += dx * self.move_speed / distance
                self.rect.y += dy * self.move_speed / distance
                # Calculate rotation angle
                angle = math.atan2(-dy, dx)
                self.angle = math.degrees(angle)
            else:
                self.target = None

        self.following()

        # check health
        if self.health == 0:
            print("dieded")
            self.kill()

    def following(self):
        if self.follow:
            self.target = self.follow.rect.centerx, self.follow.rect.centery

    def figthing(self):
        if self.attack:
            self.attacking += 1
            if self.attacking >= 30:
                self.attack.health -= 1
                self.attacking = 0

    def collision(self, unit, all_units):
        collide = pygame.sprite.spritecollide(unit, all_units, False)
        if len(collide) >= 2:
            for near_units in collide:
                if self.original_color != near_units.original_color:
                    if self.follow:
                        self.attack = self.follow
                    elif self.attack is None:
                        self.attack = near_units
                    self.figthing()
                    self.follow = None
                    self.target = None
                self.move_speed = 2
        else:
            self.move_speed = 3

    def create_unit_image(self):
        image = pygame.image.load("assets/sword_942510.png")
        unit_image = pygame.transform.scale(image, (UNIT_SIZE, UNIT_SIZE))
        return unit_image

    def draw_units(self, screen):
        pygame.draw.rect(screen, self.image.get_at((0, 0)), self.rect)
        screen.blit(self.create_unit_image(), self.rect)
