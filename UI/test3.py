from Tkinter import *

def thing(e):
    if len(e.get()) == 0:
        e.insert(END, 'haha')
    else:
        print 'No'

root = Tk()
#top = root.winfo_toplevel()
#top.rowconfigure(0, weight=1)
#top.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

e = Entry(root, state=DISABLED)
e.grid()
btn = Button(root, text='Button', command=lambda:thing(e))
btn.grid(sticky=N+E+S+W)

root.mainloop()
