import Tkinter
import ttk

window = Tkinter.Tk()
notebook = ttk.Notebook(window)
notebook.pack()
subframe = Tkinter.Frame(window)
subframe.pack()
notebook.add(subframe, text="tab", state="normal")
def buttonaction():
    notebook.tab(0, state="disabled")
button = Tkinter.Button(subframe, command=buttonaction, text="click to disable tab")
button.pack()

if __name__ == "__main__":
    window.mainloop()