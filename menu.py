import tkinter

window = tkinter.Tk()
window.title("Menu")
window.geometry("600x400+100+100")
window.resizable(True, True)


def close():
    window.destroy()


menubar = tkinter.Menu(window)
menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="New File")
menu_1.add_command(label="Open")
menu_1.add_separator()
menu_1.add_command(label="Exit", command=close)




menubar.add_cascade(label="menu 1", menu=menu_1)

window.config(menu=menubar)

window.mainloop()

print("Window Closed")
