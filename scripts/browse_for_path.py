import tkinter
from tkinter import *
import os

def browse_for_path():
    #Sets up GUI
    root = tkinter.Tk()
    root.withdraw()
    root.lift()
    root.update()
    currdir = os.getcwd()
    fileName = filedialog.askopenfilename(initialdir=currdir + "/saves/", title='Please select the game to load').replace('//', '/').replace('/','//')
    root.destroy()
    root.quit()
    return fileName
