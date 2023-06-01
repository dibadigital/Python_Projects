from tkinter import *

class Form:
    def __init__ (self):
        self.root = Tk()
        self.root.title("dibadigital")
        self.root.geometry("900x600+250+50")

        self.canv = Canvas(self.root, width = 900, height = 600)
        self.canv.pack()

        self.label = Label(self.canv, text = "Your Number: ")
        self.label.pack()
        self.label.config(font = ("Arial Bold", 15), background = "Black", foreground = "White")
        self.label.place(x=50, y=50)

        self.img = PhotoImage(file = "test.png")
        self.canv.create_image(0, 0, image = self.img, anchor = NW)

        self.entry = Entry(self.canv, bd = 5)
        self.entry.pack()
        self.entry.place(x=200, y=50)

    def MainLoop(self):
        self.root.mainloop()

def main():
    s = Form()
    s.MainLoop()

if __name__ == "__main__" : main()


