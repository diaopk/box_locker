from Tkinter import *

root = Tk()

def change_text():
    entry.configure(state=NORMAL)
    sv.set("one")
    entry.configure(state=DISABLED)

def change_btn_text(event):
    btn.configure(text="Hit you")

def del_btn(event):
    if len(entry.get()) == 3 :
        btn.configure(text="Hit us")

frame = Frame(root, width=200, height=200)
frame.bind("<Configure>", change_btn_text)
frame.bind("<Configure>", del_btn)
frame.pack()

sv = StringVar()
btn = Button(frame, text="Hit me", command=change_text)
btn.pack()
entry = Entry(frame, textvariable=sv, state=DISABLED)
entry.pack()

root.mainloop()
