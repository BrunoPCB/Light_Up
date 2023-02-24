import pygame.sprite
#import main


class Screen:
    __width = 0
    __height = 0

    def __init__(self, prHeight, prWidth):
        self.__width = prWidth
        self.__height = prHeight

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, pr_width):
        self.__width = pr_width

    @height.setter
    def height(self, pr_height):
        self.__height = pr_height


class Player:
    __height = 0
    __width = 0
    __color = (0, 0, 0)
    __posX = 0
    __posY = 0

    @property
    def posX(self):
        return self.__posX

    @property
    def posY(self):
        return self.__posY

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def color(self):
        return self.__color

    @posX.setter
    def posX(self, prPosX):
        self.__posX = prPosX

    @posY.setter
    def posY(self, prPosY):
        self.__posY = prPosY

    @width.setter
    def width(self, pr_width):
        self.__width = pr_width

    @height.setter
    def height(self, pr_height):
        self.__height = pr_height

    @color.setter
    def color(self, pr_color):
        self.__color = pr_color


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animate = False
        self.frog = []
        self.frog.append(pygame.image.load('sprites/frog/attack_1.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_2.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_3.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_4.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_5.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_6.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_7.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_8.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_9.png'))
        self.frog.append(pygame.image.load('sprites/frog/attack_10.png'))
        self.atual = 0
        self.image = self.frog[self.atual]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))

        # Local do criação do sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

    def attack(self):
        self.animate = True

    def update(self):
        if self.animate:
            self.atual += 0.3
            if self.atual >= len(self.frog):
                self.atual = 0
                self.animate = False
            self.image = self.frog[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))


class Walkmann(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walkman = []
        self.walkman.append(pygame.image.load('sprites/walkman/walkman0.png'))
        self.walkman.append(pygame.image.load('sprites/walkman/walkman1.png'))
        self.atual = 0
        self.image = self.walkman[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 200

    def update(self):
        self.atual += 0.5
        if self.atual >= len(self.walkman):
            self.atual = 0
        self.image = self.walkman[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))

'''
class Walkman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walkman = []
        self.sprites = main.spiteSheet["player"].get_width() / 32
        for i in range(self.sprites):
            img = main.spiteSheet.subsurface((i * 2, 0), (32, 32))
            self.walkman.append(img)

        self.indexSprites = 0
        self.image = self.walkman[self.indexSprites]

        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self):
        self.indexSprites += 0.25
        if self.indexSprites > (len(self.walkman)-1):
            self.indexSprites = 0
        self.image = self.walkman[int(self.indexSprites)]

'''