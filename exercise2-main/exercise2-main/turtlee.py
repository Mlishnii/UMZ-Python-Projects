import turtle

def turtlee():
    s = turtle.Screen()
    li = turtle.Turtle()

    li.penup()
    li.forward(200)
    li.pendown()
    li.forward(100)
    li.left(90)
    li.forward(200)
    li.left(90)
    li.penup()
    li.forward(100)
    li.pendown()
    li.left(90)
    li.forward(200)
    li.right(90) #
    li.penup()
    li.forward(50)
    li.pendown()
    li.right(90) #
    li.forward(100)
    li.left(180)
    li.forward(100)
    li.right(90) #
    li.forward(100)
    li.left(90)
    li.forward(200)
    li.right(90) #
    li.forward(100)
    li.left(180)
    li.forward(100)
    li.left(90)
    li.forward(200)
    li.penup()
    li.forward(50)
    li.pendown()
    li.right(90) #
    for _ in range(4):
        li.forward(10)
        li.left(90)
    li.penup()
    li.forward(60)
    li.pendown()
    for _ in range(4):
        li.forward(10)
        li.left(90)

    li.left(180)
    li.penup()
    li.forward(90)
    li.right(90)
    li.pendown()


    li.left(30)
    li.forward(60)
    li.left(100)
    li.forward(50)

    li.right(180)
    li.forward(50)
    li.right(100)
    li.forward(60)

    li.right(120)
    li.forward(100)
    li.left(90)
    li.forward(150)
    li.right(90)
    li.forward(100)
    li.right(90)
    li.forward(120)


    li.left(180)
    li.forward(60)
    li.left(90)
    li.penup()

    li.forward(150)
    li.pendown()
    for _ in range(4):
        li.forward(15)
        li.left(90)




    s.mainloop()


turtlee()