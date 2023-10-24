#Créez une calculatrice simple en Python qui permet à l'utilisateur d'effectuer des opérations de base (addition, soustraction, multiplication et division).
#Utiliser un if pour déterminer quels opé faire
#et créer une fonction addition(n1, n2) qui renvoie une somme de n1 et n2

#Créer votre propre interface à l'aide de Tkinter, pour afficher une interface d'inscription donc  Pseudo, mdp, email.
#Et lorsqu'on valide l'inssription ca m'affiche sur le terminal les données 

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice")
        

# etiquette_pseudo = tk.Label(fenetre, text="Pseudo")

operation = ""
def action_bouton1():
    global operation
    operation = operation + "1"
    etiquette_response = tk.Label(fenetre, text=operation)
    etiquette_response.grid(row=10, column=1)

def action_bouton2():
    global operation
    operation = operation + "2"
    etiquette_response2 = tk.Label(fenetre, text=operation)
    etiquette_response2.grid(row=10, column=1)

def action_bouton3():
    global operation
    operation = operation + "3"
    etiquette_response4 = tk.Label(fenetre, text=operation)
    etiquette_response4.grid(row=10, column=1)

def action_bouton4():
    global operation
    operation = operation + "4"
    etiquette_response5 = tk.Label(fenetre, text=operation)
    etiquette_response5.grid(row=10, column=1)

def action_bouton5():
    global operation
    operation = operation + "5"
    etiquette_response6 = tk.Label(fenetre, text=operation)
    etiquette_response6.grid(row=10, column=1)

def action_bouton6():
    global operation
    operation = operation + "6"
    etiquette_response7 = tk.Label(fenetre, text=operation)
    etiquette_response7.grid(row=10, column=1)

def action_addition():
    global operation
    operation = operation + "+"
    etiquette_response3 = tk.Label(fenetre, text=operation)
    etiquette_response3.grid(row=10, column=1)

# def action_soustraction():
#     global operation
#     operation = operation + "-"
#     etiquette_response8 = tk.Label(fenetre, text=operation)
#     etiquette_response8.grid(row=10, column=1)


def action_resultat():
    global operation
    resultat = 0
    operationsplit = operation.split("+")
    for element in operationsplit:
        resultat += int(element)
    operation = operation + "="
    etiquette_response9 = tk.Label(fenetre, text=operation)
    etiquette_response9.grid(row=10, column=1)
    
    # tk.DoubleVar(fenetre, name=operation)
    etiquette_response10 = tk.Label(fenetre, text=str(resultat))
    etiquette_response10.grid(row=10, column=2)
    
# boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
#     ligne = 1
#     colonne = 0
# for i in range(10):
#     bouton = tk.Button(fenetre, text=i)
#     bouton.grid(row=1, column=i)


bouton1 = tk.Button(fenetre, text="1", command=action_bouton1)
bouton2 = tk.Button(fenetre, text="2", command=action_bouton2)
bouton3 = tk.Button(fenetre, text="3", command=action_bouton3)
bouton4 = tk.Button(fenetre, text="4", command=action_bouton4)
bouton5 = tk.Button(fenetre, text="5", command=action_bouton5)
bouton6 = tk.Button(fenetre, text="6", command=action_bouton6)
bouton1.grid(row=1, column=1)
bouton2.grid(row=1, column=2)
bouton3.grid(row=1, column=3)
bouton4.grid(row=2, column=1)
bouton5.grid(row=2, column=2)
bouton6.grid(row=2, column=3)

boutonAddition = tk.Button(fenetre, text="+", command=action_addition)
boutonAddition.grid(row=4, column=1)
# boutonSoustraction = tk.Button(fenetre, text="-", command=action_soustraction)
# boutonSoustraction.grid(row=4, column=2)
boutonResultat = tk.Button(fenetre, text="=", command=action_resultat)
boutonResultat.grid(row=6, column=1)



fenetre.geometry("500x400")

fenetre.mainloop() #la fenêtre reste ouverte jusqu'à la fermeture utilisateur

