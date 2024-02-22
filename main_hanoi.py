import graphique_hanoi 
import resolution_hanoi as resolution

# nombre de disques
nombre_disque = 5
# temps d'attente entre chaque déplacement de disque pour l'interface graphique
attente = 500

dessiner = graphique_hanoi.Graphiques(nombre_disque)



t = resolution.initialise(nombre_disque)
solution = resolution.hanoi(t,nombre_disque,0,2,1, [])

f_solution = []
for x in solution:
    f_solution.append(x)


for deplacement in f_solution:
    dessiner.deplacer_rectangle(deplacement[0], deplacement[1], attente)