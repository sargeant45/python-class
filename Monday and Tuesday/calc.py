import Tkinter

# ax^2 + bx + c
# ask user for a, b, and c
print ("Enter the 'a' term")
a = float(raw_input())
print ("Enter the 'b' term")
b = float(raw_input())
print ("Enter the 'c' term")
c = float(raw_input())

def f(x):
	return a * x**2 + b * x + c  # ax^2 + bx + c 
		
window = Tkinter.Tk()

window.title("Graphing Calc")
window.geometry("500x500")

canvas = Tkinter.Canvas(window, width=300, height=300)
canvas.pack()

x = 0
while x < 300:
	y = 300 - f(x)
	canvas.create_rectangle(x, y, x, y, fill="blue")
	x += 1


window.mainloop()

