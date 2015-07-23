# finished

class Circle:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius

	def circumference(self):
		return 3.14 * 2 * self.radius
		
	def area(self):
		return 3.14 * self.radius ** 2
		
	def __str__(self):
		return str(self.x) + ", " + str(self.y) + " radius=" + str(self.radius)

c1 = Circle(5, 5, 5)
c2 = Circle(0, 0, 3)
c3 = Circle(10, 10, 2)

circle_list = [c1, c2, c3]

for circ in circle_list:
	print (circ)
	print ("circumference: " + str(circ.circumference()) )
	print ("area: " + str(circ.area()))
