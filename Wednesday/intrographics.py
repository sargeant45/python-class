import Tkinter

# create a window object
window = Tkinter.Tk()

window.title("Testing, 1... 2... 3...")
window.geometry("450x450")

T = Tkinter.Text(window, height=450, width=450)
T.pack()
T.config(font=('Comic Sans MS', 14), foreground="#ff0000")
T.insert(Tkinter.END, "Just some text and stuff.")

window.mainloop()