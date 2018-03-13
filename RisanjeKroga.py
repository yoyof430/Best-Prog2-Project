from tkinter import *

class Risanje():
    def __init__(self, master):
        self.tocka = None
        self.risemo = True
        self.zacetnaTocka = tuple()
        self.koncnaTocka = tuple()
        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

        # Registriramo se za sledenje miški
        self.canvas.bind('<ButtonRelease-1>', self.konec)
        self.canvas.bind('<Button-1>', self.zacetek)

    def zacetek(self, event):
        self.zacetnaTocka = (event.x, event.y)
        #print(self.zacetnaTocka)
    def konec(self,event):
        self.koncnaTocka = (event.x, event.y)
        self.canvas.create_oval(self.zacetnaTocka[0]-(self.zacetnaTocka[0]-self.koncnaTocka[0]),self.zacetnaTocka[1]-(self.zacetnaTocka[1]-self.koncnaTocka[1]),
                                self.koncnaTocka[0], self.koncnaTocka[1])
        print(self.koncnaTocka)



root = Tk()

aplikacija = Risanje(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()

