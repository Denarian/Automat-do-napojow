import tkinter as tk
from tkinter.messagebox import showinfo

class Numpad:
    def __init__(self, window, view,row,column):
        tk.Button(window, text='1g', width=5, command=lambda coin=0.01: add_coin(view, coin)).grid(row=row, column=column)
        tk.Button(window, text='2g', width=5, command=lambda coin=0.02 : add_coin(view, coin)).grid(row=row, column=column+1)
        tk.Button(window, text='5g', width=5, command=lambda coin=0.05: add_coin(view, coin)).grid(row=row, column=column+2)
        tk.Button(window, text='10g', width=5, command=lambda coin=0.1: add_coin(view, coin)).grid(row=row+1, column=column+0)
        tk.Button(window, text='20g', width=5, command=lambda coin=0.2: add_coin(view, coin)).grid(row=row+1, column=column+1)
        tk.Button(window, text='50g', width=5, command=lambda coin=0.5: add_coin(view, coin)).grid(row=row+1, column=column+2)
        tk.Button(window, text='1zl', width=5, command=lambda coin=1: add_coin(view, coin)).grid(row=row+2, column=column+0)
        tk.Button(window, text='2zl', width=5, command=lambda coin=2: add_coin(view, coin)).grid(row=row+2, column=column+1)
        tk.Button(window, text='5zl', width=5, command=lambda coin=5: add_coin(view, coin)).grid(row=row+2, column=column+2)
        tk.Button(window, text='R', width=5, command=lambda : return_coins(view)).grid(row=row + 3,column=column + 1)

        def add_coin(view,coin):
            view._controller.wrzuc_monete(coin)
            view.update_cash_label()

        def return_coins(view):
            returns = view._controller.wydaj_monety()
            if returns:
                text = ''
                sum = 0
                for i in returns:
                    text += str(returns[i])+" x "+str(i)+"zł\n"
                    sum += i * returns[i]
                text += "Zwrócono: "+str(sum)+"zł"
                showinfo("ZWROT",text)
            view.update_cash_label()

class Numpad2:
    def __init__(self, window, view,row,column):
        r = row
        c = column
        for i in range(1, 10):
            tk.Button(window, text=i, width=5,command=lambda i = i: view.chooseProduct(str(i))).grid(row=row, column=column)
            column+=1
            if not i%3:
                row +=1
                column = c
        i=0
        tk.Button(window, text=i, width=5,command=lambda i = i: view.chooseProduct(str(i))).grid(row=row, column=column+1)
        tk.Button(window, text='C', width=5,command=lambda : view.clear() ).grid(row=row, column=column+2)
