#The First Project: Requirements
#Authorship
#Loop
#Conditional
#Writing
#sBeauty
import turtle
import keyboard
import time
# try to use the class in the code

MAX_SPIRALS = 500

class drawable_obj:
    pass

t = turtle.Turtle()
turtle.delay(-1)
def draw_image(points, scale = 1):
    po = [[p[0] * scale, p[1] * scale] for p in points]
    t.penup()
    t.setx(po[0][0]) 
    t.sety(po[0][1])
    t.pendown()
    t.begin_fill()
    for p in po:
        t.goto(p[0], p[1])
    t.end_fill()
    t.penup()
    t.home()
    t.pendown()
    return

def draw_images(vec, scale=1):
    for i in vec:
        draw_image(i, scale)

def move_image_x_by(points, by):
    for i in points:
        i[0] += by


def move_image_y_by(points, by):
    for i in points:
        i[1] += by

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.color("red")
    eraser.hideturtle()
    eraser.up()
    eraser.setpos(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


def dump(dataSet):
    s = "color: " + dataSet[0][0][dataSet[0][1]] + "\n" + "radius: "  + str(dataSet[1][0]) + "\nfillCircle: " + str(dataSet[2][0])
    return s

def draw_spiral(at, rng):
    t.penup()
    t.goto(at[0],at[1])
    t.pendown()
    r = 10
    for i in range(rng):
        t.circle(r + i, 45)
    t.penup()
    t.home()
    t.pendown()
    
arr = [
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
]
tr1 = [
[258,623],
[378,740],
[377,513],
[258,623]
]

tr2 = [
[404,738],
[404,512],
[525,623],
[404,738]
]


jl1 = [
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
]
jlcs1 = [
[
[79,184],
[84,164],
[117,202],
[100,216],
[79,184]
],
[
[97,170],
[107,153],
[133,179],
[118,193],
[96,170]
]
]

jl2 = [
[141,178],
[131,76],
[146,69],
[186,117],
[177,120],
[156,106],
[168,178],
[141,178]
]

jl3 = [
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
]

jl4 = [
[267,182],
[224,50],
[243,53],
[293,174],
[267,182]
]

jl5 = [
[280,140],
[269,91],
[281,78],
[329,112],
[322,122],
[293,106],
[299,135],
[280,140]
]

jl6 = [
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
]

scale = 1

t.color('black','red')


move_image_x_by(arr, -360)
move_image_y_by(arr, -400)

move_image_x_by(tr1, -360)
move_image_y_by(tr1, -400)

move_image_x_by(tr2, -360)
move_image_y_by(tr2, -400)
draw_image(arr)
t.color('black','black')
draw_image(tr1)
draw_image(tr2)
turtle.bgcolor("black")

t.color('black','red')
# can be combines and automated somehow
move_image_x_by(jl1, -200)
move_image_y_by(jl1, -410)

# change method
for i in jlcs1:
    move_image_x_by(i, -200)
    move_image_y_by(i, -410)

move_image_x_by(jl2, -200)
move_image_y_by(jl2, -410)

move_image_x_by(jl3, -200)
move_image_y_by(jl3, -410)

move_image_x_by(jl4, -200)
move_image_y_by(jl4, -410)

move_image_x_by(jl5, -200)
move_image_y_by(jl5, -410)

move_image_x_by(jl6, -200)
move_image_y_by(jl6, -410)

draw_image(jl1)
draw_images(jlcs1)
draw_image(jl2)
draw_image(jl3)
draw_image(jl4)
draw_image(jl5)
draw_image(jl6)


# add input to add some conditional statement
t.color('red','red')
#draw_spiral([-960, 450],MAX_SPIRALS)

#draw_spiral([960, -450], MAX_SPIRALS)

t.penup()
t.goto(-100,24)
screen = turtle.Screen()
screen.addshape('brskicon.gif')
t.shape('brskicon.gif')
#screen.register_shape('brskicon.gif')
#turtle.shape('brskicon.gif')
#turtle.setheading(90)


x = 0 # home loc 
y = 0 # home loc
t.width(10)
colorIndex = 0
colors = ['red', 'blue', 'yellow', 'green']
clickedOnce = False
radius = 100

dataSet = [
    [colors, colorIndex],
    [radius],
    [False] # fillCircle
]

t.goto(-200,-200)
erasable = erasableWrite(t, "", font=("Arial", 20, "normal"), align="center")
tt = turtle.Turtle()
tt.hideturtle()
tt.up()
tt.goto(-300, -300)

timerVar = time.perf_counter()
fillCircle = False
while(not keyboard.is_pressed('z')):
    stateChanged = False
    if keyboard.is_pressed('a'):
        x -= 0.4
        t.goto(x,y)
    if keyboard.is_pressed('d'):
        x+=0.4
        t.goto(x,y)
    if keyboard.is_pressed('s'):
        y-=0.4
        t.goto(x,y)
    if keyboard.is_pressed('w'):
        y+=0.4
        t.goto(x,y)
    if keyboard.is_pressed('c') and (time.perf_counter() - timerVar >= 0.2):
        colorIndex = (colorIndex+1)%(len(colors))
        t.color(colors[colorIndex],'red')
        stateChanged = True
        timerVar = time.perf_counter()
    if keyboard.is_pressed('f') and (time.perf_counter() - timerVar >= 0.2):
        fillCircle = not fillCircle
        timerVar = time.perf_counter()
        stateChanged = True
    if keyboard.is_pressed('1'):
        t.fillcolor(colors[colorIndex])
        t.pencolor(colors[colorIndex])
        if fillCircle:
            t.begin_fill()
        t.down()
        t.circle(radius=radius)
        t.up()
        if fillCircle:
            t.end_fill()
    if keyboard.is_pressed('up arrow')  and (time.perf_counter() - timerVar >= 0.2):
        radius += 10
        stateChanged = True
        timerVar = time.perf_counter()
    if keyboard.is_pressed('down arrow')  and (time.perf_counter() - timerVar >= 0.2):
        radius -= 10
        stateChanged = True
        timerVar = time.perf_counter()
    if keyboard.is_pressed('space'):
        t.pendown()
    else:
        t.penup()
    
    if stateChanged:
            dataSet = [
            [colors, colorIndex],
            [radius],
            [fillCircle]
        ]
            logData = dump(dataSet=dataSet)
            erasable.clear()
            erasable = erasableWrite(tt, logData, font=("Arial", 20, "normal"), align="center")


turtle.done()

