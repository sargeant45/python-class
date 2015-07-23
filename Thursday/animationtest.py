from Tkinter import *

def rect(x1, y1, x2, y2, size, canvas, window, speed):
  canvas.create_rectangle(x1, y1, x2, y2, fill="red", tag="square")
  canvas.create_rectangle(x1 + size, y1 + size, x2 + size, y2 + size, fill="blue", tag="square2")
  
  while y1 < 300:
    canvas.move("square", speed, speed)
    canvas.move("square2", speed, speed)
    canvas.update()
    y1 = y1 + speed
  
  canvas.delete("all")

def init():
  window = Tk()
  canvas = Canvas(window, width=500, height=500)
  canvas.pack()

  size = 100
  x1 = 0
  y1 = 0
  x2 = x1 + size
  y2 = y1 + size
  
  speed = 1
  
  while True:
    rect(x1, y1, x2, y2, size, canvas, window, speed)
    speed += 1
    if speed > 100:
      speed = 1

init()
window.mainloop()