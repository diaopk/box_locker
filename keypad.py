#!/usr/local/bin/python
# This python script displaies a number pad on the LCD screen for users
# There is entry at the first row showing pin entered in '*'
# The pin is: 1234

# Import required modules and libraries
import Tkinter as tk
import tkFont as tkf
from PIL import ImageTk, Image
from pc import *
from Emailer import Email
from password import Pin

# Define a class of a whole App
# --- Start of class Application ---
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)

        # Define objects from imported class
        self.server = Email()
        self.photo_manager = Photo_Manager()
        self.pin = Pin()

        # outmost window on the screen
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.numberpad_creator()

    # Method Displaies a numberpad
    def numberpad_creator(self):
        # 2 Frames, one for entries one for numbers
        self.f1 = tk.Frame(self)
        self.f2 = tk.Frame(self)
    
        self.f1.grid()
        self.f2.grid()

        self.f1.rowconfigure(0, weight=1)
        self.f1.columnconfigure(0, weight=1)
        self.f2.rowconfigure(1, weight=1)
        self.f2.columnconfigure(0, weight=1)

        # Font
        self.e_font = tkf.Font(size=15, weight='bold')

        # 4 Entries
        self.e1 = tk.Entry(self.f1, width=4, justify=tk.CENTER, font=self.e_font, show='*', state=tk.DISABLED)
        self.e2 = tk.Entry(self.f1, width=4, justify=tk.CENTER, font=self.e_font, show='*', state=tk.DISABLED)
        self.e3 = tk.Entry(self.f1, width=4, justify=tk.CENTER, font=self.e_font, show='*', state=tk.DISABLED)
        self.e4 = tk.Entry(self.f1, width=4, justify=tk.CENTER, font=self.e_font, show='*', state=tk.DISABLED)

        self.e1.grid(row=0, column=0, sticky=tk.W)
        self.e2.grid(row=0, column=1, sticky=tk.W)
        self.e3.grid(row=0, column=2)
        self.e4.grid(row=0, column=3)

        # 10 digit buttons
        self.btn1 = tk.Button(self.f2, text='1', width=3, command=lambda:self.entries_checker(1, process='input'))
        self.btn2 = tk.Button(self.f2, text='2', width=3, command=lambda:self.entries_checker(2, process='input'))
        self.btn3 = tk.Button(self.f2, text='3', width=3, command=lambda:self.entries_checker(3, process='input'))
        self.btn4 = tk.Button(self.f2, text='4', width=3, command=lambda:self.entries_checker(4, process='input'))
        self.btn5 = tk.Button(self.f2, text='5', width=3, command=lambda:self.entries_checker(5, process='input'))
        self.btn6 = tk.Button(self.f2, text='6', width=3, command=lambda:self.entries_checker(6, process='input'))
        self.btn7 = tk.Button(self.f2, text='7', width=3, command=lambda:self.entries_checker(7, process='input'))
        self.btn8 = tk.Button(self.f2, text='8', width=3, command=lambda:self.entries_checker(8, process='input'))
        self.btn9 = tk.Button(self.f2, text='9', width=3, command=lambda:self.entries_checker(9, process='input'))
        self.btn0 = tk.Button(self.f2, text='0', width=3, command=lambda:self.entries_checker(0, process='input'))
    
        # Show buttons
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
        self.btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
        self.btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
        self.btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
        self.btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

        # cencel, enter, browse and forget buttons
        self.cencel = tk.Button(self.f2, text='Cencel', command=lambda:self.entries_checker(process='delete'))
        self.enter = tk.Button(self.f2, text='Enter', command=lambda:self.btn_enter()) 
        self.browse = tk.Button(self.f2, text='Browse', command=lambda:self.btn_browse())
        self.forget = tk.Button(self.f2, text='Forget', command=lambda:self.btn_forget())
        self.change = tk.Button(self.f2, text='Change', command=lambda:self.btn_change())

        self.cencel.grid(row=3, column=0)
        self.enter.grid(row=3, column=2)
        self.browse.grid(row=4, column=0)
        self.forget.grid(row=4, column=1)
        self.change.grid(row=4, column=2)

    # Method to check pin
    def btn_enter(self):
        # Make 4 digits a string
        pin = str(self.e1.get()+self.e2.get()+self.e3.get()+self.e4.get())

        # If pin is correct, then accept and clear the entries
        if self.pin.pin_check(pin):
            print 'Access Accepted'
            self.entries_checker(process='delete')
        else: # Else capture the guy trying to access the box with the wrong pin
            print 'Access Not Accepted'
            self.entries_checker(process='delete')
            self.photo_manager.take_photo()
            #self.show_topwin()
            # Show the first photo
            self.show_topwin(self.photo_manager.last(), process='takephoto')

    # Method to open a window for browsing photo
    def btn_browse(self):
        self.show_topwin(process='browse')

    # Method to reset the pin
    def btn_forget(self):
        self.pin.pin_forget()

    # Method to change the pin
    def btn_change(self):
        pass
            
    # Method to display the toplevel window with the photo
    # Store img object as the global variable to prevent
    # from the gabage collector
    def show_topwin(self, photo=None, **kwarg):
        # Define the position that the toplevel
        # window displaies as the same as the root
        # window
        w = str(self.winfo_screenwidth()/2 - 150)
        h = str(self.winfo_screenheight()/2 -150)
        pos = '300x300+%s+%s' % (w, h)

        topwin = tk.Toplevel()
        topwin.configure(bg='black')
       
        # If 'take a photo'
        if kwarg.get('process') == 'takephoto':
            topwin.geometry('800x480+400+240')
            # if photo is None then go for tests
            if photo is None:
                self.img = ImageTk.PhotoImage(Image.open('image.jpg'))
            else:
                self.img = ImageTk.PhotoImage(Image.open(photo.get_path()))
            topwin.title('WE CAPTURED YOU')
            label = tk.Label(topwin, image=self.img)
            label.pack(side='bottom', fill='both', expand='yes')
            
            # Destroy the toplevel window after 3sec it created
            topwin.after(10000, lambda:topwin.destroy())

            # Send the email with the photo
            self.server.send(photo=photo)
        
        # else if 'browse photos'
        # show the photo browser
        elif kwarg.get('process') == 'browse':
            topwin.geometry(pos)
            topwin.title('Browse photos')
            
            # --- Define widgets ---
            # Define x and y scrollbar
            xscrollbar = tk.Scrollbar(topwin, orient='horizontal')
            yscrollbar = tk.Scrollbar(topwin, orient='vertical')
            # Define a canvas for a frame widget with labels
            canvas = tk.Canvas(topwin, 
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)
            # Defines a frame for labels with photos
            frame = tk.Frame(canvas)

            # --- Locate widgets ---
            xscrollbar.pack(side='bottom', fill='x')
            yscrollbar.pack(side='right', fill='y')
            xscrollbar.config(command=canvas.xview)
            yscrollbar.config(command=canvas.yview)
            canvas.pack(side='left', fill='both', expand=True)
            canvas.create_window((4, 4), window=frame, anchor='nw', tags='frame')

            # Define a event function for the frame
            def on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox('all'))
            
            # Call the event
            frame.bind('<Configure>', on_frame_configure)

            # Image size
            size = 280, 280

            # Populate images
            for photo in self.photo_manager.get_photos():
                im = Image.open(photo.get_path())
                im.thumbnail(size)
                img = ImageTk.PhotoImage(im)
                label_img = tk.Label(frame, image=img)
                label_img.image = img # Must keep a reference for each label because of the python collector
                label_time = tk.Label(frame, text=photo.get_datetime())
                label_img.pack()
                label_time.pack()
        else:
            pass

    # Method to clear the entry h
    def btn_cencel(self, h):
        h.config(state=tk.NORMAL)
        h.delete(0)
        h.config(state=tk.DISABLED)

    # Method to input digits into entries
    def input(self, e, digit):
        e.config(state=tk.NORMAL)
        e.insert(tk.END, str(digit))
        e.config(state=tk.DISABLED)

    # Method to process 'delete' or 'input' for entries
    # based on the value of **process
    def entries_checker(self, digit=None, **process):
        for ety in [self.e1, self.e2, self.e3, self.e4]:

            # If the value of process is 'input' and the 
            # entry is epty then insert the digit into the
            # entry. break when a single input process finishes
            if process.get('process') == 'input':
                if len(ety.get()) == 0:
                    self.input(ety, digit)
                    break

            # else if the value of process if 'delete' then 
            # invoke cencel_btn() to clear the input
            elif process.get('process') == 'delete' and digit is None:
                self.btn_cencel(ety)

            # else print some debug messagaes
            else:
                print process
                print 'Nothing processed'

    def screen_width(self):
        return self.winfo_screenwidth()/2

    def screen_height(self):
        return self.winfo_screenheight()/2

    # --- End of the class Application --- 

if __name__ == '__main__':
    app = Application()
    app.master.title('Security Box Keypad')
    app.master.geometry('%dx%d+%d+%d' % (300, 300, app.screen_width()-150, app.screen_height()-150))
    app.mainloop()
