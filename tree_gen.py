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


#tile class
class Tile():
    def __init__(self, row, col, data):
        self.row=row
        self.col=col
        self.strData = ''
        self.color = 'black'
        self.data=data
        self.newData=0
        self.oldData=0
    #return tile coords
    def getX(self):
        return self.row
    def getY(self):
        return self.col
    #used by map to manage per tile data
    def getStr(self):  
        if (self.data == 0):
            self.strData = ' '
            self.color = 'forest green'
        elif (self.data == 1):
            self.strData = ' '
            self.color = 'skyblue1'
        return Label(text=self.strData, bg=self.color, width=2, height=1)
    def getData(self):
        return self.data
    #partner to above method
    def dataCommit(self, data):
        self.newData=data
    def dataPush(self):
        self.oldData=self.data
        self.data=self.newData
    def oldCommit(self):
        self.newData=self.oldData            

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
      
    #uses Tiles getStr/update to manage individual tile data          
    def getStr(self, row, col):
        return self.map[row][col].getStr()
    def getData(self, row, col):
        return self.map[row][col].getData()
    def update(self, row, col, data):
        self.map[row][col].dataCommit(data)
        self.map[row][col].dataPush()
    def getTile(self, row, col):
        return self.map[row][col]
            

#for now map will have a static size definition
map=Map(30, 30)

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
        self.l = Label(text='Generate a fresh map', bg='grey30', fg='grey20', font=('helvetica', 30, 'bold'))
        self.l.pack(expand=True)
        #base menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
        
        #file menu creation
        file=Menu(menu)
        file.add_command(label='Close and Exit', command=self.shutdown)
        menu.add_cascade(label='File', menu=file)
        
        #generation menu
        gen=Menu(menu)
        gen.add_command(label='Fresh Generation', command=self.createNewGeneration)
        menu.add_cascade(label='Generation', menu=gen)
        
        #evolution menu
        evo=Menu(menu)
        evo.add_command(label='Smooth', command=self.smooth)  
        evo.add_command(label='Flood', command=self.flood)  
        evo.add_command(label='Drought', command=self.drought)
        evo.add_command(label='Undo', command=self.undo)
        menu.add_cascade(label='Evolution', menu=evo) 
        
   
     
    #class one evolution, can be run multiple times
    def smooth(self):
        #run an evolve check on all tiles
        for row in range(30):
            for col in range(30):
                smoothEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(30):
            for col in range(30):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
                
    def flood(self):
        #run an evolve check on all tiles
        for row in range(30):
            for col in range(30):
                floodEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(30):
            for col in range(30):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
         
    def drought(self):
        #run an evolve check on all tiles
        for row in range(30):
            for col in range(30):
                droughtEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(30):
            for col in range(30):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
    
    def undo(self):
        for row in range(30):
            for col in range(30):
                map.getTile(row, col).oldCommit()
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
            
    #generates a new map based on given paramaters    (paramaters not yet implimented)   
    def createNewGeneration(self):
        self.l.destroy()
        for row in range(30):
            for col in range(30):
                r=randint(0,1)
                if(r == 0):
                    map.update(row, col, 0)
                    map.getStr(row, col).grid(row=row, column=col)
                else:
                    map.update(row, col, 1)
                    map.getStr(row, col).grid(row=row, column=col)
 

    #this uh.. yeah
    def shutdown(self):
        exit()

#local tools import last to avoid loops
from smooth import smoothEvo
from flood import floodEvo
from drought import droughtEvo

root=Tk()
root.geometry('600x630')
root.configure(bg='gray30')

app=Window(root)
root.mainloop()

