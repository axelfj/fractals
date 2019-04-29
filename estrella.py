from turtle import *

def estrella(profundidad):
    def estrellaAux(profundidad, lado):
        if profundidad == 0:
            return
        else:
            for i in range(5):
                estrellaAux(profundidad - 1, lado * 1/3)
                forward(lado)
                right(144)
    if isinstance(profundidad, int) and profundidad > 0:
        speed(0)
        tracer(0, 0)
        hideturtle()
        estrellaAux(profundidad, 500)
        update()
    else:
        return "La profundidad debe ser entero positivo"

tracer(0, 0)
speed(0)
hideturtle()
estrella(5)
update()
