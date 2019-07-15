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
            #self.strData = ''
            self.color = 'gray20'
        elif (self.data == 1):
            #self.strData = ''
            self.color = 'gray40'
        elif (self.data == -1): #border data
            self.color = 'gray15'
        return Label(text=self.strData, bg=self.color, font = ('helvetica', '1'), width=2, height=1)
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

root=Tk()
root.geometry('601x601')
root.configure(bg='gray30')

#for now map will have a static size definition

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
        
        #tile map
        dataMap = [[0 for x in range(75)] for x in range(75)]
        #label map
        labelMap = [[0 for x in range(75)] for x in range(75)]
        
        #base menu
        menu=Menu(self.master)
        self.master.config(menu=menu)
        
        #file menu creation
        file=Menu(menu)
        file.add_command(label='Close and Exit', command=self.shutdown)
        menu.add_cascade(label='File', menu=file)
        
        #generation menu
        gen=Menu(menu)
        gen.add_command(label='Clear Map', command=self.clearMap)
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
        for row in range(0,74):
            for col in range(0,74):
                smoothEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(75):
            for col in range(75):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
                
    def flood(self):
        #run an evolve check on all tiles
        for row in range(75):
            for col in range(75):
                floodEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(75):
            for col in range(75):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
         
    def drought(self):
        #run an evolve check on all tiles
        for row in range(75):
            for col in range(75):
                droughtEvo(map, map.getTile(row, col))
        #update all tiles and reprint
        for row in range(75):
            for col in range(75):
                map.getTile(row, col).dataPush()
                map.getStr(row, col).grid(row=row, column=col)
    
    def clearMap(self):
        for row in range(75):
            for col in range(75):
                self.map[row][col].getStr.grid_remove()
        self.l = Label(text='Generate a fresh map', bg='grey30', fg='grey20', font=('helvetica', 30, 'bold'))
        self.l.pack(expand=True)
    
    def undo(self):
        for row in range(75):
            for col in range(75):
                self.map[row][col].oldCommit()
                self.map[row][col].dataPush()
                self.map[row][col].getStr.grid(row=row, column=col)
            
    #generates a new map based on given paramaters    (paramaters not yet implimented)   
    def createNewGeneration(self):
        self.l.destroy()
        for row in range(75):
            for col in range(75):
                r=randint(0,1)
                if (row < 2 or row > 72 or col < 2 or col > 72):
                    self.map[row][col].dataCommit(-1)
                    self.map[row][col].dataPush()
                    self.map[row][col].getStr.grid(row=row, column=col)
                else:
                    if(r == 0):
                        self.map[row][col].dataCommit(0)
                        self.map[row][col].dataPush()
                        self.map[row][col].getStr.grid(row=row, column=col)
                    else:
                        self.map[row][col].dataCommit(1)
                        self.map[row][col].dataPush()
                        self.map[row][col].getStr.grid(row=row, column=col)
 

    #this uh.. yeah
    def shutdown(self):
        for row in range(75):
            for col in range(75):
                self.map[row][col].getStr.grid_remove()
        exit()

#local tools import last to avoid loops
from smooth import smoothEvo
from flood import floodEvo
from drought import droughtEvo

app=Window(root)
root.mainloop()

