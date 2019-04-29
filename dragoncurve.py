from random import randrange
from turtle import *

variacionColor = 3
minimoColor = 50

color = []

def restringir(n):
    if n < minimoColor:
        return minimoColor
    elif n > 255:
        return 255
    else:
        return n

def colorInicial():
    global color
    color = [randrange(256), randrange(256), randrange(256)]
    color = [restringir(x) for x in color]
    pencolor(tuple(color))

def alterarColor():
    global color
    color = [restringir(x + randrange(variacionColor) + 1 - variacionColor / 2) for x in color]
    color = [int(x) for x in color]
    pencolor(tuple(color))

def generarInstrucciones(profundidad):
    instrucciones = "R"
    for i in range(profundidad):
        res = ""
        sig = "R"
        for inst in instrucciones:
            res += sig + inst
            sig = "L" if sig == "R" else "R"
        instrucciones = res
            
    return instrucciones

def dragonCurve(segmento, profundidad, angulo):
    instrucciones = generarInstrucciones(profundidad)
##    reset()
    penup()
    home()
    pendown()
    hideturtle()
    tracer(0, 0)
    for instruccion in instrucciones:
        alterarColor()
        forward(segmento)
        if instruccion == "R":
            right(angulo)
        else:
            left(angulo)
    update()

def inicializacion():
    speed(0)
    hideturtle()
    colormode(255)
    bgcolor(0, 0, 0)
    colorInicial()

angulo = 0
inicializacion()
while True:
    dragonCurve(11, 11, angulo)
    angulo += 5
