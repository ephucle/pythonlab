from swampy.TurtleWorld import *
import time
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

draw(bob, 20, 12)
wait_for_user()