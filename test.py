from tkinter import *

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
        
    def shutdown(self):
        exit()
        
        
from smooth import smoothEvo
root = Tk()
root.geometry('500x500')
root.config(bg='gray30')
app = Window(root)
root.mainloop()