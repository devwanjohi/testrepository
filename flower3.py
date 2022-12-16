import turtle
import colorsys

turtle.bgcolor('black')
turtle.speed(0.1)
c = 0.0
turtle.hideturtle()
for i in range(450):
    colors = colorsys.hls_to_rgb(c,1,1)
    turtle.color(colors)
    c+=0.005
    turtle.forward(i)
    turtle.backward(i)
    turtle.left(10)
    turtle.right(180)
    turtle.tracer(10)
turtle.mainloop()