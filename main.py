from tkinter import *
from tkinter import messagebox

def ButtonClick(button):
    global x_o, flag
    button ["bg"] = "#2ec4b6"
    if button["text"] == "" and x_o == True:
        button ["text"] = "X"
        x_o = False
        flag = flag+1
    elif button ["text"] == "" and x_o == False:
        button ["text"] = "O"
        x_o = True
        flag = flag+1   
    else: 
        messagebox.showinfo("Tic Tac Toe", "Player has already entered")

    winner = check_winner()
    if winner == "X":
        messagebox.showinfo("Tic Tac Toe", "X Wins!")
    elif winner == "O":
        messagebox.showinfo("Tic Tac Toe", "O Wins!")
    elif winner == "Tie":
        messagebox.showinfo("Tic Tac Toe", "Tie!")



def check_winner():
    '''return letter (X or O) of winner, "" for non finished, or "Tie"'''
    global button_grid

    # check horizontal
    for i in range(3):
        if button_grid[i][0]['text'] != "" \
                and (button_grid[i][0]['text'] == button_grid[i][1]['text'] == button_grid[i][2]['text']):
            return button_grid[i][0]['text']
        
    # check vertical
    for i in range(3):
        if button_grid[0][i]['text'] != "" \
                and (button_grid[0][i]['text'] == button_grid[1][i]['text'] == button_grid[2][i]['text']):
            return button_grid[0][i]['text']
        
    # check diaganol 1
    if button_grid[0][0]['text'] != "" \
            and (button_grid[0][0]['text'] == button_grid[1][1]['text'] == button_grid[2][2]['text']):
        return button_grid[0][0]['text']
    
    # check diaganol 2
    if button_grid[2][0]['text'] != "" \
            and (button_grid[2][0]['text'] == button_grid[1][1]['text'] == button_grid[0][2]['text']):
        return button_grid[2][0]['text']

    # check for not finished
    for i in range(3):
        for j in range(3):
            if button_grid[i][j]['text'] == "":
                return "" # not finished

    return "Tie"  # not finished

"""
1 2 3
4 5 6
7 8 9
3 5 9
1 4 7
2 5 8
3 6 9
"""

def CheckForWin():
    global button1, button2, button3, button4, button5,button6, button7, button8, button9
    # horisontal Xs
    if      button1 ["text"] == "X" and button2["text"] == "X" and button3 ["text"] == "X" or \
            button4 ["text"] == "X" and button5["text"] == "X" and button6 ["text"] == "X" or \
            button7 ["text"] == "X" and button8["text"] == "X" and button9 ["text"] == "X":
        messagebox.showinfo("Tic Tac Toe", "Player X has already entered")
    # horizontal Os
    elif    button1 ["text"] == "O" and button2["text"] == "O" and button3 ["text"] == "O" or \
            button4 ["text"] == "O" and button5["text"] == "O" and button6 ["text"] == "O" or \
            button7 ["text"] == "O" and button8["text"] == "O" and button9 ["text"] == "O":
        messagebox.showinfo("Tic Tac Toe", "Player O has already entered")
    elif    button3 ["text"] == "X" and button5["text"] == "X" and button9 ["text"] == "X" and \
            button1 ["text"] == "X" and button4["text"] == "X" and button7 ["text"] == "X" and \
            button2 ["text"] == "X" and button5["text"] == "X" and button8 ["text"] == "X" and \
            button3 ["text"] == "X" and button6["text"] == "X" and button9 ["text"] == "X":
        messagebox.showinfo("Tic Tac Toe","Player X has already entered")
    elif    button3 ["text"] == "O" and button5["text"] == "O" and button9 ["text"] == "O" and \
            button1 ["text"] == "O" and button4["text"] == "O" and button7 ["text"] == "O" and \
            button2 ["text"] == "O" and button5["text"] == "O" and button8 ["text"] == "O" and \
            button3 ["text"] == "O" and button6["text"] == "O" and button9 ["text"] == "O":
        messagebox.showinfo("Tic Tac Toe","Player O has already entered")
    elif flag==8:
            messagebox.showinfo("Tic Tac Toe","Game Tied")


main = Tk()
main.title("TIC TAC TOE")

x_o = True
flag = 0 

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

button_grid = [
    [button1, button2, button3],
    [button4, button5, button6],
    [button7, button8, button9],
]

main.mainloop()