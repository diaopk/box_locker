import Tkinter as tk
from PIL import ImageTk, Image
from test_pc import Photo_Manager

class Test(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.pm = Photo_Manager
        self.scrollbar = tk.Scrollbar(root, orient='vertical')
        self.canvas = tk.Canvas(root,
                yscrollcommand=self.scrollbar.set)
        self.frame = tk.Frame(self.canvas)
        
        self.scrollbar.config(command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='y', expand=True)
        
        self.canvas.create_window((4, 4), window=self.frame,
                anchor='nw',
                tags="self.frame")

        img1 = ImageTk.PhotoImage(Image.open(Photo_Manager.first().get_path()))
        img2 = ImageTk.PhotoImage(Image.open(self.pm.next().get_path()))
        self.la1 = tk.Label(self.frame, image=img1)
        self.la2 = tk.Label(self.frame, image=img2)
        self.la1.pack(side='top', fill='y')
        self.la2.pack(side='top', fill='y')
    
        """for i in range(30):
            btn = tk.Button(self.frame, text='Button')
            btn.pack(side='left', fill='x')
        self.pm = Photo_Manager()
        for photo in self.pm.photo_seq:
            self.img = ImageTk.PhotoImage(Image.open(photo.get_path()))
            self.label = tk.Label(self.frame, image=self.img)
            self.label.pack(side='top', fill='y')
        """
        self.frame.bind("<Configure>", self.on_frame_configure)
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

root = tk.Tk()
Test(root).pack()
root.mainloop()
