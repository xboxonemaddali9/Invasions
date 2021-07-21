import pygame
import math

class Character (pygame.sprite.Sprite):
    def __init__(self, scaleFactor, startingPos, speed, animsDirList, bulletImage):
        # initialising sprite logic
        pygame.sprite.Sprite.__init__(self)

        self.animsDirList = animsDirList
        self.anim = self.animsDirList[0]

        self.scaleFactor = scaleFactor
        
        self.image = pygame.image.load(self.anim.framesList[0]).convert_alpha()
        # establishing a rect object on the player, and setting its coordinates
        self.rect = self.image.get_rect(center=startingPos)
        self.scaleFactor = scaleFactor
        
        # speed is an unchanged magnitude 
        self.speed = [list(speed)[0], list(speed)[1]]
        # whereas velocity changes based on direction
        self.velocity = [list(speed)[0], list(speed)[1]]
        maxVelocity = (max(self.velocity[0], self.velocity[1]))
        self.diagonalSpeed = [math.sqrt((maxVelocity**2)/2), math.sqrt((maxVelocity**2)/2)]

        


        self.bulletImage = bulletImage
        self.bullets = []

        self.flipSprite = False


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, size, velocity, startingPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.imagesList = []
        self.rect = self.image.get_rect()
        self.rect.x = startingPos[0]
        self.rect.y = startingPos[1]
        self.size = size
        self.velocity = velocity
        self.i = 0

    def InitVelocity(self, plyrVelocity, flipSprite):
        # only sets the velocity initialisation once
        while self.i < 1:
            # j iterates as 0 and 1, and therefore manipulates each index of 
            # velocities of player and bullet at the same time
            for j in range(len(plyrVelocity) - 1):
                # if when the player shoots, the player is facing left
                if flipSprite:
                    self.velocity[j] = -(abs(plyrVelocity[j]) + self.velocity[j])
                # ...or facing right
                elif flipSprite == False:
                    self.velocity[j] = abs(plyrVelocity[j]) + self.velocity[j]
            self.i += 1
