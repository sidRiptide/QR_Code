from tkinter import *
import pyqrcode
from tkinter import filedialog
import png
from PIL import Image, ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("500x550")

def generate():
    input_path = filedialog.asksaveasfilename(title="save qrcode ",filetypes=(("png ",".png"),("all files","*.*")))
    if input_path :
        if not input_path.endswith(".png") :
            input_path = input_path + ".png"
        # create qr
        get_qr = pyqrcode.create(my_entry.get())
#         save qr
        get_qr.png(input_path,scale=5)
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))

        my_label.configure(image=get_image)
        my_label.pack(pady=10)



def clear():
    my_entry.delete(0, END)

my_entry = Entry(root, width=40)
my_entry.pack(padx=5, pady=5)

myButton = Button(root, text="Generate QR Code", command=generate)
myButton.pack(pady=12)

myButton2 = Button(root, text="Clear", command=clear)
myButton2.pack()

my_label = Label(root, text="")
my_label.pack()


root.mainloop()