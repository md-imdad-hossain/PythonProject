
import tkinter as tk
from tkinter import ttk
from Tkinter import *
import tkFileDialog
from tkinter import PhotoImage
import ttk
import tkMessageBox

form = tk.Tk()
form.title("KIT MAKER")
form.geometry("500x400")

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

btnNext = Button( text="Browse...",  fg='#990000', font="Verdata 10 bold", width=6, height=6).place(x=30, y=50)



tab_parent.add(tab1, text="STEP 1")
tab_parent.add(tab2, text="STEP 2", state="disabled")


tab_parent.pack(expand=1, fill='both')

form.mainloop()