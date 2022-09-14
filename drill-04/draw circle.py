import turtle

i=0
j=0
while (i<6):
    turtle.penup()
    turtle.goto(100*i,0)
    turtle.pendown()
    turtle.goto(100*i,500)
    i=i+1

while (j<6):
    turtle.penup()
    turtle.goto(0,100*j)
    turtle.pendown()
    turtle.goto(500,100*j)
    j=j+1


turtle.exitonclick()
