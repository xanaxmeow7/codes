from turtle import*
import tkinter as tk

# def draw_sqare():
#     for i in range(4):
#         forward(100)
#         right(90)

# draw_sqare()
# mainloop()




size = 50
width(2)
speed(1000)


def draw_sqare():
    for i in range(4):
        forward(100)
        right(90)



def draw_trangle():
    for i in range(3):
        forward(100)
        right(120)


def draw_circle():
    circle(size)


def draw_star():
    for i in range(5):
        forward(size)
        right(144)

def draw_desyatiygolnik():
    for i in range(10):
        forward(size)
        right(360/10)

def draw_petnatcad():
    for i in range(15):
        forward(size)
        right(360/15)


def draw_suare_circle():
    for i in range(12):
        draw_sqare()
        right(30)


def draw_trangle_cirle():
    for i in range(12):
        draw_trangle()
        right(30)



def draw_circle_cirle():
    for i in range(12):
        draw_circle()
        right(30)



def draw_star_cirle():
    for i in range(12):
        draw_star()
        right(30)


def draw_desyatiygolnik_cirle():
    for i in range(12):
        draw_desyatiygolnik()
        right(30)


def draw_petnatcad_cicle():
     for i in range(12):
        draw_petnatcad()
        right(30)



def keyboard_input():
    command = input_text.get()

    if command == "круг":
        draw_circle()
    elif command == "треугольник":
        draw_trangle()
    elif command == "квадрат":
        draw_sqare()
    elif command == "звезда":
        draw_star()
    elif command == "догектагон":
        draw_desyatiygolnik()
    elif command == "догектагон 15":
        draw_petnatcad()
    elif command == "круг в круге":
        draw_circle_cirle()
    elif command == "треугольник в круге":
        draw_trangle_cirle()
    elif command == "квадрат в круге":
        draw_suare_circle()
    elif command == "звезда в круге":
        draw_star_cirle()
    elif command == "догектагон в круге":
        draw_desyatiygolnik_cirle()
    elif command == "догектагон 15 в круге":
        draw_petnatcad_cicle()
    elif command == "вправо":
        up()
        forward(150)
        down()
    elif command == "влево":
        up()
        backward(150)
        down()
    elif command == "вверх":
        up()
        left(90)
        forward(150)
        right(90)
        down()
    elif command == "вниз":
        up()
        right(90)
        forward(150)
        left(90)
        down()


commands_label1 = tk.Label(
    text ='круг, квадрат, треугольник, звезда, догектагон, догектагон 15',
    width = 100,
    font = ("Arial", 10)
)
commands_label1.pack()
commands_label2 = tk.Label(
    text ='круг в круге, квадрат в круге, треугольник в круге, звезда в круге, догектагон в круге, догектагон 15 в круге',
    width = 100,
    font = ("Arial", 10)
)
commands_label2.pack()
commands_label3 = tk.Label(
    text ='вправо, влево, вверх, вниз',
    width = 100,
    font = ("Arial", 10)
)
commands_label3.pack()

input_text = tk.Entry(
    text = 'Введите название фигуры',
    width = 100,
    font = ("Ariel", 10)
)
input_text.pack()

button_name = tk.Button(
    text = "нарисовать",
    command = keyboard_input,
    width = 100,
    font = ('Arial', 20)

)
button_name.pack()

mainloop()