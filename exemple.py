# #boucle
# x = 1
# while x <= 10 :
#     if (x % 2 == 0):
#         print(x)
#     x = x + 1

# #liste
# liste = ["pomme", "poire", "noix"]
# print(liste[0])

# #fonction
# def saluer(nom):
#     print("Bonjour " + nom)
# saluer("Madame")

# #dictionnaire => chaque clé est associée à une valeur
# personne = {"nom": "Lucas", "age":24, "ville":"Saint Germain en Laye"}
# print(personne["nom"])
# print(personne["ville"])

# #input
# nom = input("Entrez votre nom :")
# print("Bonjour, " + nom)

#pour avoir une interface graphique
import tkinter as tk
# print(tk.TkVersion) #vérifier si on a tkinter

#gérer les événements
def action_bouton():
    print("Le bouton a été cliqué")

fenetre = tk.Tk() #créer une fenêtre
fenetre.title("Ma première interface graphique")

#ajouter des étiquettes (=textes)
etiquette = tk.Label(fenetre, text="Bravo tu as fait ta première interface graphique")
etiquette.pack() #le .pack affiche toutes les étiquettes qu'on a créé

# création de bouton
bouton = tk.Button(fenetre, text="Cliquez sur moi !", command=action_bouton)
bouton.pack()

#création d'un champ de texte
champ_text = tk.Entry(fenetre)
champ_text.pack()

fenetre.geometry("400x300")

fenetre.mainloop() #la fenêtre reste ouverte jusqu'à la fermeture utilisateur

