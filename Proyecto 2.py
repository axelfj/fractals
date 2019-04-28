from turtle import *
import math
import random

#--------------------------------------------------------------------------------------#

# Triangulo de Sierpinski #

# Entradas: Profundidad y lado, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Triangulo de Sierpinski, dibujado con turtle.

# Restricciones: Profundidad y lado deben ser números mayores a 0.
   
def trianguloSierpinskiAux(profundidad,lado):
    ht()
    if profundidad == 0:
        return 
    else:
        for x in range(3):
            lt(120)
            fd(lado)
            trianguloSierpinskiAux(profundidad-1,lado/2)
            
def trianguloSierpinski(profundidad,lado):    
    if isinstance (profundidad, int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        trianguloSierpinskiAux(profundidad,lado)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'

# Triangulo Mod #

# Entrada: Profundidad y lado. Funciona como el triangulo de Sierpinski.

# Salida: Pyramid head acompañado de los triangulos de sierpinski.

# Restricciones: Profundidad y lado deben ser enteros mayores que 0.

def trianguloMod(profundidad,lado):
    bgcolor("black")
    color("white")
    x= Screen()
    x.bgpic("triangle.gif")
    while True:
        for x in range(5):
            clear()
            penup()
            w = random.randrange(-250,250)
            i = random.randrange(-100,100)
            setpos(w,i)
            pendown()
            trianguloSierpinski(profundidad,lado)


#--------------------------------------------------------------------------------------#
    
# Alfombra de Sierpinski #

# Entradas: Profundidad y lado, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Alfombra de Sierpinski, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0
   
def alfombraSierpinskiAux(profundidad,lado):
    ht()
    if profundidad == 0:
        return
    else:
        for x in range(4):
            for i in range(2):
                alfombraSierpinskiAux(profundidad-1,lado/3)
                fd(lado/3)
            fd(lado/3)
            lt(90)               

def alfombraSierpinski(profundidad,lado):    
    if isinstance (profundidad, int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        alfombraSierpinskiAux(profundidad,lado)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'

# AlfombraMod #

# Entradas: Profundidad y lado, usa alfombraSierpinski como base.

# Salidas: La alfombra de Sierpinski varias veces, incluyendo un giro de 100º.
#           Cuando la profundidad es mucha, forma una especie de sol.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0

def alfombraMod(profundidad,lado):
    color("white")
    bgcolor("black")
    while True:
        ht()
        alfombraSierpinski(profundidad,lado)
        rt(100)
        
#--------------------------------------------------------------------------------------#
    
# Hexagono de Sierpinski #

# Entradas: Profundidad y lado, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Hexagono de Sierpinski, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0
   
def hexagonoSierpinskiAux(profundidad,lado):
    ht()
    speed(0)
    if profundidad == 0:
        return
    else:        
        for x in range(6):
            for i in range(3):
                pendown()
                hexagonoSierpinskiAux(profundidad-1,lado/3)
                lt(60)
                begin_fill()
                fd(lado/3)
                end_fill
            lt(60)
            penup()
            fd(lado/3)      
            
def hexagonoSierpinski(profundidad,lado):    
    if isinstance (profundidad, int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        hexagonoSierpinskiAux(profundidad,lado)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'

# HexagonoMod #

# Entradas: Profundidad y lado.

# Salidas: Múltiples hexagonos de sierpinski que hacen un circulo y luego
#           este 'rebota' para dar continuación a otro círculo.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0

def hexagonoMod(profundidad,lado):
    color("orange")
    bgcolor("black")
    for x in range(1000000000000000):
        hexagonoSierpinski(profundidad,lado)
        rt(10)
        fd(10)
        if x%30==0:
            clear()
            hexagonoSierpinski(profundidad,lado)
            rt(80)
            fd(10)
            
#--------------------------------------------------------------------------------------#
    
# Curva de Koch #

# Entradas: Profundidad y lado, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Curva de Koch, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0
   
def kochAux(profundidad,lado):
    ht()
    if profundidad == 1:
        fd(lado/3)
        lt(60)
        fd(lado/3)
        rt(120)
        fd(lado/3)
        lt(60)
        fd(lado/3)
    else:
        kochAux(profundidad-1,lado)
        lt(60)
        kochAux(profundidad-1,lado)
        rt(120)
        kochAux(profundidad-1,lado)
        lt(60)
        kochAux(profundidad-1,lado)
    

def koch(profundidad,lado):
    if isinstance(profundidad, int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        kochAux(profundidad,lado)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'

# Koch Mod #

# Entradas: Profundidad y lado.

# Salidas: Varios Koch unidos con un random en el color.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0.

def kochMod(profundidad,lado):
    ht()
    def kochAux(profundidad,lado):
        ht()
        bgcolor("black")
        if profundidad == 1:
            fd(lado/3)
            lt(60)
            fd(lado/3)
            rt(120)
            fd(lado/3)
            lt(60)
            fd(lado/3)
        else:
            colormode(255)
            color(random.randrange(255),random.randrange(255),random.randrange(255))
            kochAux(profundidad-1,lado)
            lt(60)
            kochAux(profundidad-1,lado)
            rt(120)
            kochAux(profundidad-1,lado)
            lt(60)
            kochAux(profundidad-1,lado)
    if isinstance(profundidad, int) and profundidad > 0:
        while True:
            tracer(0,0)
            speed(0)
            begin_fill()
            kochAux(profundidad,lado)
            end_fill()
            lt(80)
            update()

    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'
    
#--------------------------------------------------------------------------------------#
    
# Círculo de Ravel #

# Entradas: Profundidad y radio, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Círculo de Ravel, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Radio debe ser mayor que 0  

def ravelAux(profundidad,radio):
    ht()
    if profundidad == 0:
        return
    else:
        for x in range(3):
            ravelAux(profundidad-1,radio*6/26) 
            circle(radio,60)
            ravelAux(profundidad-1,radio*46/100)
            circle(radio,60)
            
def ravel(profundidad,radio):
    if isinstance(profundidad,int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        ravelAux(profundidad,radio)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Radio debe ser mayor que 0'

# Ravel Mod #

# Entradas: Profundidad y Radio.

# Salidas: Varios circulos de ravel que hacen ilusión a luces.

# Restricciones: Profundidad debe ser un entero mayor que 0, radio debe ser mayor a 0.

def ravelMod(profundidad,radio):
    ht()
    def ravelAux(profundidad,radio):
        if profundidad == 0:
            return
        else:
            begin_fill()
            ht()
            colormode(255)
            color(random.randrange(255),random.randrange(255),random.randrange(255))
            bgcolor("black")
            for x in range(3):
                ravelAux(profundidad-1,radio*6/26) 
                circle(radio,60)
                ravelAux(profundidad-1,radio*46/100)
                circle(radio,60)
            end_fill()
    if isinstance(profundidad,int) and profundidad > 0:
        while True:
            tracer(0,0)
            speed(0)
            clear()
            ravelAux(profundidad,radio+2)
            rt(60)
            update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Radio debe ser mayor que 0'
    
#--------------------------------------------------------------------------------------#
    
# Curva de Satie #

# Entradas: Profundidad y radio, donde profundidad es la cantidad de veces que se va
#           a repetir la recursión y lado es el largo de cada lado.

# Salidas: Curva de Satie, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0  

def satieAux(profundidad,lado):
    ht()
    if profundidad == 1:
        c = math.sqrt(((lado/2)**2)+((lado/4)**2))
        fd(c)
        rt(117)
        fd(lado/2)
        lt(117)
        fd(c)
    else:
        satieAux(profundidad-1,lado)
        rt(117)
        satieAux(profundidad-1,lado)
        lt(117)
        satieAux(profundidad-1,lado)
        
def satie(profundidad,lado):
    if isinstance(profundidad, int) and profundidad > 0:
        tracer(0,0)
        speed(0)
        lt(27)
        satieAux(profundidad,lado)
        update()
    else:
        return 'Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0'

# Satie Mod #

# Entradas: Profundidad y Lado.

# Salida: Espiral de Saties

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser mayor que 0

def satieMod(profundidad,lado):
    bgcolor("blue")
    color("yellow")
    while True:
        clear()
        for x in range(100):
            satie(profundidad,lado)
            if x%10==0:
                rt(25)
        fd(10)
        rt(40)
    
#--------------------------------------------------------------------------------------#
    
# Estrella de Debussy #

# Entradas: Profundidad, lado, n y relación. Donde profundidad es la cantidad de
#           veces que se repite la recursión, lado es el largo de cada lado,
#           n es la cantidad de picos y relación es el tamaño que va a tener
#           n.

# Salidas: Estrella de Debussy, dibujado con turtle.

# Restricciones: Profundidad debe ser un entero mayor a 0, Lado debe ser
#                   entero mayor que 0, N debe ser mayor entero que 0,
#                   Relación debe ser mayor a 0.

def debussyAux(profundidad, lado, n , relacion):
    ht()
    if profundidad == 0:
        return 
    else:
        for x in range(n - 1):
            rt(180)
            rt(360/n)
            fd(lado)
            debussyAux(profundidad-1, lado*relacion, n, relacion)
            lt(180)
            fd(lado)
        rt(360/n)

def debussy(profundidad, lado, n, relacion):
    if isinstance(profundidad, int) and isinstance(lado,int):
        for x in range(n):
            fd(lado)
            debussyAux(profundidad-1, lado*relacion, n, relacion)
            back(lado)
            rt(360/n)
    else:
        return '''Profundidad debe ser un entero mayor a 0, Lado debe ser
entero mayor que 0, N debe ser mayor entero que 0, Relación debe ser mayor a 0'''

# Debussy Mod #

# Entradas: Profundidad, lado, n y relación.

# Salida: Debussy coloreado.

# Restricciones:Profundidad debe ser un entero mayor a 0, Lado debe ser
#               entero mayor que 0, N debe ser mayor entero que 0,
#               Relación debe ser mayor a 0

def debussyMod(profundidad,lado,n,relacion):
    bgcolor("black")
    color("white")
    def debussyAux(profundidad, lado, n , relacion):
        if profundidad == 0:
            return 
        else:
            for x in range(n - 1):
                rt(180)
                rt(360/n)
                fd(lado)
                debussyAux(profundidad-1, lado*relacion, n, relacion)
                lt(180)
                fd(lado)
            rt(360/n)
    if isinstance(profundidad, int) and isinstance(lado,int):
        for x in range(n):
            while True:
                colormode(255)
                color(random.randrange(255),random.randrange(255),random.randrange(255))
                fd(lado)
                debussyAux(profundidad-1, lado*relacion, n, relacion)
                back(lado)
                rt(360/n)                
    else:
        return '''Profundidad debe ser un entero mayor a 0, Lado debe ser
entero mayor que 0, N debe ser mayor entero que 0, Relación debe ser mayor a 0'''



