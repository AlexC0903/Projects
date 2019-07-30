import tkinter
from math import*

window = tkinter.Tk()
window.title("Button")
window.geometry("600x400+100+100")
window.resizable(True, True)

def calc(event):
    label.config(text = "= "+str(eval(entry.get())))

entry = tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label = tkinter.Label(window, text="The answer is...")
label.pack()

window.mainloop()



