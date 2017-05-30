from Tkinter import *
from PIL import Image, ImageTk
from time import sleep

def topwin(top, root, Img1):
    print 'Function called'
    top.lift()
    top.title('Sorry we captured you')
    lable = Label(root, text='we captured you', image=Img1)
    lable.pack()

def destroy(t):
    sleep(2)
    t.destroy()

root = Tk()
root.title('test toplevel window')
root.grid()

top = Toplevel(bg='black')
top1 = winfo_toplevel()
    
img = Image.open('./image.jpg')
Img = ImageTk.PhotoImage(img)

btn = Button(root, text='hit me to show window', command=lambda:topwin(top, root, Img))
btn.pack() 
btn1 = Button(root, text='DESTORY', command=lambda:destroy(top))
btn1.pack()
if top == top1:
    la = Label(root, text='true')
else: 
    la = Label(root, text='false')

la.pack()

# Define the width and height for root window
w = 400
h = 400

top.geometry('%dx%d+%d+%d' % (400, 400, root.winfo_screenwidth()/2-200, root.winfo_screenheight()/2-200))
root.geometry('%dx%d+%d+%d' % (400, 400, root.winfo_screenwidth()/2-200, root.winfo_screenheight()/2-200))
root.mainloop()
