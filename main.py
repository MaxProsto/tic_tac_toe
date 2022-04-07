from ast import Lambda
from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title('Tic Tac Toe - Multiplayer')
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
player_a_name = Entry(tk, textvariable = p1, bd = 5)
player_a_name.grid(row = 1, column = 1, columnspan =8)
player_b_name = Entry(tk, textvariable = p2, bd =5)
player_b_name.grid(row = 2, column = 1, columnspan =8)
bclick = True
flag = 0
buttons = StringVar()
label = Label(tk, text = 'Player 1: ', font= ' arial 20 bold', bg = 'white', fg = 'black', height = 1, width = 😍
label.grid(row=1, column = 0)

label = Label(tk, text = 'Player 2: ', font= ' arial 20 bold', bg = 'white', fg = 'black', height = 1, width = 😍
label.grid(row=2, column = 0)

button1 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button1))
button1.grid(row = 3, column = 0)

button2 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button2))
button2.grid(row = 3, column = 1)

button3 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button3))
button3.grid(row = 3, column = 2)

button4 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button4))
button4.grid(row = 4, column = 0)

button5 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button5))
button5.grid(row = 4, column = 1)

button6 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button6))
button6.grid(row = 4, column = 2)

button7 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button7))
button7.grid(row = 5, column = 0)

button8 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button8))
button8.grid(row = 5, column = 1)

button9 = Button(tk, text = '', font='arial 20 bold', bg = 'gray', fg = 'white', height = 4, width =8, command = Lambda:btnClick(button9))
button9.grid(row = 5, column = 2)

if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
  b1.config(bg='red')
  b2.config(bg='red')
  b3.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
  
 elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
  b4.config(bg='red')
  b5.config(bg='red')
  b6.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
 elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
  b7.config(bg='red')
  b8.config(bg='red')
  b9.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
 elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
  b1.config(bg='red')
  b4.config(bg='red')
  b7.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'X выиграли!')
  disable_all_buttons()
 elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
  b2.config(bg='red')
  b5.config(bg='red')
  b8.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
 elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
  b2.config(bg='red')
  b5.config(bg='red')
  b8.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
 elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
  b1.config(bg='red')
  b5.config(bg='red')
  b9.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()
 elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
  b3.config(bg='red')
  b5.config(bg='red')
  b7.config(bg='red')
  winner = True
  messagebox.showinfo('Tic Tac Toe', 'O выиграли!')
  disable_all_buttons()


def b_click(b):
 global clicked, count
 if b['text'] == '' and clicked == True:
  b['text'] = 'X'
  clicked = False
  count += 1
  checkifwon()
 elif b['text'] == '' and clicked == False:
  b['text'] = 'O'
  clicked = True
  count += 1
  checkifwon()
 else:
  messagebox.showerror('Tik Tac Toe', 'Эта ячейка занята, выберите другое!')

b1 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b1))
b2 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b2))
b3 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b3))

b4 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b4))
b6 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b6))
b5 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b5))

b7 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b7))
b8 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b8))
b9 = Button(tk, text='', font=('Arial', 20), height=3, width=6, bg ='yellow', command= lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


tk.mainloop()