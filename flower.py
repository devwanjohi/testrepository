import turtle as sohail
import colorsys as cs
sohail.setup(800,800)
sohail.speed(9)
sohail.tracer(10)
sohail.width(2)
sohail.bgcolor('black')
for j in range(25):
    for i in range(15):
        sohail.color(cs.hls_to_rgb(i/15,j/25,1))
        sohail.right(90)
        sohail.circle(200-j*4,90)
        sohail.left(90)
        sohail.circle(200-j*4,90)
        sohail.circle(50,24)
sohail.hideturtle()
sohail.done()