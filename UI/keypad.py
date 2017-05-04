#!/usr/local/bin/python
# This python script displaies a number pad on the LCD screen for users
# There is entry at the first row showing pin entered in '*'
# The correct pin is: 1234

# Import python modules
import Tkinter as tk
import tkFont as tkf

# Define a class of a whole App
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)

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

        self.f1.grid(sticky=tk.N+tk.S)
        self.f2.grid(sticky=tk.N+tk.S)

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
        self.e1.grid(row=0, column=0, sticky=tk.S+tk.N)
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

        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.btn4.grid(row=1, column=0)
        self.btn5.grid(row=1, column=1)
        self.btn6.grid(row=1, column=2)
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        self.btn0.grid(row=3, column=1)

        # A Enter and Cencel bottons
        self.cencel = tk.Button(self.f2, text='Cencel', command=lambda:self.entries_checker(process='delete'))
        self.enter = tk.Button(self.f2, text='Enter', command=lambda:self.enter_btn()) 
        self.cencel.grid(row=3, column=0)
        self.enter.grid(row=3, column=2)

    # Method to check pin
    def enter_btn(self):
        # Make 4 digits a string
        pin = str(self.e1.get()+self.e2.get()+self.e3.get()+self.e4.get())
        if pin == '1234':
            print 'Access Accepted'
        else:
            print 'Access Not Accepted'

    def cencel_btn(self, h):
        h.config(state=tk.NORMAL)
        h.delete(0)
        h.config(state=tk.DISABLED)

    # Method to input digits into entries
    def input(self, e, digit):
        e.config(state=tk.NORMAL)
        e.insert(tk.END, str(digit))
        e.config(state=tk.DISABLED)

    def entries_checker(self, digit=None, **process):
        for ety in [self.e1, self.e2, self.e3, self.e4]:
            if process.get('process') == 'input':
                if len(ety.get()) == 0:
                    self.input(ety, digit)
                    break
            elif process.get('process') == 'delete' and digit is None:
                self.cencel_btn(ety)
            else:
                print process
                print 'Nothing processed'

app = Application()
app.master.title('Security Box Keypad')
app.master.geometry('600x400')
app.mainloop()
