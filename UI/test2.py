import Tkinter as tk

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter+= 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()

root = tk.Tk()
root.title("Some Stuff")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=label.destroy)
button.pack()
root.mainloop()
