from Tkinter import *
from PIL import Image, ImageTk
from test_pc import Photo_Manager

root = Tk()

pm = Photo_Manager()

img = ImageTk.PhotoImage(Image.open(pm.first().get_path()))
label = Label(root, image=img)
label.image = img
label.pack()

root.mainloop()
