###############################################################
#
#   Project Requirements:
#   Authorship
#   Loop
#   Conditional
#   Writing
#   Beauty
#   Made by: Faisal Kassem
#   Student No: 404386
###############################################################

import turtle
import keyboard
import time

MAX_SPIRALS = 500

class Timer:
    def __init__(self) -> None:
        self.timeVar = time.perf_counter()
    
    def timeDiff(self):
        return time.perf_counter() - self.timeVar

    def tick(self):
        self.timeVar = time.perf_counter()

class Dumper:
    def dump(self, dataSet):
        s = "color: " + dataSet[0][0][dataSet[0][1]] + "\n" + "radius: "  + str(dataSet[1][0]) + "\nfillCircle: " + str(dataSet[2][0])
        return s

class DrawObject:
    def __init__(self, coordinates) -> None:
        self.coords = coordinates
    
    def getCoords(self):
        return self.coords

class Drawer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.dumper = Dumper()
        self.timer = Timer()
        turtle.delay(-1)
    def draw_image(self,points: DrawObject, scale = 1):
        po = [[p[0] * scale, p[1] * scale] for p in (points.getCoords())]
        self.t.penup()
        self.t.setx(po[0][0]) 
        self.t.sety(po[0][1])
        self.t.pendown()
        self.t.begin_fill()
        for p in po:
            self.t.goto(p[0], p[1])
        self.t.end_fill()
        self.t.penup()
        self.t.home()
        self.t.pendown()
        return

    def draw_images(self,vec: DrawObject, scale=1):
        for i in vec.getCoords():
            self.draw_image(i, scale)

    def move_image_x_by(self,points, by):
        for i in points.getCoords():
            i[0] += by


    def move_image_y_by(self,points, by):
        for i in points.getCoords():
            i[1] += by
    
    def setColor(self,cl1, cl2):
        self.t.color(cl1, cl2)
    
    def setBgrnd(self,cl):
        turtle.bgcolor(cl)

    def draw_spiral(self,at, rng):
        self.t.penup()
        self.t.goto(at[0],at[1])
        self.t.pendown()
        r = 10
        for i in range(rng):
            self.t.circle(r + i, 45)
        self.t.penup()
        self.t.home()
        self.t.pendown()
    
    def setPenWidth(self, width):
        self.t.width(width=width)

    def erasableWrite(self,tortoise, name, font, align, reuse=None):
        eraser = turtle.Turtle() if reuse is None else reuse
        eraser.color("red")
        eraser.hideturtle()
        eraser.up()
        eraser.setpos(tortoise.position())
        eraser.write(name, font=font, align=align)
        return eraser

    def enableDrawing(self):
        self.t.penup()
        self.t.goto(-100,24)
        screen = turtle.Screen()
        screen.addshape('brskicon.gif')
        self.t.shape('brskicon.gif')
        x = 0 # home loc 
        y = 0 # home loc
        self.t.width(10)
        colorIndex = 0
        colors = ['red', 'blue', 'yellow', 'green']
        clickedOnce = False
        radius = 100

        dataSet = [
            [colors, colorIndex],
            [radius],
            [False] # fillCircle
        ]
        self.t.goto(-200,-200)
        erasable = self.erasableWrite(self.t, "", font=("Arial", 20, "normal"), align="center")
        tt = turtle.Turtle()
        tt.hideturtle()
        tt.up()
        tt.goto(-300, -300)

        fillCircle = False
        while(not keyboard.is_pressed('z')):
            stateChanged = False
            if keyboard.is_pressed('a'):
                x -= 0.4
                self.t.goto(x,y)
            if keyboard.is_pressed('d'):
                x+=0.4
                self.t.goto(x,y)
            if keyboard.is_pressed('s'):
                y-=0.4
                self.t.goto(x,y)
            if keyboard.is_pressed('w'):
                y+=0.4
                self.t.goto(x,y)
            if keyboard.is_pressed('c') and (self.timer.timeDiff() >= 0.2):
                colorIndex = (colorIndex+1)%(len(colors))
                self.t.color(colors[colorIndex],'red')
                stateChanged = True
                self.timer.tick()
            if keyboard.is_pressed('f') and (self.timer.timeDiff() >= 0.2):
                fillCircle = not fillCircle
                stateChanged = True
                self.timer.tick()
            if keyboard.is_pressed('1'):
                self.t.fillcolor(colors[colorIndex])
                self.t.pencolor(colors[colorIndex])
                if fillCircle:
                    self.t.begin_fill()
                self.t.down()
                self.t.circle(radius=radius)
                self.t.up()
                if fillCircle:
                    self.t.end_fill()
            if keyboard.is_pressed('up arrow')  and (time.perf_counter() - timerVar >= 0.2):
                    radius += 10
                    stateChanged = True
                    timerVar = time.perf_counter()
            if keyboard.is_pressed('down arrow')  and (time.perf_counter() - timerVar >= 0.2):
                    radius -= 10
                    stateChanged = True
                    timerVar = time.perf_counter()
            if keyboard.is_pressed('space'):
                    self.t.pendown()
            else:
                    self.t.penup()
    
            if stateChanged:
                    dataSet = [
                        [colors, colorIndex],
                        [radius],
                        [fillCircle]
                    ]
                    logData = self.dumper.dump(dataSet=dataSet)
                    erasable.clear()
                    erasable = self.erasableWrite(tt, logData, font=("Arial", 20, "normal"), align="center")


