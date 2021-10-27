#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
leg_length = 70
space_between_legs = 380 / legs
spider.pensize(5)
leg_amount = -2
while (leg_amount < legs):
  spider.goto(0,0)
  spider.setheading(space_between_legs*leg_amount)
  spider.forward(leg_length)
  leg_amount = leg_amount + 1
spider.hideturtle()
wn = trtl.Screen()