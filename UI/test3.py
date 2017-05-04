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

f = Frame(root)
f.rowconfigure(0, weight=1)
f.columnconfigure(0, weight=1)
f.grid(sticky=E+W+S+N)
e = Entry(f, state=DISABLED)
e.grid(sticky=N+W+E)
btn = Button(f, text='Button', command=lambda:thing(e))
btn.grid(sticky=E+W+N)

root.mainloop()
