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
#from PIL import Image
#from PIL import ImageTk
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
    #used by map to manage per tile data
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
    def getData(self):
        return self.data
    #partner to above method
    def dataCommit(self, data):
        self.newData=data
    def dataPush(self):
        self.oldData=self.data
        self.data=self.newData
    def getOldData(self):
        return self.oldData         

root=Tk()
root.geometry('525x525')
root.configure(bg='gray30')
 #tile map
dataMap = [[0 for x in range(75)] for x in range(75)]
#label map
tmp = Label(text='temp')
labelMap = [[tmp for x in range(75)] for x in range(75)]

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
        
    #updates a tiles data and reprints
    def updateTile(self, row, col, data):
        dataMap[row][col].dataCommit(data)
        dataMap[row][col].dataPush()
        labelMap[row][col].grid_remove()
        labelMap[row][col] = dataMap[row][col].makeLabel()
        labelMap[row][col].grid(row=row, column=col)

    #generates a new map based on given paramaters    (paramaters not yet implimented)   
    def createNewGeneration(self):
        self.l.destroy()
        for row in range(75):
            for col in range(75):
                dataMap[row][col] = Tile(row, col, 0)
                r=randint(0,1)
                if (row < 2 or row > 72 or col < 2 or col > 72):
                    self.updateTile(row, col, -1)
                else:
                    self.updateTile(row, col, r)
                        
    #this uh.. yeah
    def shutdown(self):
        for row in range(75):
            for col in range(75):
                labelMap[row][col].grid_remove()
        exit()

app=Window(root)
root.mainloop()

