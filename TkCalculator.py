import tkinter

window=tkinter.Tk()
window.title("TkCalc")
window.resizable(True, True)

equa=""
equation=tkinter.StringVar()
equation.set("Input")


def btnPress(num):
     global equa
     equa += str(num)
     equation.set(equa)


def EqualPress():
     global equa
     total=str(eval(equa))
     equation.set(total)
     equa=""


def ClearPress():
     global equa
     equa = ""
     equation.set("Input")
     


result = tkinter.Label(window, textvariable=equation)
result.grid(row=0, columnspan=8)

btn0 = tkinter.Button(window, text="0", bg="white", width=7, relief="solid", command=lambda:btnPress(0))
btn0.grid(row=4, column=2, padx=10, pady=10)
btn1 = tkinter.Button(window, text="1", bg="white", width=7, relief="solid", command=lambda:btnPress(1))
btn1.grid(row=1, column=1, padx=10, pady=10)
btn2 = tkinter.Button(window, text="2", bg="white", width=7,relief="solid", command=lambda:btnPress(2))
btn2.grid(row=1, column=2, padx=10, pady=10)
btn3 = tkinter.Button(window, text="3", bg="white", width=7,relief="solid", command=lambda:btnPress(3))
btn3.grid(row=1, column=3, padx=10, pady=10)
btn4 = tkinter.Button(window, text="4", bg="white", width=7,relief="solid", command=lambda:btnPress(4))
btn4.grid(row=2, column=1, padx=10, pady=10)
btn5 = tkinter.Button(window, text="5", bg="white", width=7,relief="solid", command=lambda:btnPress(5))
btn5.grid(row=2, column=2, padx=10, pady=10)
btn6 = tkinter.Button(window, text="6", bg="white", width=7,relief="solid", command=lambda:btnPress(6))
btn6.grid(row=2, column=3, padx=10, pady=10)
btn7 = tkinter.Button(window, text="7", bg="white", width=7,relief="solid", command=lambda:btnPress(7))
btn7.grid(row=3, column=1, padx=10, pady=10)
btn8 = tkinter.Button(window, text="8", bg="white", width=7,relief="solid", command=lambda:btnPress(8))
btn8.grid(row=3, column=2, padx=10, pady=10)
btn9 = tkinter.Button(window, text="9", bg="white", width=7,relief="solid", command=lambda:btnPress(9))
btn9.grid(row=3, column=3, padx=10, pady=10)


btnadd = tkinter.Button(window, text="+", bg="white", width=7,relief="solid", command=lambda:btnPress("+"))
btnadd.grid(row=1, column=4, padx=10, pady=10)
btnsub = tkinter.Button(window, text="-", bg="white", width=7,relief="solid", command=lambda:btnPress("-"))
btnsub.grid(row=2, column=4, padx=10, pady=10)
btnmul = tkinter.Button(window, text="*", bg="white", width=7,relief="solid", command=lambda:btnPress("*"))
btnmul.grid(row=3, column=4, padx=10, pady=10)
btndiv = tkinter.Button(window, text="/", bg="white", width=7,relief="solid", command=lambda:btnPress("/"))
btndiv.grid(row=4, column=4, padx=10, pady=10)
btnequal = tkinter.Button(window, text="=", bg="white", width=7,relief="solid", command=EqualPress)
btnequal.grid(row=4, column=3, padx=10, pady=10)
btnclear = tkinter.Button(window, text="C", bg="white", width=7,relief="solid", command=ClearPress)
btnclear.grid(row=4, column=1, padx=10, pady=10)


window.mainloop()
