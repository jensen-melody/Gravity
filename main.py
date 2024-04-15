from turtle import *
import time,turtle,math

#var setup
G = 20
planets = []

#Screen setup
screen = Screen() #Runs the screen's constructor to create it!
screen.bgcolor('black')
screen.setup(width=800,height=800) #Sets the size of your window in pixels
screen.tracer(0)

#planet class
class planet(Turtle):

    def __init__(self, x, y, dx, dy, mass, size, color, pen=False):
        self.mass = mass
        self.dx = dx
        self.dy = dy

        Turtle.__init__(self)
        self.pu()
        if pen == True:
            self.pd()
        self.shape('circle')
        self.goto(x,y)
        self.color(color)
        self.turtlesize(size)

#star class
class star(Turtle):

    def __init__(self, x, y, mass, size, color):
        self.mass = mass

        Turtle.__init__(self)
        self.pu()
        self.shape('circle')
        self.goto(x,y)
        self.color(color)
        self.turtlesize(size)


#run function
def run():
    while True:

        #update screen
        screen.update()
        time.sleep(1/60)

        #update physics
        for i in planets:
            if not isinstance(i, star):
                for j in planets:

                    rx = j.xcor()-i.xcor()
                    ry = j.ycor()-i.ycor()

                    if not (rx == 0 and ry ==0):

                        r = math.sqrt(rx**2+ry**2)

                        fx = (G*i.mass*j.mass*rx)/(r**3)
                        fy = (G*i.mass*j.mass*ry)/(r**3)

                        i.dx += fx/i.mass
                        i.dy += fy/i.mass

        #update position
        for i in planets:
            if not isinstance(i, star):
                i.goto(i.xcor()+i.dx,i.ycor()+i.dy)


#make planets

#star + planet + moon
'''planets.append(star(0,0,200,8,'yellow'))
planets.append(planet(0,200,4.5,0,25,1,'blue'))
planets.append(planet(0,220,9.5,0,1,0.1,'white'))'''
                
#binary system
'''planets.append(planet(100,0,0,1,50,1.5,'red'))
planets.append(planet(-100,0,0,-1,50,1.5,'blue'))'''
                
#star and binary planets
planets.append(star(0,0,200,7,'yellow'))
planets.append(planet(0,250,6,0,25,1,'red'))
planets.append(planet(0,300,1.6,0,25,1,'blue'))

run()
