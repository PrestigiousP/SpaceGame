import os
import pygame
from time import *
import time
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
        time.perf_counter()
        self.image_timer1 = 0
        self.save_image_rotation = None
        #self.circle = pygame.draw.circle(screen, (66, 255, 10), self.position, 32)
        self.hitbox = (self.position, 32)

    def get_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            pass

    def get_hitbox(self):
        return self.hitbox

    def rotate_image(self, direction):
        convert = tuple(direction)
        if convert != (0, 0):
            """empêcher que le vaisseau se repositionner dans un axe x ou y après avoir été dans un angle horizontale 
                                et avoir arrêté de bouger"""
            # if convert != (1, 1) and convert != (-1, 1) and convert != (1, -1) and convert != (-1, -1):
            #     print(self.image_timer1, " non diag")
            #     if self.image_timer1 > 0 and (time.perf_counter() - self.image_timer1) < 15:
            #         self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
            #         self.image = pygame.transform.rotate(self.image, self.image_rotation[self.save_image_rotation])
            #         self.image_direction = self.save_image_rotation
            #         # self.image_timer1 = 0
            #     else:
            #         self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
            #         self.image = pygame.transform.rotate(self.image, self.image_rotation[convert])
            #         self.image_direction = convert
            #         print(time.perf_counter() - self.image_timer1)
            #         if time.perf_counter() - self.image_timer1 > 10:
            #             self.image_timer1 = 0
            # else:
            #     print(self.image_timer1, " diag")
            #     # Sauvegarde l'image en diagonale
            #     self.save_image_rotation = convert
            #     # Start un timer pour évaluer si l'image doit resté en diagonale
            #     self.image_timer1 = time.perf_counter()
            #     self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
            #     self.image = pygame.transform.rotate(self.image, self.image_rotation[convert])
            #     self.image_direction = convert

            self.image = pygame.image.load(os.path.join('Images', 'spaceshooter.png'))
            self.image = pygame.transform.rotate(self.image, self.image_rotation[convert])
            self.image_direction = convert

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
