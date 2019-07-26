#
# a simple forest generation applet
# intended to showcase the different
# classess of celular automata
# 
# not intended to actually be efficient
#

#external libraries
from tkinter import *
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
    #creates a new label, used during any tile update
    def makeLabel(self):  
        if (self.data == 0):
            self.strData = ''
            self.color = 'gray20'
        elif (self.data == 1):
            self.strData = ''
            self.color = 'gray40'
        elif (self.data == -1): #border data
            self.color = 'gray15'
        return Label(text=self.strData, bg=self.color, font = ('helvetica', '1'), width=3, height=1)
    #data managedment methods
    def getData(self):
        return self.data
    def dataCommit(self, data):
        self.newData=data
    def dataPush(self):
        self.oldData=self.data
        self.data=self.newData
    def getOldData(self):
        return self.oldData         

#tile map
dataMap = [[0 for x in range(75)] for x in range(75)]
#label map
labelMap = [[0 for x in range(75)] for x in range(75)]

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
        self.l = Label(text='Generate a fresh map', bg='grey30',
                       fg='grey20', font=('helvetica', 30, 'bold'))
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
        gen.add_command(label='Fresh Generation',
                        command=self.createNewGeneration)
        gen.add_command(label='Clear Map', command=self.clearMap)
        menu.add_cascade(label='Generation', menu=gen)

        #transformation menu
        transform=Menu(menu)
        transform.add_command(label='Smooth', command=self.smooth)
        menu.add_cascade(label='Transformation', menu=transform)
        

#------------------------------------------------------------------------------
#utilities
    
    #recreates a tiles data and reprints
    def recreateTile(self, row, col, data):
        dataMap[row][col].dataCommit(data)
        dataMap[row][col].dataPush()
        if (labelMap[row][col] != 0):
            labelMap[row][col].grid_remove()
        labelMap[row][col] = dataMap[row][col].makeLabel()
        labelMap[row][col].grid(row=row, column=col)
        
    #updates a tiles data and reprints
    def updateTile(self, row, col):
        dataMap[row][col].dataPush()
        labelMap[row][col].grid_remove()
        labelMap[row][col] = dataMap[row][col].makeLabel()
        labelMap[row][col].grid(row=row, column=col)
        

    #this uh.. yeah
    def shutdown(self):
        for row in range(75):
            for col in range(75):
                if (labelMap[row][col] != 0):
                    labelMap[row][col].grid_remove()
        exit()
        
#------------------------------------------------------------------------------
#generation menu commands

    #generates a new map of randomly placed tile types
    def createNewGeneration(self):
        self.l.destroy()
        for row in range(75):
            for col in range(75):
                dataMap[row][col] = Tile(row, col, 0)
                r=randint(0,1)
                if (row < 2 or row > 72 or col < 2 or col > 72):
                    self.recreateTile(row, col, -1)
                else:
                    self.recreateTile(row, col, r)
                    
    #wipes current grid out entirely and sets default message
    def clearMap(self):
        for row in range(75):
            for col in range(75):
                labelMap[row][col].grid_remove()
        self.l = Label(text='Generate a fresh map', bg='grey30', fg='grey20', font=('helvetica', 30, 'bold'))
        self.l.pack(expand=True)

#------------------------------------------------------------------------------
#evolution menu commands     
                            
    def smooth(self):
        #run an evolve check on all tiles
        for row in range(0,74):
            for col in range(0,74):
                dataMap[row][col].dataCommit(smoothOne(dataMap, row, col))
                #smoothOne(dataMap, row, col)
        #update all tiles and reprint
        #it is important to reprint after all tiles have been smoothed
        for row in range(75):
            for col in range(75):
                self.updateTile(row, col)
                

#local imports
from smooth import smoothOne
from smooth import smoothTwo
from smooth import smoothThree
#app is created and run
root = Tk()
root.geometry('525x525')
root.configure(bg='gray30')
app = Window(root)
root.mainloop()
