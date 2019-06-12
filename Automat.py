

class Automat:
    def __init__(self):
        self.bank  = {
            0.01 : 5,
            0.02 : 5,
            0.05 : 5,
            0.10 : 5,
            0.20 : 5,
            0.50 : 5,
            1 : 5,
            2 : 5,
            5 : 5
        }
        self.wrzuty = {
            0.01 : 0,
            0.02 : 0,
            0.05 : 0,
            0.10 : 0,
            0.20 : 0,
            0.50 : 0,
            1 : 0,
            2 : 0,
            5 : 0
        }

        self.lista_produktow = {
            30 : "woda",
            31 : "woda nieggazowana",
            32 : "woda gazowana",
            33 : "woda lekko gazowana",
            34 : "lipton icetea peach",
            35 : "lipton icetea lemon",
            36 : "coca cola zero",
            37 : "coca cola lime",
            38 : "fanta",
            39 : "sprite",
            40 : "pepsi",
            41 : "cappy orange",
            42 : "oranżada",
            43 : "lemoniada",
            44 : "tymbark jabłko-mięta",
            45 : "tymbark cytryna-mięta",
            46 : "leon",
            47 : "tiger",
            48 : "redbull",
            49 : "montain dew",
            50 : "hortex"
            
        }
        self.ilosc_produktow = {
            30 : 5,
            31 : 5,
            32 : 5,
            33 : 5,
            34 : 5,
            35 : 5,
            36 : 5,
            37 : 5,
            38 : 5,
            39 : 5,
            40 : 5,
            41 : 5,
            42 : 5,
            43 : 5,
            44 : 5,
            45 : 5,
            46 : 5,
            47 : 5,
            48 : 5,
            49 : 5,
            50 : 5
            
            }
        self.ceny_produktow = {
            30 : 1.7,
            31 : 1.8,
            32 : 1.9,
            33 : 2.0,
            34 : 2.0,
            35 : 2.3,
            36 : 2.5,
            37 : 1.6,
            38 : 1.8,
            39 : 2.0,
            40 : 2.6,
            41 : 2.5,
            42 : 3.0,
            43 : 3.2,
            44 : 2.7,
            45 : 2.4,
            46 : 2.2,
            47 : 2.5,
            48 : 3.0,
            49 : 2.7,
            50 : 3.5
            }
    def sprawdz_dostepnosc(self, produkt):
        if self.ilosc_produktow[produkt] > 0:
            return True
        return False

    def sprawdz_cene(self, produkt):
        return self.ceny_produktow[produkt]
    
    def wrzuc_monete(self, moneta):
        self.wrzuty[moneta] += 1

    def schowaj_monety(self):
        for i in self.bank:
            self.bank[i] += self.wrzuty[i]
            self.wrzuty[i] = 0

    def suma(self):
        sum=0
        for i in self.wrzuty:
            sum += i * self.wrzuty[i]
        return sum

    def wydaj_monety(self):
       w = {k:self.wrzuty[k] for k in self.wrzuty if self.wrzuty[k] > 0}
       for i in self.wrzuty:
           self.wrzuty[i] = 0
       return w

    def wydaj_produkt(self,prokukt):
        if prokukt in self.ilosc_produktow:

            reszta = self.suma() - self.ceny_produktow[prokukt]

            reszta_monety = {}
            
            monety = [k for k in self.bank if self.bank[k] > 0]
            monety.reverse()
            if monety:
                for i in monety:
                    reszta_monety[i] = 0
                    while reszta // i and self.bank[i]:
                        reszta -= i
                        self.bank[i] -= 1
                        reszta_monety[i] += 1
                if reszta >= 0.01:
                    return -1
            self.ilosc_produktow[prokukt] -= 1
            self.schowaj_monety()
            return {k:v for k,v in reszta_monety.items() if v > 0}
        else:
            return {}
