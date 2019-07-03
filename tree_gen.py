#
# a simple forest generation applet
# intended to showcase the different
# classess of celular automata
# 
# not intended to actually be efficient
#

#base gui library
from tkinter import *
#helper gui libraries
from PIL import Image
from PIL import ImageTk
#utils
from random import randint
#local tools
import evolution
import generation


#tile class
class Tile():
    def __init__(self, row, col, data):
        self.row=row
        self.col=col
        self.data=data
    def getRow(self):
        return self.row
    def getCol(self):
        return self.col
    def getData(self):
        return self.data
    def update(self, data):
        self.data=data
            

#a tile managing class
class Map:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self._map=[]
    
        #build map
        for row in range(self.rows):
            self._map.append([])
            for col in range(self.cols):
                t=Tile(row, col, '')
                self._map[row].append(t)
            

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
        
        #generation menu
        gen=Menu(menu)
        gen.add_command(label='fresh generation', command=self.createNewGeneration)
        menu.add_cascade(label='Generation', menu=gen)
        
        #evolution menu
        evo=Menu(menu)
        evo.add_command(label='class 1', command=self.evolveOne)  
        menu.add_cascade(label='Evolution', menu=evo)      
     
    def evolveOne(self):
        Label(text='pass').grid(row=0, column=0, ipadx=4)
        evolution.classOne            
     
    #generates a new map based on given paramaters    (paramaters not yet implimented)   
    def createNewGeneration(self):
        map=Map(15,15)
        for row in range(0,14):
            for col in range(0,14):
                r=randint(0,1)
                if(r == 0):
                    return 0
                else:
                    return 0
        
        
        
        
    #    for x in range(0,20):
    #        for y in range(0,20):
    #            r=randint(0,1)
    #            if(r==0):
    #                Label(text='#').grid(row=y, column=x, ipadx=4)
    #            elif(r==1):
    #                Label(text='.').grid(row=y, column=x, ipadx=4)
          

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

