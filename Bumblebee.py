import pgzrun
import pgzero
import pygame
import random
WIDTH = 1000
HEIGHT = 1000
score = 0
gameo=False
bee=Actor("bee")
bee.pos=300, 400
flower=Actor("flower")
flower.pos=100, 200
def draw():
    screen.blit("background", (0, 0))
    flower.draw()
    bee.draw()
def displaceflower():
    flower.x=random.randint(50, 950)
    flower.y=random.randint(50, 950)
def update():
    global score
    if keyboard.left:
        bee.x-=2
    elif keyboard.right:
        bee.x+=2
    elif keyboard.up:
        bee.y-=2
    elif keyboard.down:
        bee.y+=2
    if bee.colliderect(flower):
        score+=1
        displaceflower()
pgzrun.go()