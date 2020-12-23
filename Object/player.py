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
        self.image_rotation = {
            (0, -1): 0,
            (-1, -1): 45,
            (-1, 0): 90,
            (-1, 1): 135,
            (0, 1): 180,
            (1, 1): 225,
            (1, 0): 270,
            (1, -1): 315,
        }
        self.image_direction = (0, -1)

    def rotate_image(self, direction):
        convert = tuple(direction)
        """empêcher que le vaisseau se repositionner dans un axe x ou y après avoir été dans un angle orizontale 
        et avoir arrêté de bouger"""
        # if (self.image_direction == (1, 1) or self.image_direction == (-1, 1) or
        #     self.image_direction == (1, -1) or self.image_direction == (-1, -1)):


        if convert != (0, 0) and convert != self.image_direction:
            self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
            self.image = pygame.transform.rotate(self.image, self.image_rotation[convert])
            self.image_direction = convert

        # rotation = 0
        # convert = tuple(direction)
        # if convert != (0, 0) and convert != self.image_direction:
        #     result = convert[0] - self.image_direction[0]
        #     result2 = convert[1] - self.image_direction[1]
        #     if result == 1:
        #         rotation += 45
        #     elif result == -1:
        #         rotation += 225
        #     elif result == 2:
        #         rotation += 90
        #     if result2 == 1:
        #         rotation += 45
        #     elif result2 == -1:
        #         rotation += 225
        #     elif result == 2:
        #         rotation += 90
        #     self.image_direction = convert
        # self.image = pygame.transform.rotate(self.image, rotation)

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
            # self.image = pygame.transform.rotate(self.image, 270)
        elif direction == [-1, 0]:
            # left
            self.position[0] -= 1 * self.speed
            # self.image = pygame.transform.rotate(self.image, 90)
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
