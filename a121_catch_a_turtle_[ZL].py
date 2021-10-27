# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
#-----initialize turtle-----
bob = trtl.Turtle()

#-----game configuration----
bob.color("pink")
bob.shape("square")
bob.shapesize(1)

#-----game functions--------
def bob_clicked(x, y):
  print("Ah, you clicked me!")
  

#-----events----------------
wn = trtl.Screen()
wn.mainloop()


