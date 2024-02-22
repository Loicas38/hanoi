import tkinter as tk
import time

class Graphiques():
    def __init__(self, nb_rectangles):
        
        self.fenetre = tk.Tk()
        self.fenetre.title("tours d'hanoi")
        # empêche que l'on puisse redimensionner la fenêtre
        self.fenetre.resizable(0, 0)
        # fait passer la fenêtre à l'avant plan
        self.fenetre.wm_attributes("-topmost", 1)
        self.canvas = tk.Canvas(self.fenetre, height = 850, width = 1000, bg="white")

        #création des pics
        x1 = 200
        y1 = 700
        y2 = 680 - 25 * nb_rectangles
        self.espace = 300
        self.pics = {}
        for x in range(3):
            self.canvas.create_rectangle(x1, y1, x1+3, y2, fill='black')
            self.pics[x] = {'x1': x1, 'x2': x1 +3, 'y1': y1, 'y2': y2}
            x1 += self.espace

        #creation des rectangles 
        x1 = 60
        x2 = 340
        y1 = 680
        y2 = 700
        dif_taille = (x2 - x1)/nb_rectangles/2
        self.rectangles = {}
        for x in range(nb_rectangles):
            nb = self.canvas.create_rectangle(x1, y1, x2, y2, fill = 'blue')
            self.rectangles[x] = {'id': nb, 'pic': 0, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}
            y1 -= 25
            y2 -= 25
            x1 += dif_taille
            x2 -= dif_taille

        self.canvas.pack()

    def stop(self):
        self.fenetre.quit()


    def deplacer_rectangle(self, depart, arrivee, attente: int):
        """ attente = attente entre déplacements, ms
        va permettre de déplacer les rctangles en prenant les pics de déprt et d'arrivée """
        liste_depart = []
        for nb, data in self.rectangles.items():
            if data['pic'] == depart:
                liste_depart.append(nb)

        disque = max(liste_depart)

        liste_arrive = []
        for nb, data in self.rectangles.items():
            if data['pic'] == arrivee:
                liste_arrive.append(nb)

        
        x = self.pics[arrivee]['x1'] - (self.rectangles[disque]['x2'] - self.rectangles[disque]['x1'])/2
        y = 680 - len(liste_arrive) * 20 - 5 * len(liste_arrive)

        self.rectangles[disque]['pic'] = arrivee

        self.canvas.moveto(self.rectangles[disque]['id'], x, y)
        self.canvas.pack()
        
        self.fenetre.after(attente,self.stop)
        self.fenetre.mainloop()