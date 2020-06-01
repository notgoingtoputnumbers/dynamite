import sys

import pygame

from game_objects import Background, rectangules, player, blasts, enemies, boxes, loots, bombs
from settings import SIZE, WHITE

pygame.init()
pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Game objects
#player = Player()

#background = Background()


# Groups
moving_objects = pygame.sprite.Group()


#weapons.add(Weapon(player.rect.midtop))

moving_objects.add(player)
#moving_objects.add(Weapon(player.rect.midtop))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    moving_objects.update()
    bombs.update()
    enemies.update()
    blasts.update()
    boxes.update()


    #screen.blit(weapons.image, weapons2.rect)


    #    screen.blit(background.image, background.rect)
    #    screen.blit(player.image, player.rect)
    moving_objects.draw(screen)
    bombs.draw(screen)
    enemies.draw(screen)
    blasts.draw(screen)
    loots.draw(screen)
    # circles.draw(screen)

    for i in boxes:
        pygame.draw.rect(screen, (0, 0, 255), i)

    for i in rectangules:
        pygame.draw.rect(screen, (255, 0, 0), i)



    pygame.display.flip()

    clock.tick(60)
