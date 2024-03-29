import pygame
import os

class player:

    #initialize data from other file
    def __init__(self, qr):
        self.qr = qr #welcome stuff from the other file

    #render player
    def render(self):
        self.qr.screen.blit(self.qr.playerImg, (self.qr.playerX, self.qr.playerY))

    #too advanced for my sanity movement script
    def movement(self):

        #up
        if self.qr.up and (not self.qr.down): #if up and not down
            #only up
            if ((not (self.qr.right or self.qr.left)) or (self.qr.right and self.qr.left)) and self.qr.playerY >= self.qr.speed: #if not going right or left OR going right and left AND you are not too high up to go out of bounds
                if self.qr.playerY >= self.qr.speed: #if not too high
                    self.qr.playerY += -self.qr.speed #move up by set speed

            #up and right
            elif self.qr.right and (not self.qr.left): #if going right and not left

                #diaginal movement top right by set speed
                if self.qr.playerX+32 <= self.qr.screenWidth-self.qr.speed: #if not too far right
                    self.qr.playerX += (self.qr.speed / (2**(1/2))) #move right by set speed
                    #print((self.qr.speed / (2**(1/2))))
                if self.qr.playerY >= self.qr.speed: #if not too far up
                    self.qr.playerY += -(self.qr.speed / (2**(1/2))) #move up by set speed

            #up and left
            elif self.qr.left and (not self.qr.right): #if left and not right

                #diaginal movement top left by set speed
                if self.qr.playerX >= -self.qr.speed: #if not too far left
                    self.qr.playerX += -(self.qr.speed / (2**(1/2))) #move left by set speed
                    #print(-(self.qr.speed / (2**(1/2))))
                if self.qr.playerY >= -self.qr.speed: #if not too far up
                    self.qr.playerY += -(self.qr.speed / (2**(1/2))) #move up by set speed

        #down
        elif self.qr.down and (not self.qr.up): #if down and not up

            #only down
            if ((not (self.qr.right or self.qr.left)) or (self.qr.right and self.qr.left)) and self.qr.playerY+32 >= self.qr.speed: #if not right or left OR right and left and not too far down
                if self.qr.playerY+32 <= self.qr.screenHeight - self.qr.speed: #if not too far down
                    self.qr.playerY += self.qr.speed #move down by set speed

            #down and right
            elif self.qr.right and (not self.qr.left): #if right and not left

                #diaginal movement bottom right by set speed
                if self.qr.playerX+32 <= self.qr.screenWidth-self.qr.speed: #if not too far right
                    self.qr.playerX += (self.qr.speed / (2**(1/2))) #move right by set speed
                    #print((self.qr.speed / (2**(1/2))))
                if self.qr.playerY+32 <= self.qr.screenHeight - self.qr.speed: #if not too far down
                    self.qr.playerY += (self.qr.speed / (2**(1/2))) #move down by set speed

            #down and left
            elif self.qr.left and (not self.qr.right): 

                #diaginal movement bottom left by set speed
                if self.qr.playerX >= -self.qr.speed: #if not too far left
                    self.qr.playerX += -(self.qr.speed / (2**(1/2))) #move left bt set speed
                    #print(-(self.qr.speed / (2**(1/2))))
                if self.qr.playerY+32 <= self.qr.screenHeight - self.qr.speed: #if not too far down
                    self.qr.playerY += (self.qr.speed / (2**(1/2))) #move down by set speed
        
        #right
        elif self.qr.right and (not self.qr.left): #if right and not left
            if self.qr.playerX+32 <= self.qr.screenWidth-self.qr.speed: #if not too far right
                self.qr.playerX += self.qr.speed #move right by set speed
                #print(self.qr.speed)

        #left
        elif self.qr.left and (not self.qr.right): #if left and not right
            if self.qr.playerX >= self.qr.speed: #if not too far left
                self.qr.playerX += -self.qr.speed #move left by set speed
                #print(-self.qr.speed)

    #level system
    bullets_shot = 1

    class lvl:
        def hp(self):
            pass

        def gun_type(self, power):
            pass

    #collision system
    class hitbox:
        def walls_hit(self):
            pass
        def projectile_hit(self):
            pass
