import Tkinter as tk

count = 0
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        #self.bt = tk.Button(self, text=self.bt_text(self.lb))
        #self.bt.grid()
        self.label = tk.Label(self, fg="green")
        self.label.grid()
        self.bt_text(self.label)
        self.bt = tk.Button(self, text="haha")
        self.bt.grid()
        self.e1 = tk.Entry(self)
        self.e1.grid()

    def bt_text(self, label):
        count = 0

        def addition():
            global count
            count+=1
            label.config(text=str(count))            
            label.after(1000, addition)

        addition()

app = Application()
app.master.title('Security Box - keypad')
app.mainloop()
