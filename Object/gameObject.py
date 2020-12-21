import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self, screen, speed, health):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.health = health

        # Screen used to display the object
        self.screen = screen

        # Set the position
        self.position = None

        # Set the speed
        self.speed = speed

        # Set the image
        self.image = None
        self.rect = None
        # self.image.get_rect(center=(position[0], position[1]))

    def get_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.delete()

    def delete(self):
        del self
