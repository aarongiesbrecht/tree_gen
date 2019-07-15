from tkinter import *
root = Tk()
root.geometry('700x700')

class Tile:
    def __init__(self, x, y, data):
        self.x=x
        self.y=y
        self.data=data
    def getData(self):
        return self.data
    def getLabel(self):
        return Label(text='[{},{}]'.format(self.x, self.y))

#tile array
t = [[0 for x in range(75)] for x in range(75)]
#label array
l  = [[0 for x in range(75)] for x in range(75)]

for x in range(75):
    for y in range(75):
        t[x][y] = Tile(x,y,0)
        l[x][y] = t[x][y].getLabel()
        l[x][y].grid(row=x,column=y)
'''
for x in range(75):
    for y in range(75):
        l[x][y].grid_remove()  
  
l = Label(text='Generate a fresh map', bg='grey30', fg='grey20')
l.pack(expand=True)    '''

root.mainloop()