class Application:
    def __init__(self) -> None:
        self.Drw = Drawer()

    def init(self):
        bsign = DrawObject([
                [392,802],
                [576,622],
                [422,472],
                [575,324],
                [473,223],
                [529,325],
                [405,436],
                [405,248],
                [422,211],
                [399,226],
                [392,185],
                [383,226],
                [362,211],
                [379,247],
                [378,437],
                [252,324],
                [311,227],
                [206,324],
                [360,472],
                [207,620],
                [392,802]
        ])

        bsignW1 = DrawObject([
                [258,623],
                [378,740],
                [377,513],
                [258,623]
        ])

        bsignW2 = DrawObject([
                [404,738],
                [404,512],
                [525,623],
                [404,738]
        ])

        japL1 = DrawObject([
                [1,124],
                [29,107],
                [51,155],
                [112,6],
                [132,29],
                [109,88],
                [138,145],
                [119,153],
                [101,109],
                [67,200],
                [39,187],
                [42,179],
                [28,177],
                [1,124]
        ])
        japlcs1 = DrawObject([
        DrawObject([
                [79,184],
                [84,164],
                [117,202],
                [100,216],
                [79,184]
        ]),
        DrawObject([
                [97,170],
                [107,153],
                [133,179],
                [118,193],
                [96,170]
        ])
        ])
        
        japL2 = DrawObject([
                [141,178],
                [131,76],
                [146,69],
                [186,117],
                [177,120],
                [156,106],
                [168,178],
                [141,178]
        ])

        japL3 = DrawObject([
                [209,190],
                [200,150],
                [166,144],
                [172,122],
                [194,127],
                [187,86],
                [196,76],
                [241,102],
                [235,114],
                [208,102],
                [213,131],
                [228,135],
                [224,124],
                [235,120],
                [259,157],
                [219,154],
                [224,181],
                [221,188],
                [210,190]
        ])

        japL4 = DrawObject([
                [267,182],
                [224,50],
                [243,53],
                [293,174],
                [267,182]
        ])

        japL5 = DrawObject([
                [280,140],
                [269,91],
                [281,78],
                [329,112],
                [322,122],
                [293,106],
                [299,135],
                [280,140]
        ])

        japL6 = DrawObject([
                [327,213],
                [291,151],
                [293,142],
                [310,133],
                [323,153],
                [355,156],
                [283,11],
                [312,1],
                [389,155],
                [389,164],
                [384,171],
                [378,179],
                [339,180],
                [350,199]
        ])


        self.Drw.setColor('black','red')
        self.Drw.move_image_x_by(bsign, -360)
        self.Drw.move_image_y_by(bsign, -400)

        self.Drw.move_image_x_by(bsignW1, -360)
        self.Drw.move_image_y_by(bsignW1, -400)

        self.Drw.move_image_x_by(bsignW2, -360)
        self.Drw.move_image_y_by(bsignW2, -400)
        self.Drw.draw_image(bsign)
        self.Drw.setColor('black','black')
        self.Drw.draw_image(bsignW1)
        self.Drw.draw_image(bsignW2)
        self.Drw.setBgrnd("black")
        self.Drw.setColor('black', 'red')
        tmp = [
            japL1,
            japL2,
            japL3,
            japL4,
            japL5,
            japL6
        ]

        for i in tmp:
            self.Drw.move_image_x_by(i, -200)
            self.Drw.move_image_y_by(i, -410)
            self.Drw.draw_image(i)

        for i in japlcs1.getCoords():
            self.Drw.move_image_x_by(i, -200)
            self.Drw.move_image_y_by(i, -410)

        self.Drw.draw_images(japlcs1)


        self.Drw.setColor('red','red')

        self.Drw.draw_spiral([-960, 450],MAX_SPIRALS)

        self.Drw.draw_spiral([960, -450], MAX_SPIRALS)

        self.Drw.enableDrawing()

        turtle.done()


    def run(self):
        self.init()

def main():
    Application().run()

if __name__ == "__main__":
    main()