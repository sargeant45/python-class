# animationtest.py goo.gl/XGPMZ6
# broken

import Tkinter
import math

class Circle:
	def __init__(self, x, y, radius, speed):
		self.x = x
		self.y = y
		self.radius = radius
		self.speed = speed
	def area(self):
		return 3.14 * self.radius**2
	def __str__(self):
		return str(self.x) + ", " + str(self.y) + " radius=" + str(self.radius)

window = Tkinter.Tk()
canvas = Tkinter.Canvas(window, width=150, height=400)
canvas.pack()

dx = 0
dy = 0

def move_right(event):
	print ("right")
	global dx
	dx = 10
def move_left(event):
	print ("left")
	global dx
	dx = -10
def move_up(event):
	global dy
	dy = -10
def move_down(event):
	global dy
	dy = 10

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

x1 = 10
y1 = 10
x2 = x1 + 10
y2 = y1 + 10

c1 = Circle(75, 300, 5, -1)
canvas.create_oval(c1.y-5, c1.y-5, c1.x+5, c1.y+5, fill="red", tag="redcircle")
canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tag="bluesquare")

while True:
	global dx
	global dy
	if x1 > 150:
		x1 = 150
		dx = 0
	elif x1 < 0:
		x1 = 0
		dx = 0
	else: canvas.move("bluesquare", dx, dy)
	if c1.x < 0:
		c1.x = 0
		c1.speed = -1 * c1.speed
	elif c1.x > 150:
		c1.x = 150
		c1.speed = -1 * c1.speed
	else: canvas.move("redcircle", c1.x - x1, c1.y - y1)
	
	if abs(x1-c1.x) + abs(y1-c1.y) < 20:
		if c1.area() > 100: #100 is the original rectangle area
			c1.radius += 5
			canvas.delete("bluesquare")
		if c1.area() < 100: # if circle loses to square
			x2 += 10
			y2 += 10
			canvas.delete("redcircle")
			# todo: redraw the blue square at a larger size
			# todo: respawn the redcircle
			# todo: create top and bottom boundaries
	canvas.after(1000)
	canvas.update()
	y1 += dy
	x1 += dx
	c1.x += c1.speed
	c1.y += c1.speed

window.mainloop()


