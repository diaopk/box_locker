import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.S+tk.N+tk.E+tk.W)

        # btn
        #top = self.winfo_toplevel()
        #top.rowconfigure(0, weight=1)
        #top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.btn = tk.Button(self, text='Button')
        self.btn.grid(sticky=tk.N+tk.S+tk.E+tk.W)

app = Application()
app.master.title('Test 4')
app.mainloop()
