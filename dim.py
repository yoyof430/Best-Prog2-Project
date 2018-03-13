from tkinter import *


class Risalnik():
    def __init__(self, master):
        # Trenutna točka, od koder bomo nadaljevali lomljeno
        # črto. Na začetku je ni.
        self.tocka = None
        self.risemo = True
        self.debelina = 5
        self.barva = None  # none = default črna
        self.kajRisemo = 'PROSTOROCNA CRTA' # OVAL
        self.pravokotnikOrodje = None #za pravokotnik
        self.vmesniLik = None

        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

        # Registriramo se za sledenje miški
        self.canvas.bind("<B1-Motion>", self.nadaljuj_crto)
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.tipka_pritisnjena)
        self.canvas.bind('<ButtonRelease-1>', self.izklopi_risanje)
        self.canvas.bind('<Button-1>', self.zacni_risanje)

    def zacni_risanje(self,event):
        if self.kajRisemo == 'PROSTOROCNA CRTA':
            return
        if self.kajRisemo == 'OVAL':
            self.tocka = (event.x, event.y)
            self.vmesniLik = self.canvas.create_oval(event.x, event.y, event.x, event.y)
            self.pravokotnikOrodje = self.canvas.create_rectangle(event.x, event.y, event.x, event.y, dash =(5,4))
            return
        if self.kajRisemo == 'OZNACEVANJE':
            najblizjiID = self.canvas.find_closest(event.x,event.y)
            print(event.x, event.y,najblizjiID)
            return

    def izklopi_risanje(self, event):
        if self.kajRisemo == 'PROSTOROCNA CRTA':
            self.tocka = None
            return
        if self.kajRisemo == 'OVAL':
            (xMin, yMin) = self.tocka
            self.canvas.coords(self.vmesniLik, xMin, yMin, event.x, event.y)
            self.canvas.delete(self.pravokotnikOrodje)
            self.tocka = None
            self.vmesniLik = None
            self.pravokotnikOrodje = None
            return

    def nadaljuj_crto(self, event):
        '''Nadaljuj 'lomljeno črto'.'''
        if self.kajRisemo == 'PROSTOROCNA CRTA':
            if self.tocka is not None:
                (x, y) = self.tocka
                self.canvas.create_line(x, y, event.x, event.y, width=self.debelina, capstyle=ROUND, fill=self.barva)
                self.tocka = (event.x, event.y)
            else:
                self.tocka = (event.x, event.y)
        if self.kajRisemo == 'OVAL':
            if self.tocka is not None:
                (xMin,yMin) = self.tocka
                self.canvas.coords(self.pravokotnikOrodje, xMin, yMin, event.x, event.y)
                self.canvas.coords(self.vmesniLik, xMin, yMin, event.x, event.y)
            return
    def tipka_pritisnjena(self, event):
        if event.char == 'r':
            self.risemo = not self.risemo
            print('zdaj risemo' if self.risemo else 'ne risemo')
            self.tocka = None
        if event.char == '+':
            self.debelina += 1
        if event.char == '-' and self.debelina > 1:
            self.debelina -= 1
        if event.char == 'c':
            self.barva = 'black'
        if event.char == 'm':
            self.barva = '#3879e2'
        if event.char == 'd':
            self.canvas.delete(ALL)
        if event.char == 'o':
            self.kajRisemo = 'OVAL'
        if event.char == 'p':
            self.kajRisemo = 'PROSTOROCNA CRTA'
        if event.char == 'z':
            self.kajRisemo = 'OZNACEVANJE'
        print(self.kajRisemo)



# glavno okno
root = Tk()

aplikacija = Risalnik(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
