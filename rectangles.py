import pgzrun
import random
WIDTH = 300
HEIGHT = 400
def draw():
    r=255
    g=0
    b=random.randint(120, 255)
    w=WIDTH
    h=HEIGHT-200
    for i in range(20):
        rectangle=Rect((0,0),(w,h))
        rectangle.center=150, 200
        screen.draw.rect(rectangle,(r, g, b))
        r-=10
        g+=10
        w-=10
        h+=10
    
pgzrun.go()

