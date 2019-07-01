#
# a simple forest generation applet
# intended to be a class 1 totallistic
# cellular automata
# 
# not intended to be good
#

#base gui library
from tkinter import *
#helper gui libraries
from PIL import Image
from PIL import ImageTk


#main window is generated from tkinters default frame data
class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #master refers to main window
        self.master = master
        self.initWindow()

    def initWindow(self):
        #sizing and title
        self.master.title('Tree Gen')
        
        #base menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
        
        #file menu creation
        file=Menu(menu)
        file.add_command(label='close and exit', command=self.shutdown)
        menu.add_cascade(label='File', menu=file)
        
        #left as comment for reference
        #Label(text='pass').grid(row=0, column=0)
        for x in range(0,20):
            for y in range(0,20):
                Label(text='X').grid(row=y, column=x, ipadx=4)
        
        

    def displayImg(self, i, x, y):
      load=Image.open(i)
      render=ImageTk.PhotoImage(load)
      img=Label(self, image=render)
      img.image=render
      img.place(x=x, y=y)  
    
    def displayText(self, i):
        text=Label(self, text=i)
        text.pack()

    def shutdown(self):
        exit()

root=Tk()
root.geometry("450x450")
app=Window(root)
root.mainloop()

