from tkinter import*
from tkinter import ttk
import os

class Form:
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("900x600+250+50")
        self.root.title("Menu")
        self.root.overrideredirect(True)
        
        self.canv = Canvas(self.root, width=900, height=600)
        self.canv.pack()

        self.label=ttk.Label(self.canv,text="Designed by Diba Digital")
        self.label.pack()
        self.label.config(font=("Arial Bold",15))
        self.label.config(background="blue",foreground="white")
        self.label.place(x=0,y=550)
        
        self.my_image1 = PhotoImage(file = "menu_resized.png")
        self.my_image2 = PhotoImage(file = "house_resized.png")
        self.my_image3 = PhotoImage(file = "login_page_resized.png")
        self.my_image4 = PhotoImage(file = "logout_page_resized.png")
        
        self.photo1 = PhotoImage(file='shutdown_resized.png')
    
        self.photo2 = PhotoImage(file='home_icon_resized.png')
    
        self.photo3 = PhotoImage(file='icon_phone_resized.png')
    
        self.photo4 = PhotoImage(file='refresh_resized.png')
    
        self.photo5 = PhotoImage(file='logout_resized.png')

        self.obj_bg = self.canv.create_image(0, 0, image=self.my_image1, anchor=NW)
        self.obj1 = self.canv.create_image(760, 20, image=self.photo1, anchor=NW)
        self.obj2 = self.canv.create_image(50, 100, image=self.photo2, anchor=NW)
        self.obj3 = self.canv.create_image(50, 200, image=self.photo3, anchor=NW)
        self.obj4 = self.canv.create_image(50, 300, image=self.photo4, anchor=NW)
        self.obj5 = self.canv.create_image(50, 400, image=self.photo5, anchor=NW)

        self.canv.tag_bind(self.obj1,'<Button>',func=self.ExitClick)
        self.canv.tag_bind(self.obj2,'<Button>',func=self.Obj2Click)
        self.canv.tag_bind(self.obj3,'<Button>',func=self.Obj3Click)
        self.canv.tag_bind(self.obj4,'<Button>',func=self.Obj4Click)
        self.canv.tag_bind(self.obj5,'<Button>',func=self.Obj5Click)

    def ExitClick(self,event):
        os._exit(1)
    def Obj2Click(self,event):
        self.canv.itemconfig(self.obj_bg, image = self.my_image2)
    def Obj3Click(self,event):                  
        self.canv.itemconfig(self.obj_bg, image = self.my_image3)
    def Obj4Click(self,event):                  
        self.canv.itemconfig(self.obj_bg, image = self.my_image1)
    def Obj5Click(self,event):                  
        self.canv.itemconfig(self.obj_bg, image = self.my_image4)

        
    def MainLoop(self):
        self.root.mainloop()
        

def main():
    
    s=Form()
    s.MainLoop()

if __name__ == "__main__" : main()


