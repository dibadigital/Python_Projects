
from tkinter import *
import numpy as np
import matplotlib
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class myclass:
    def __init__(self,  window):
        self.window = window
        self.window.geometry("500x500")

        self.box = Entry(window)
        self.box.pack ()

        self.btn = Button (window, text="Click", command=self.plot)
        self.btn.pack()

    def plot (self):
        x= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y= np.array([20,21,19,10,22,27,25,15,31,26])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(x, y,color='red')

        a.set_title ("graph", fontsize=15)

        a.set_ylabel("y", fontsize=15)
        a.set_xlabel("x", fontsize=15)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        
def main():
    window = Tk()
    s= myclass(window)
    window.mainloop()
if __name__ == "__main__" : main()
