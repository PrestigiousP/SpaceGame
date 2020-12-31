import random
import pygame
import sys
import time
import threading
import os
from Object.meteor import Meteor
from Object.player import Player
from Event import Event


def wait():
    timer = 1
    for i in range(1):
        timer -= 1
        time.sleep(1)
    print("finished")


def check_collision(take_damage, player, rocks):
    if take_damage:
        take_damage = hitbox_collision(player, rocks)
        #print(player.health)
        return take_damage
    else:
        thread = threading.Thread(target=wait)
        thread.start()
        take_damage = True
        return take_damage


def hitbox_collision(player, rocks):
    hitbox = player.get_hitbox()
    x_player = hitbox[0][0]
    y_player = hitbox[0][1]
    # Calculate if player's hitbox is in the range for every rock
    for i in rocks:
        a = x_player - i.position[0]
        b = y_player - i.position[1]
        c_squared = a ** 2 + b ** 2
        c = c_squared ** 0.5
        hitbox2 = i.get_hitbox()
        # hitbox[1] is the radius of the player object
        if hitbox[1] + hitbox2[1] >= c:
            player.get_hit(i.damage)
            print("player hit")
            return False
        else:
            return True

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
    # Allow the player to get hit
    take_damage = True

    # Add meteors to the game
    rocks = []
    for i in range(10):
        # Surface, speed, hp, damage
        rocks.append(Meteor(screen, random.uniform(0.2, 1), 100, 10))
        rocks[i].set_random_position()

    # List containing objects
    # Not created yet

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

        # Check if the player got hit
        take_damage = check_collision(take_damage, player, rocks)
        print(player.health)

        player.rotate_image(player_movement)
        player.move(player_movement)

        screen.blit(space_background, space_rect)
        pygame.draw.circle(screen, (0, 255, 30), player.position, 32)
        # pygame.draw.rect(screen, (0, 255, 0), player.rect)
        screen.blit(player.image, player.rect)

        for i in range(10):
            if (rocks[i].position[0] > 1100 or rocks[i].position[0] < -100 or rocks[i].position[1] > 780 or
                    rocks[i].position[1] < -100):
                rocks[i].set_random_position()
            else:
                screen.blit(pygame.transform.rotate(rocks[i].image, 0), rocks[i].rect)
                # should notify
                rocks[i].move()
            pygame.draw.circle(screen, (0, 255, 0), rocks[i].position, 30)
            # print(rocks[i])

        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
