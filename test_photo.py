from test_pc import *
from Tkinter import *
from PIL import ImageTk, Image

root = Tk()

yscrollbar = Scrollbar(root, orient='vertical')
xscrollbar = Scrollbar(root, orient='horizontal')
canvas = Canvas(root, 
        yscrollcommand=yscrollbar.set,
        xscrollcommand=xscrollbar.set)
pm = Photo_Manager()
frame = Frame(canvas)

yscrollbar.pack(side=RIGHT, fill=Y)
yscrollbar.config(command=canvas.yview)
xscrollbar.pack(side=BOTTOM, fill=X)
xscrollbar.config(command=canvas.xview)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
canvas.create_window((4, 4), window=frame, tags='frame')
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

frame.bind('<Configure>', on_frame_configure)

img = ImageTk.PhotoImage(Image.open(pm.first().get_path()))
img1 = ImageTk.PhotoImage(Image.open(pm.next().get_path()))
img2 = ImageTk.PhotoImage(Image.open(pm.next().get_path()))
label = Label(frame, image=img)
label1 = Label(frame, image=img1)
label2 = Label(frame, image=img2)
label.pack()
label1.pack()
label2.pack()

mainloop()
