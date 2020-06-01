import pygame

from bisect import bisect_left
from random import sample, randint, choice

from settings import WIDTH, HEIGHT, DETIME, BLASTIME, lines, explines, WALLSIZE



blasts = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Wall, self).__init__()

        self.rect = pygame.Rect(x, y, WALLSIZE, WALLSIZE)

rectangules = []
for i in range(1, 13, 2):
    for j in range(1, 13, 2):
        rectangules.append(Wall(WALLSIZE * i, WALLSIZE * j))

loots = pygame.sprite.Group()

def loot(position):
    a = randint(1, 10)
    if a > 6:
        loots.add(Dynamite(position))

def plusbullet(player):
    pass

class Dynamite(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Dynamite, self).__init__()

        self.image = pygame.image.load('assets/plusweapon.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = position

class Boxes(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Boxes, self).__init__()

        self.rect = pygame.Rect(x, y, WALLSIZE, WALLSIZE)

    def update(self):

        if pygame.sprite.spritecollide(self, blasts, False):
            loot(self.rect.midtop)
            self.kill()

boxes = pygame.sprite.Group()
for i in sample(range(13), 7):
    for j in sample(range(13), 7):
         boxes.add(Boxes(WALLSIZE * i, WALLSIZE * j))

def take_closest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

class Weapon(pygame.sprite.Sprite):

    def __init__(self, position, power):
        super(Weapon, self).__init__()

        self.position = position

        self.image = pygame.image.load('assets/dynamite.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = position

        self.time = pygame.time.Clock()
        self.time_elapsed = 0

        self.power = power

    def update(self):
        self.time_elapsed += self.time.tick()
        if self.time_elapsed > DETIME:
            blasts.add(BlastUp(self.power, self.position))
            blasts.add(BlastDown(self.power, self.position))
            blasts.add(BlastRight(self.power, self.position))
            blasts.add(BlastLeft(self.power, self.position))
            player.weapon_update()
            self.kill()

# class CircleBlast(pygame.sprite.Sprite):
#     def __init__(self, power, position):
#         super(CircleBlast, self).__init__()
#
#         self.power = power
#         self.position = position
#
#         self.circle = pygame.draw.circle((0, 255, 0), 50, 50)

# circles = pygame.sprite.Group()
# circles.add(CircleBlast(5, 50))


class BlastUp(pygame.sprite.Sprite):
    def __init__(self, power, position):
        super(BlastUp, self).__init__()

        self.power = power
        self.position = position
        self.time = pygame.time.Clock()
        self.time_elapsed = 0
        self.time_check = 0

        self.image = pygame.image.load('assets/blast.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.position

    def update(self):
        self.time_elapsed += self.time.tick()
        self.time_check += self.time.get_time()

        if self.time_check > 1000 / self.power:
            self.rect.move_ip(0, 50)
            self.time_check = 0

        if self.time_elapsed > BLASTIME:
            self.kill()

class BlastDown(pygame.sprite.Sprite):
    def __init__(self, power, position):
        super(BlastDown, self).__init__()

        self.power = power
        self.position = position
        self.time = pygame.time.Clock()
        self.time_elapsed = 0
        self.time_check = 0

        self.image = pygame.image.load('assets/blast.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.position

    def update(self):
        self.time_elapsed += self.time.tick()
        self.time_check += self.time.get_time()

        if self.time_check > 1000 / self.power:
            self.rect.move_ip(0, -50)
            self.time_check = 0

        if self.time_elapsed > BLASTIME:
            self.kill()

class BlastLeft(pygame.sprite.Sprite):
    def __init__(self, power, position):
        super(BlastLeft, self).__init__()

        self.power = power
        self.position = position
        self.time = pygame.time.Clock()
        self.time_elapsed = 0
        self.time_check = 0

        self.image = pygame.image.load('assets/blast.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.position

    def update(self):
        self.time_elapsed += self.time.tick()
        self.time_check += self.time.get_time()

        if self.time_check > 1000 / self.power:
            self.rect.move_ip(-50, 0)
            self.time_check = 0

        if self.time_elapsed > BLASTIME:
            self.kill()

class BlastRight(pygame.sprite.Sprite):
    def __init__(self, power, position):
        super(BlastRight, self).__init__()

        self.power = power
        self.position = position
        self.time = pygame.time.Clock()
        self.time_elapsed = 0
        self.time_check = 0

        self.image = pygame.image.load('assets/blast.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.position

    def update(self):
        self.time_elapsed += self.time.tick()
        self.time_check += self.time.get_time()

        if self.time_check > 1000 / self.power:
            self.rect.move_ip(50, 0)
            self.time_check = 0

        if self.time_elapsed > BLASTIME:
            self.kill()


bombs = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    max_speed = 3

    # bullets = 2
    # wasted = 0

    def __init__(self, weapons):
        super(Player, self).__init__()

        self.weapons = weapons

        self.image = pygame.image.load('assets/cat.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT - 25

        self.time = pygame.time.Clock()
        self.time_bomb_delay = 0
        self.bullets = 2
        self.power = 3

    def update(self):

        if pygame.sprite.spritecollide(self, boxes, False):
            self.rect.move_ip((-self.current_speed_x, -self.current_speed_y))

        self.current_speed_x = self.current_speed_y = 0

        keys = pygame.key.get_pressed()

        if self.rect.centery in lines:
            if keys[pygame.K_LEFT] and self.rect.centerx >= 25:
                self.current_speed_x = - self.max_speed
            if keys[pygame.K_RIGHT] and self.rect.centerx <= WIDTH - 25:
                self.current_speed_x = self.max_speed
            if keys[pygame.K_UP] and self.rect.centery >= 25 and self.rect.centerx in explines:
                self.rect.centerx = take_closest(lines, self.rect.centerx)
                self.current_speed_x = 0
                self.current_speed_y = - self.max_speed
            if keys[pygame.K_DOWN] and self.rect.centery <= HEIGHT - 25 and self.rect.centerx in explines:
                self.rect.centerx = take_closest(lines, self.rect.centerx)
                self.current_speed_x = 0
                self.current_speed_y = self.max_speed

        if self.rect.centerx in lines:
            if keys[pygame.K_DOWN] and self.rect.centery <= HEIGHT - 25:
                self.current_speed_y = self.max_speed
            if keys[pygame.K_UP] and self.rect.centery >= 25:
                self.current_speed_y = - self.max_speed
            if keys[pygame.K_LEFT] and self.rect.centerx >= 25 and self.rect.centery in explines:
                self.rect.centery = take_closest(lines, self.rect.centery)
                self.current_speed_y = 0
                self.current_speed_x = - self.max_speed
            if keys[pygame.K_RIGHT] and self.rect.centerx <= WIDTH - 25 and self.rect.centery in explines:
                self.rect.centery = take_closest(lines, self.rect.centery)
                self.current_speed_y = 0
                self.current_speed_x = self.max_speed

        self.rect.move_ip((self.current_speed_x, self.current_speed_y))

        self.shooting()

    def shooting(self):

        keys = pygame.key.get_pressed()

        if self.time_bomb_delay > 0:
            self.time_bomb_delay -= self.time.tick()
        else:
            self.time_bomb_delay = 0

        if keys[pygame.K_SPACE] and self.bullets > 0 and self.time_bomb_delay == 0:
            self.weapons.add(Weapon(self.rect.midtop, self.power))
            self.bullets -= 1
            self.time_bomb_delay = 200
            self.time.tick()

    def weapon_update(self):

        self.bullets += 1


player = Player(bombs)


class Enemy(pygame.sprite.Sprite):

    max_speed = 1.5

    def __init__(self, player_pos_x, player_pos_y, enemy_pos_x, enemy_pos_y):
        super(Enemy, self).__init__()

        self.player_pos_x = player_pos_x
        self.player_pos_y = player_pos_y

        self.image = pygame.image.load('assets/evil.png')
        self.rect = self.image.get_rect()

        self.enemy_pos_x = enemy_pos_x
        self.enemy_pos_y = enemy_pos_y


        self.rect.centerx = self.enemy_pos_x
        self.rect.bottom = self.enemy_pos_y

    def update(self):

        if pygame.sprite.spritecollide(self, blasts, False):
            self.kill()

        self.player_pos_x, self.player_pos_y = player.rect.left, player.rect.top

        if self.player_pos_x < self.rect.left:
            self.rect.move_ip(-self.max_speed, 0)
            if pygame.sprite.spritecollide(self, rectangules, False):
                self.rect.move_ip(self.max_speed, 0)
        else:
            self.rect.move_ip(self.max_speed, 0)
            if pygame.sprite.spritecollide(self, rectangules, False):
                self.rect.move_ip(-self.max_speed, 0)

        if self.player_pos_y < self.rect.top:
            self.rect.move_ip(0, -self.max_speed)
            if pygame.sprite.spritecollide(self, rectangules, False):
                self.rect.move_ip(0, self.max_speed)
        else:
            self.rect.move_ip(0, self.max_speed)
            if pygame.sprite.spritecollide(self, rectangules, False):
                self.rect.move_ip(0, -self.max_speed)


enemies = pygame.sprite.Group()
enemy_left = Enemy(player.rect.left, player.rect.top, 10, HEIGHT / 2)
enemy_right = Enemy(player.rect.left, player.rect.top, WIDTH - 10, HEIGHT / 2)
enemies.add(enemy_left, enemy_right)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load('assets/background.png')
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT