from tkinter import Tk, Label, Button
from tkinter import Tk, Canvas, Frame, BOTH
# http://zetcode.com/gui/tkinter/drawing/

DIM_Y = 10
DIM_X = 10

def getx(x):
    return int(DIM_X / 2) + x

def gety(y):
    return -(int(DIM_Y / 2) + y + 1) % DIM_Y 


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.close_button = Button(master, text="Draw", command=self.initUI)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def initUI(self):
      
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        canvas.pack(fill=BOTH, expand=1)


root = Tk()
my_gui = MyFirstGUI(root)\
root.mainloop()
