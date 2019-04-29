from turtle import *

## Lista de Movimientos ##
## Entradas: Recibe un nùmero entero
## Salidas: Una lista con los movimientos a realizar en el fractal##
## Restricciones: El nùmero debe ser entero, mayor que 0 (si se desea la lista
## con elementos) ##

def movimientos(n):
    if isinstance (n, int):
        if n == 0:
            return []
        else:
            i = ['D' if u == 'I' else 'I' for u in movimientos(n-1)[::-1]]
            return movimientos(n-1) + ['D'] + i
    else:
        return "Debe ser un nùmero entero"

## Dibujo Dragon ##
## Entradas: Recibe un nùmero entero y la distancia a moverse ##
## Salidas: Nos retorna el fractal
## Restricciones: Si el digito 'n' es muy grande, es probable que turtle
## dure demasiado, por lo que es recomendable usar nùmeros pequeños.
## La distancia debe ser acorde al nùmero entero que se digite.
## El par ordenado (16,1) entrega la curva del dragón.
    
def curvaDragon(n,d):    
    speed(0)
    tracer(0,0)
    update()
    forward(d)
    for i in movimientos(n):
        if i == 'D':
            rt(90)
        else:
            lt(90)
        forward(d)
    exitonclick()

curvaDragon(16,1)