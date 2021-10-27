#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.speed(0)
# and body


# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots


legs = 4
leg_length = 70
space_between_legs = 250 / legs
ladybug.pensize(5)
leg_amount = -2
while (leg_amount < legs):
  ladybug.penup()
  ladybug.goto(0,-55)
  ladybug.pendown()
  ladybug.setheading(space_between_legs*leg_amount)
  ladybug.circle(25,180,10)
  leg_amount = leg_amount + 1


ladybug.penup()
ladybug.pendown()
ladybug.hideturtle()
ladybug.penup()
ladybug.goto(0, -72.5) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(85)
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots += 1
  wn = trtl.Screen()
wn.mainloop()