import os
import pygame

from Event import Event
from Object.gameObject import GameObject
from EventHandlerInterface import EventHandlerInterface


class Player(GameObject, EventHandlerInterface):

    def __init__(self, screen, speed, x, y, health):
        super().__init__(screen, speed, health)
        self.health = health
        self.position = [x, y]
        self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.direction = [0, 0]

    def move(self, direction, second_direction):
        """
        Permet au joueur de se déplacer. Le second argument sert à empêcher une récursivité infinie.
        """
        if direction == (0, -1):
            # up
            self.direction[1] = -1
            self.position[1] -= 1
        elif direction == (0, 1):
            # down
            self.direction[1] = 1
            self.position[1] += 1
        elif direction == (1, 0):
            # right
            self.direction[0] = 1
            self.position[0] += 1
        elif direction == (-1, 0):
            # left
            self.direction[0] = -1
            self.position[0] -= 1
        if second_direction and self.direction != (0, 0):
            self.move(self.direction, False)
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))

    def update(self, event: Event):
        print("update received and receive the event: ", event)
        self.move(event)
        # gotta stop the move function
        pass
