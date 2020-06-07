from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import font

back_color = 'white'
fore_color = 'black'
btn_w = 8
btn_h = 4
player1 = True
player2 = False
flag = 0
myFont = font.BOLD


win = tk.Tk()
win.title('Tic Tac Toe')

def disableBtn():
    button1.configure(state='disabled')
    button2.configure(state='disabled')
    button3.configure(state='disabled')
    button4.configure(state='disabled')
    button5.configure(state='disabled')
    button6.configure(state='disabled')
    button7.configure(state='disabled')
    button8.configure(state='disabled')
    button9.configure(state='disabled')

def check_for_win():
    global flag, scoreA, scoreB
    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        print('Player A wins!')
        disableBtn()
        score = scoreA.get()
        if score == '':
            score = 1
        else:
            score = int(score) + 1
        scoreA.set(str(score))
        messagebox.showinfo('Tic Tac Toe', 'Player A Wins !')

    elif (button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
        button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
        button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
        button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
        button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
        button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        print('Player B wins!')
        disableBtn()
        score = scoreB.get()
        if score == '':
            score = 1
        else:
            score = int(score) + 1
        scoreB.set(str(score))
        messagebox.showinfo('Tic Tac Toe', 'Player B Wins !')

    elif flag==8:
        print('Its a tie')
        disableBtn()
        messagebox.showinfo('Tic Tac Toe', 'Its a tie')
    
        

def btnClick(button):
    global player1, player2, flag
    if player1 == True and button['text']==' ':
        button['text'] = 'X'
        player1 = False
        player2 = True
        flag += 1
        check_for_win()
    if player2 == True and button['text']==' ':
        button['text'] = 'O'
        player2 = False
        player1 = True
        flag += 1
        check_for_win()

def resetGame():
    global player1, player2, flag
    button1.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button2.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button3.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button4.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button5.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button6.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button7.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button8.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button9.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    player1 = True
    player2 = False
    flag = 0

def restartGame():
    # flush all data scores and active the game fresh
    global player1, player2, flag
    button1.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button2.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button3.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button4.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button5.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button6.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button7.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button8.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    button9.configure(state='active', text=' ', bg=back_color, fg=fore_color)
    player1 = True
    player2 = False
    flag = 0
    scoreA.set('0')
    scoreB.set('0')

Game = ttk.Frame(win, borderwidth=3)
Game.grid(row=0, column=0)

GF = ttk.Frame(Game, borderwidth=3)
GF.grid(rowspan=3, column=0)

button1 = tk.Button(GF, text=' ',font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button1))
button1.grid(row=0, column=0)        

button2 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button2))
button2.grid(row=0, column=1)        

button3 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button3))
button3.grid(row=0, column=2)        

button4 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button4))
button4.grid(row=1, column=0)        

button5 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button5))
button5.grid(row=1, column=1)        

button6 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button6))
button6.grid(row=1, column=2)        

button7 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button7))
button7.grid(row=2, column=0)        

button8 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button8))
button8.grid(row=2, column=1)        

button9 = tk.Button(GF, text=' ', font=myFont, bg=back_color, fg=fore_color, width=btn_w, height=btn_h, command=lambda :btnClick(button9))
button9.grid(row=2, column=2)        

optionsFrame = ttk.Frame(Game, borderwidth=3)
optionsFrame.grid(row=0, column=1)

ttk.Label(optionsFrame, text='Player A').grid(row=0, column=0, sticky='N', padx=3, pady=3)
scoreA = tk.StringVar()
scoreB = tk.StringVar()

if scoreA.get() == '' and scoreB.get() == '':
    scoreA.set('0')
    scoreB.set('0')
    
scoreA_box = ttk.Entry(optionsFrame, state='readonly', justify='right', font=myFont, textvariable=scoreA)
scoreA_box.grid(row=1, column=0, sticky='N', padx=3, pady=3)

ttk.Label(optionsFrame, text='Player B').grid(row=2, column=0, sticky='N', padx=3, pady=3)
scoreB_box = ttk.Entry(optionsFrame, state='readonly', justify='right', font=myFont, textvariable=scoreB)
scoreB_box.grid(row=3, column=0, sticky='N', padx=3, pady=3)

restartBtn = ttk.Button(Game, text='RESTART', command=restartGame)
restartBtn.grid(row=1, column=1, sticky='WESN', padx=10, pady=10)


resetBtn = ttk.Button(Game, text='RESET', command=resetGame)
resetBtn.grid(row=2, column=1, sticky='WESN', padx=10, pady=10)

win.mainloop()