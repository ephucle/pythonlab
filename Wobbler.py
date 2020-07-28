"""

This module is part of an exercise for
Think Python: an Introduction to Software Design
Allen B. Downey

"""
#https://greenteapress.com/wp/swampy/
from swampy.TurtleWorld import TurtleWorld, Turtle
#from TurtleWorld import *
from random import randint

class Wobbler(Turtle):
    """a Wobbler is a kind of Turtle with attributes for speed and
    clumsiness."""

    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Turtle.__init__(self, world)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.color = color

        # move to the starting position
        self.pu()  #Puts the pen up (inactive).
        self.rt(randint(0,360)) #rt(self, angle=90) Turns right by the given angle.
        self.bk(150) #bk(self, dist=1) Moves the turtle backward by the given distance.

    def step(self):
        """step is invoked by TurtleWorld on every Wobbler, once
        per time step."""
        
        self.steer()
        self.wobble()
        self.move()

    def move(self):
        """move forward in proportion to self.speed"""
        self.fd(self.speed)

    def wobble(self):
        """make a random turn in proportion to self.clumsiness"""
        dir = randint(0,self.clumsiness) - randint(0,self.clumsiness)
        self.rt(dir)

    def steer(self):
        """steer the Wobbler in the general direction it should go.
        Postcondition: the Wobbler's heading may be changed, but
        its position may not."""
        self.rt(10)

def make_world(constructor):
    #constructor ~ Wobbler
    # create TurtleWorld
    world = TurtleWorld()
    world.delay = 2
    world.setup_run()   #setup_run(self)  Adds a row of buttons for run, step, stop and clear.

    # make three Wobblers with different speed and clumsiness attributes
    colors = ['orange', 'green', 'purple' ]
    i = 1.0
    for color in colors:
        t = constructor(world, i, i*30, color) #Wobbler.__init__(self, world, speed=1, clumsiness=60, color='red')
        i += 0.5

    return world

if __name__ == '__main__':
    world = make_world(Wobbler)
    world.mainloop()
