
import turtle as trtl
painter = trtl
painter.speed(0)
y = 0
color = input("what color should these circles be? ")
painter.color(color)
while y < 20:
  painter.circle(18)
  painter.right(20)
  painter.forward(10)
  y += 1


