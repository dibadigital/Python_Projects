from tkinter import*
from tkinter import ttk
from PIL import Image , ImageDraw , ImageTk
import os
import time

def clickedbutton(event=None):
        print("button clicked")

def main():

        root=Tk()
        root.title("Diba")

        pic1=PhotoImage(file="Desert_resized.png")
        l1=ttk.Label(root,image=pic1)
        l1.pack()
        l1.place(x=0,y=0)

        pic2=PhotoImage(file="power_off_resized.png")
        l2=ttk.Label(root,image=pic2)
        l2.pack()
        l2.place(x=100,y=100)

        l2.bind("<Button-1>",clickedbutton)
        
        root.mainloop()

if __name__ == "__main__" : main()


'''im1=Image.open("Desert.png")
        im2=Image.open("power_off_resized.png")
        im2=im2.resize(im1.size)
        new = Image.alpha_composite(im1 , im2).save("mine2.png")'''

        
'''mask=Image.new("L",(256,256),"black")
        draw=ImageDraw.Draw(mask)
        draw.ellipse([0,0,256,256],fill=255)
        del draw
        mask.save("mask_circle_01.jpg")
        mask=Image.open("mask_circle_01.jpg")
        mask=mask.resize(im1.size)
        new = Image.composite(im2 , im1, mask).save("mine.png")'''
'''image = Image.open("Buzzer.png")
        photo = ImageTk.PhotoImage(image)'''
