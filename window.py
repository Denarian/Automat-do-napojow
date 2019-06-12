import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpad


class Window:
    def __init__(self, controller):
        self._window = tk.Tk()
        self._controller = controller

        self._window.title('Automat do napojow')
        self._window.geometry('340x520')
        self._cash_label = tk.Label(self._window, text="Wrzuć monetę")
        self._cash_label.grid(row=0,column=4,columnspan=3)

        self._numpad = numpad.Numpad(self._window, self,1,4)

        self._product_label = tk.Label(self._window, text='')
        self._product_label.grid(row=6,column=4,columnspan=3)
        self._numpad2 = numpad.Numpad2(self._window, self,7,4)
        ttk.Separator(self._window,orient="vertical").grid(row=0,column=3,rowspan=30,sticky="ns")
        tk.Label(self._window, text='Produkty').grid(row=0, column=0,columnspan=3)
        tk.Label(self._window,text='Numer').grid(row=1, column=0)
        tk.Label(self._window, text='Produkt').grid(row=1, column=1)
        tk.Label(self._window, text='Cena').grid(row=1, column=2)
        i = 2
        for x in controller.lista_produktow:
            tk.Label(self._window, text=str(x)).grid(row=i, column=0)
            tk.Label(self._window, text=str(controller.lista_produktow[x])).grid(row=i, column=1)
            tk.Label(self._window, text=str(controller.ceny_produktow[x])+"zł").grid(row=i, column=2)
            i += 1
        self._productNumber = ''


    def start(self):
        self._window.mainloop()


    def chooseProduct(self, i):
        self._productNumber += i
        self._product_label.config(text=self._productNumber)
        if len(self._productNumber) > 1:
            product = int(self._productNumber)
            try:
                text = self._controller.lista_produktow[product]

            except :
                showinfo("Err", "Nie ma takiego produktu")
            else:

                if self._controller.ilosc_produktow[product] == 0:
                    text += "\tBrak wybranego produktu"
                    showinfo("Err", text)
                else:
                    if self._controller.suma() >= self._controller.ceny_produktow[product]:
                        returned_coins = self._controller.wydaj_produkt(product)
                        if returned_coins == -1:
                            showinfo("Err","Tylko odliczona kwota")
                            returns = self._controller.wydaj_monety()
                            if returns:
                                text = ''
                                sum = 0
                                for i in returns:
                                    text += str(returns[i]) + " x " + str(i) + "zł\n"
                                    sum += i * returns[i]
                                text += "Zwrócono: " + str(sum) + "zł"
                                showinfo("ZWROT", text)
                                self.update_cash_label()
                        else:
                            odd_money = 0
                            for j in returned_coins:
                                odd_money += j * returned_coins[j]

                            text += "\n Reszta: "+str(odd_money)+"zł\n"
                            for i in returned_coins:
                                text += str(returned_coins[i]) + " x " + str(i) + "zł\n"
                            showinfo("Wydano produkt", text)
                            self.update_cash_label()
                    else:
                        text += " : " + str(self._controller.ceny_produktow[product]) + "zł"
                        showinfo("Cena", text)

            self.clear()
            

    def clear(self):
        self._productNumber=''
        self._product_label.config(text=self._productNumber)

    def update_cash_label(self):
        sum = self._controller.suma()
        if sum > 0:
            self._cash_label.config(text=str(sum) + "zł")
        else:
            self._cash_label.config(text="Wrzuć monetę")
