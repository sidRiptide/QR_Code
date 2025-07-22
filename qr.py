from tkinter import *
import pyqrcode
from tkinter import filedialog
import png
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("500x550")

def generate():
    pass

def clear():
    pass

my_entry = Entry(root, width=40)
my_entry.pack(padx=5, pady=5)

myButton = Button(root, text="Generate QR Code", command=generate)
myButton.pack(pady=12)

myButton2 = Button(root, text="Clear", command=clear)
myButton2.pack()



root.mainloop()