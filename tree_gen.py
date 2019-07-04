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
    #used by map to manage per tile data
    def getData(self):
        return Label(text=self.data)
    #partner to above method
    def update(self, data):
        self.data=data
            

#a tile managing class
class Map:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self.map=[]
    
        #build map
        for row in range(self.rows):
            self.map.append([])
            for col in range(self.cols):
                t=Tile(row, col, '')
                self.map[row].append(t)
      
    #uses Tiles getData/update to manage individual tile data          
    def getData(self, row, col):
        return self.map[row][col].getData()
    def update(self, row, col, data):
        self.map[row][col].update(data)
    def getTile(self, row, col):
        return self.map[row][col]
            

map=Map(15,15)

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
     
    #class one evolution, can be run multiple times
    def evolveOne(self):
        evolution.classOne(map, map.getTile(5,5))
        map.update(5,5,'X')
        map.getData(5,5).grid(row=5, column=5, ipadx=5)      
     
    #generates a new map based on given paramaters    (paramaters not yet implimented)   
    def createNewGeneration(self):
        for row in range(0,14):
            for col in range(0,14):
                r=randint(0,1)
                if(r == 0):
                    map.update(row, col, '_')
                    map.getData(row, col).grid(row=row, column=col, ipadx=5)
                else:
                    map.update(row, col, '|')
                    map.getData(row, col).grid(row=row, column=col, ipadx=5)
     
    #displays an img 'i' at x/y    
    def displayImg(self, i, x, y):
      load=Image.open(i)
      render=ImageTk.PhotoImage(load)
      img=Label(self, image=render)
      img.image=render
      img.place(x=x, y=y)  
      
    #displays text i (only to be used to test if app has crashed)
    def displayText(self, i):
        text=Label(self, text=i)
        text.pack()
        
    #this uh.. yeah
    def shutdown(self):
        exit()

root=Tk()
root.geometry("450x450")
app=Window(root)
root.mainloop()

