from turtle import*
bgcolor('red')
color('gray')
begin_fill()
for i in range(4):
    if i % 2 == 0:
        forward(150)
    else:
        forward(20)
    right(90)
end_fill()

penup()
forward(60)
pendown()

color('white')
begin_fill()
for i in range(4):
    if i % 2 == 0:
        forward(30)
    else:
        forward(40)
    left(90)
end_fill()


penup()
left(90)
forward(40)
left(90)
forward(130)
pendown()




color('gray')
begin_fill()
for i in range(4):
    right(90)
    if i % 2 == 0:
        forward(200)
    else:
        forward(300)
end_fill()



penup()
right(90)
forward(20)
right(90)
forward(20)
pendown()



color('black')
begin_fill()
for i in range(4):
    if i % 2 == 0:
        forward(260)
    else:
        forward(160)
    left(90)
end_fill()




penup()
forward(115)
right(90)
forward(10)
pendown()


color('white')
begin_fill()
circle(7.5)
end_fill()



penup()
forward(100)
mainloop()