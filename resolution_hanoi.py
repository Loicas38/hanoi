#!/usr/bin/python3

def initialise(nb_disques) :
    """ Fonction qui initialise un tableau pour représenter les tours de hanoi """
    t = [[],[],[]]
    for i in range(nb_disques,0,-1) :
        t[0].append(i)
    return t

def affiche(tours) :
    """ Cette fonction est chargée d'afficher le plateau de façon agréable """
    print()
    print("="*6," HANOI ","="*7)
    for ligne in tours :
        if len(ligne)==0 :
            print("-")
        else :
            for nb in ligne :
                print(nb, end=" ")
            print()
    print("="*20)  


def hanoi(tours,n,depart,arrivee,auxiliaire, deplacements):
    """ cette fonction récursive va déplacer la pyramide de hanoi de hauteur n
    de la tige de départ (0 pour gauche, 1 pour centre, 2 pour droite) vers la tige d'arrivée. 
    cette fonction opérera sur le tableau, de façon récursive """
    # On rappelle que pour retirer un élément d'un tableau en python, on utilise la méthode pop
    # tours[0].pop() retire le dernier élément de la première ligne
    # pop renvoi l'élément que l'on peut manipuler
    # valeur = tours[0].pop() par exemple
    # et à contrario, append ajoute à la fin de la liste
    # tours.append(nombre)
    
    if n == 0:
        return

    hanoi(tours, n-1, depart, auxiliaire, arrivee, deplacements)

    attente = tours[depart].pop(-1)
    tours[arrivee].append(attente)
    deplacements.append((depart, arrivee))

    hanoi(tours, n-1, auxiliaire, arrivee, depart, deplacements)

    #affiche(tours)
    return deplacements


if __name__ == "__main__":
    nombre_disque = 4

    t = initialise(nombre_disque)
    affiche(t)
    a = hanoi(t,nombre_disque,0,2,1, [])
    print(a)