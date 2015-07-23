

# f(x) = x^2 + 3
def f(x):
	return x * x + 3
	
	
print (f(2))

# 1. try building a function g(x) 
#    and display the value of g(some number)	

# 2. try creating a loop
#    and print the values of g(0), g(1), g(2)...g(9), g(10)

# g(x) = 3 * x - 5
def g(x):
	return 3 * x - 5
	
x = 0
while x < 11:
	print ( str(x) + "\t" + str(g(x)) )
	x += 1