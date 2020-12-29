import pygame
import os
import math
import random
from Object.gameObject import GameObject


class Meteor(GameObject):

    def __init__(self, screen, speed, health):
        super().__init__(screen, speed, health)

        self.health = health

        # Var useful to know the relative location of the object
        self.relative_position = ''

        # Set the image for the object
        self.image = pygame.image.load(os.path.join('Images', 'meteor.png'))
        self.rect = self.image.get_rect()

    def move(self):
        angle = None
        if self.relative_position == 'top':
            min_angle = math.atan2((self.screen.get_height() / 2) + 50, 50)
            angle = random.uniform(min_angle, 2 * min_angle)
        elif self.relative_position == 'right':
            min_angle = math.atan2(50, (self.screen.get_width() / 2) + 50)
            angle = random.uniform(min_angle + (math.pi / 2), (2 * min_angle) + (math.pi / 2))
        elif self.relative_position == 'bottom':
            min_angle = math.atan2((self.screen.get_height() / 2) + 50, 50)
            angle = random.uniform(min_angle + math.pi, (2 * min_angle) + math.pi)
        elif self.relative_position == 'left':
            min_angle = math.atan2((self.screen.get_height() / 2) + 50, 50)
            angle = random.uniform(min_angle + (math.pi * (6 / 4)), (2 * min_angle) + (math.pi * (6 / 4)))
        y = self.speed * math.sin(angle)
        x = self.speed * math.cos(angle)
        self.position = (self.position[0] + x, self.position[1] + y)
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))

    def set_random_position(self):
        r = random.random()
        x = None
        y = None
        if 0 <= r < 0.25:
            self.relative_position = 'top'
            x = random.randint(0, self.screen.get_width())
            y = -50
        elif 0.25 <= r < 0.5:
            self.relative_position = 'right'
            x = self.screen.get_width()+50
            y = random.randint(-50, self.screen.get_height())
        elif 0.5 <= r < 0.75:
            self.relative_position = 'bottom'
            x = random.randint(0, self.screen.get_width())
            y = self.screen.get_height()+50
        elif 0.75 <= r < 1:
            self.relative_position = 'left'
            x = -50
            y = random.randint(-50, self.screen.get_height())
        self.position = [x, y]
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        return self.position
