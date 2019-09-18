#   a115_buggy_image.py
import turtle as trtl

robot = trtl.Turtle()
robot.pensize(40)
robot.circle(20)
w = 6
y = 70
z = 380 / w
robot.pensize(5)
n = 0
while (n < w):
  robot.goto(0,0)
  robot.setheading(z*n)
  robot.forward(y)
  n = n + 1
robot.hideturtle()
wn = trtl.Screen()
wn.mainloop()

