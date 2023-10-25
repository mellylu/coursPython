#PROJET SEULE ET PAS DU TOUT REUSSI
#AJOUTER FONCTIONNE, CA SE RAJOUTE A LA BASE DE DONNEES (bd.json)
#AFFICHER LES TACHES FONCTIONNE (problème => page trop petite donc pas toutes les infos visibles si il y a beaucoup d'objet dans le tableau)
#SUPPRIMER FONCTIONNE MAIS PROBLEME (quand je récupère l'id ça prend le dernier id donc ça supprime à chaque fois le dernier element)
#PROJET NON DYNAMIQUE => la base de données se modifie automatiquement mais l'interface tkinter ne recupère pas les nouvelles infos
#PAS COMPRIS QUE C'ETAIT EVALUE SINON J'AURAI DAVANTAGE CHERCHE UN GROUPE

import json
import uuid
import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk

fenetre = tk.Tk()

fenetre.title("Gestionnaire de tâche")

with open('bd.json') as mon_fichier:
    data = json.load(mon_fichier)


def getIdTache(id):
    print("get id tache")

def deleteIdTache(id):
    with open('bd.json') as mon_fichier:
        data = json.load(mon_fichier)
    print("delete id tache")
    # print(id)
    print(data)
    data = list(filter(lambda item: item["id"] != id, data))
    file = open("bd.json" , 'w')
    file.write(json.dumps(data))
    file.close()
    # mon_fichier.close()
    # getAllTaches()
    #pour raffraichir la page
    # button.pack_forget()
    # label.pack()


def addTache():
    tache = {
        "id": str(uuid.uuid4()),
	    "name": champ_name.get(),
	    "description" : champ_description.get(),
	    "date": str(champdate.get_date()),
        "etat": etat.get(),
    }
    data.append(tache)
    with open('bd.json', 'w') as mon_fichier:
	    json.dump(data, mon_fichier)

def updateIdTache(id):
    print("delete id tache")


def getAllTaches():
    tk.Label(fenetre, text="LISTE DES TACHES").pack()
    tk.Label(fenetre, text="---------------").pack()
    for element in data:
        x1 = tk.Label(fenetre, text=element["id"])
        # if (element["etat"] == "En cours"):
        # x1.config(bg="yellow")
        x1.pack()
        x2 = tk.Label(fenetre, text=element["name"])
        x2.pack()
        x3 = tk.Label(fenetre, text=element["description"])
        x3.pack()
        x4 = tk.Label(fenetre, text=element["date"])
        x4.pack()
        x5 = tk.Label(fenetre, text=element["etat"])
        x5.pack()
        tk.Button(fenetre, text="Supprimer", command = lambda: deleteIdTache(element["id"])).pack()
        # if (element["etat"] == "Termine"):
        # var1 = tk.IntVar()
        # var1.set("Termine")
        # cEtat = tk.Checkbutton(fenetre, text=element["etat"],variable=var1, onvalue=1, offvalue=0, command= lambda:updateIdTache(element["id"]))
        # cEtat.pack()



etiquette_name = tk.Label(fenetre, text="Nom de la tâche")
etiquette_description = tk.Label(fenetre, text="Descrption de la tâche")
etiquette_etat = tk.Label(fenetre, text="Etat de la tâche")
etiquette_date = tk.Label(fenetre, text="Date de la tâche")

champ_name = tk.Entry(fenetre)
champ_description = tk.Entry(fenetre)
champ_etat = tk.Entry(fenetre)
champdate = Calendar(fenetre, selectmode = 'day',
               year = 2023, month = 10,
               day = 25)

etiquette_name.pack()
champ_name.pack()
etiquette_description.pack()
champ_description.pack()
etiquette_etat.pack()
etat = tk.StringVar()
etat.set("En cours")
r1 = tk.Radiobutton(fenetre, text="En cours", variable=etat, value="En cours")
r2 = tk.Radiobutton(fenetre, text="Terminé", variable=etat, value="Termine")
r1.pack()
r2.pack()
etiquette_date.pack()
champdate.pack(pady = 20)


bouton_add = tk.Button(fenetre, text="Ajouter une tâche", command=addTache)
bouton_add.pack()

bouton_getAll = tk.Button(fenetre, text="Afficher les tâches", command=getAllTaches)
bouton_getAll.pack()


fenetre.geometry("2000x1600")

fenetre.mainloop()


