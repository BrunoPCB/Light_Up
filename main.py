from random import randrange

import pygame
from pygame.locals import *
from sys import exit
from classes import *
import os

pygame.init()

# Tela
mainScreen = Screen
mainScreen.width = 640
mainScreen.height = 480
screen = pygame.display.set_mode((mainScreen.width, mainScreen.height))

# Imagem
Image = 'Vela_walk.png'

# Relogio
clock = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Diretórios
dirMain = os.path.dirname(__file__)
dirWalkman = os.path.join(dirMain, 'sprites/walkman/spritesheet/walkman.png')
dirBush = os.path.join(dirMain, 'sprites/walkman/spritesheet/bush.png')
dirSounds = os.path.join(dirMain, 'audio/sounds')

# Sprite
all_sprites = pygame.sprite.Group()

spriteSheet = {"player": pygame.image.load(dirWalkman, 'walkman.png'),
               "bush": pygame.image.load(dirBush, 'bush.png')}


class Walkman(pygame.sprite.Sprite):
    __posX = 100
    __posY = 350
    __tamanho = 64

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def pos_x(self):
        return self.__posX

    @pos_x.setter
    def pos_x(self, x):
        self.__posX = x

    @property
    def pos_y(self):
        return self.__posY

    @pos_y.setter
    def pos_y(self, y):
        self.__posY = y

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walkman = []
        self.sprites = spriteSheet["player"].get_width() // self.__tamanho
        for i in range(0, self.sprites):
            img = spriteSheet["player"].subsurface((i * self.__tamanho, 0), (self.__tamanho, self.__tamanho))
            self.walkman.append(img)

        self.indexSprites = 0
        self.image = self.walkman[self.indexSprites]
        self.image = pygame.transform.scale(self.image, (self.__tamanho * 3, self.__tamanho * 3))

        self.rect = self.image.get_rect()
        #self.rect.center = (100, 350)
        self.rect.center = (self.__posX, self.__posY)

    # def move(self, KEY):
    #     if pygame.key.get_pressed(KEY):
    #         # Movimento
    #     else:
    #        return 'Vela_Idle.png'


    def update(self):
        # self.image = dirWalkman + self.move()
        self.indexSprites += 0.1
        if self.indexSprites > (len(self.walkman)):
            self.indexSprites = 0
        self.rect.center = (self.__posX, self.__posY)
        self.image = self.walkman[int(self.indexSprites)]
        self.image = pygame.transform.scale(self.image, (self.__tamanho * 3, self.__tamanho * 3))


class Bush(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bush = []
        self.qtdSprites = spriteSheet["bush"].get_width() // 32
        for i in range(0, self.qtdSprites, 1):
            img = spriteSheet["bush"].subsurface((i * 32, 0), (32, 32))
            self.bush.append(img)

        self.indexSprites = 0
        self.image = self.bush[self.indexSprites]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))

        self.rect = self.image.get_rect()
        self.rect.center = (randrange(250, 400), randrange(350, 420))

    def update(self):
        # if self.rect.topright[0] < 0:
        #     self.rect.x = mainScreen.width
        # self.rect.x -= 10
        self.indexSprites += 0.2

        # if self.indexSprites > (len(self.bush) - 1):
        #     self.indexSprites = 0
        #     self.rect.x = mainScreen.width-50
        #     self.rect.y = randrange(350, 400, 50)

        self.image = self.bush[int(self.indexSprites)]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))


walkman = Walkman()
#for i in range(4):
# bush = Bush()
# all_sprites.add(bush)
all_sprites.add(walkman)

background = pygame.image.load('sprites/backgrounds/pathway.jpg').convert()
background = pygame.transform.scale(background, (mainScreen.width, mainScreen.height))

while True:
    clock.tick(60)
    screen.fill(BRANCO)

    for event in pygame.event.get():
        # Fechar
        if event.type == QUIT:
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
        if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
            walkman.pos_x += 5
        if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
            walkman.pos_x -= 5
        # if pygame.key.name(K_w) or pygame.key.name(K_UP):
        if (pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]) and walkman.pos_y >= 280:
               walkman.pos_y -= 10
        if (pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]) and walkman.pos_y <= 340:
            walkman.pos_y += 10

    # if walkman.pos_y == 0:
    #     walkman.pos_x = 0

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
