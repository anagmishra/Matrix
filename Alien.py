import pgzrun
import random
WIDTH = 500
HEIGHT = 500
alien = Actor("download")
alien.x = 50
alien.y = 50
message = ""
def draw():
    screen.fill("cyan")
    alien.draw()
    screen.draw.text(message,(400, 400))

def on_mouse_down(pos):
    global message
    #print("Hello")
    #print(alien.collidepoint(pos))
    if alien.collidepoint(pos)==True:
        alien.x = random.randint(50, 450)
        alien.y = random.randint(50, 450)
        message = "Good shot"
    else:
        message = "You missed!"
pgzrun.go()