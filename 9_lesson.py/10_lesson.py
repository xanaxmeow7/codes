from turtle import*
# color("cyan")
# begin_fill()
# forward(200)
# right(120)
# forward(200)
# right(120)
# forward(200)
# end_fill()
# mainloop()








# number = 0
# while True:
#     print(number)
#     number = number + 1




# import random
# import time 

# summa = 0
# while True:
#     number = random.randint(5, 10)
#     time.sleep(0.1)
#     summa += number
#     print(summa)




# choice = input('Enter color ')

# while choice != 'stop':
#     color(choice)
#     begin_fill()
#     forward(200)
#     right(90)
#     forward(100)
#     right(90)
#     forward(200)
#     right(90)
#     forward(100)
#     end_fill()
#     choice = input('Enter color ')
# mainloop()











one_circle = 10
biggest_circle = 500

while one_circle <= biggest_circle:
    color("cyan")
    begin_fill()
    circle(one_circle)
    end_fill()
    one_circle += 10
    speed(15)

mainloop()