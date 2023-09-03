from turtle import*


Screen() .bgcolor("black")
width(6)



def draw_square(c, size, n):
    for i in range(n):
        color(c)
        forward(size)
        left(360/n)

draw_square('red', 100, 6)
draw_square('blue', 120, 6) 
draw_square('green', 140, 6)
draw_square('yellow', 160, 6)
draw_square('orange', 180, 6)
draw_square('purple', 200, 6)

mainloop()