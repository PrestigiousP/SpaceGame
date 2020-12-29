import random
import pygame
import sys
import time
import os
from Object.meteor import Meteor
from Object.player import Player
from Event import Event


def main():
    pygame.init()
    screen_width = 1000
    screen_height = 680

    # Set screen object and display
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Set space background image
    space_background = pygame.image.load(os.path.join('Images', 'space.png'))
    space_rect = space_background.get_rect()
    # Create player
    player = Player(screen, 0.8, 500, 340, 100)

    rocks = []
    for i in range(10):
        # rocks.append(Meteor(screen, random.uniform(0.2, 1), 100))
        rocks.append(Meteor(screen,  1, 100))
        rocks[i].set_random_position()

    # a dict to map keys to a direction
    movement = {pygame.K_UP: (0, -1),
                pygame.K_DOWN: (0, 1),
                pygame.K_LEFT: (-1, 0),
                pygame.K_RIGHT: (1, 0)}

    move = (0, 0)
    player_movement = [0, 0]
    arrow_key_pressed = 0

    player_event = Event()
    player_event.set_event(pygame.event.get())
    player_event.attach(player)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                move = movement.get(event.key, move)
                arrow_key_pressed += 1
                if arrow_key_pressed < 4:
                    player_movement[0] += move[0]
                    player_movement[1] += move[1]
                else:
                    player_movement[0] += move[0] * 2
                    player_movement[1] += move[1] * 2

            if event.type == pygame.KEYUP:
                arrow_key_pressed -= 1
                if event.scancode == 79 or event.scancode == 80:
                    player_movement[0] = 0
                elif event.scancode == 81 or event.scancode == 82:
                    player_movement[1] = 0

        player.rotate_image(player_movement)
        player.move(player_movement)

        screen.blit(space_background, space_rect)
        screen.blit(player.image, player.rect)

        for i in range(10):
            if (rocks[i].position[0] > 1100 or rocks[i].position[0] < -100 or rocks[i].position[1] > 780 or
                    rocks[i].position[1] < -100):
                rocks[i].set_random_position()
                print(rocks[i].position)
            else:
                screen.blit(pygame.transform.rotate(rocks[i].image, 0), rocks[i].rect)
                # should notify
                rocks[i].move()
        # for i in range(10):
        #     screen.blit(pygame.transform.rotate(rocks[i].image, 0), rocks[i].rect)
        #     rocks[i].move()
        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
