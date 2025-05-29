from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("TIC TAC TOE")

button1 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button1))

button1.grid(row=0,column=0)

button2 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0,column=1)

button3 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button3))
button3.grid(row=0,column=2)

button4 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button4))
button4.grid(row=1,column=0)

button5 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button5))
button5.grid(row=1,column=1)

button6 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button6))
button6.grid(row=1,column=2)

button7 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button7))
button7.grid(row=2,column=0)

button8 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button8))
button8.grid(row=2,column=1)

button9 = Button(main, text="", font=("arial",60,"bold"),bg="#ffb5a7",fg="white",width=3, command=lambda: ButtonClick(button9))
button9.grid(row=2,column=2)

main.mainloop()