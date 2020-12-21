import os
import pygame
import math

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

    def update_image(self):
        self.image = pygame.transform.rotate(self.image, math.pi)

    def move(self, direction):
        """
        Permet au joueur de se déplacer. Le second argument sert à empêcher une récursivité infinie.
        """
        if direction == [0, -1]:
            # up
            self.position[1] -= 1 * self.speed
        elif direction == [0, 1]:
            # down
            self.position[1] += 1 * self.speed
        elif direction == [1, 0]:
            # right
            self.position[0] += 1 * self.speed
        elif direction == [-1, 0]:
            # left
            self.position[0] -= 1 * self.speed
        elif direction == [-1, -1]:
            # up left
            self.position[1] -= 1 * self.speed
            self.position[0] -= 1 * self.speed
        elif direction == [-1, 1]:
            # down left
            self.position[1] += 1 * self.speed
            self.position[0] -= 1 * self.speed
        elif direction == [1, -1]:
            # up right
            self.position[1] -= 1 * self.speed
            self.position[0] += 1 * self.speed
        elif direction == [1, 1]:
            # down right
            self.position[1] += 1 * self.speed
            self.position[0] += 1 * self.speed
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))

    def update(self, event: Event):
        print("update received and receive the event: ", event)
        self.move(event)
        # gotta stop the move function
        pass
