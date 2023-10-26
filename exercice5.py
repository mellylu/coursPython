import json
import uuid
import tkinter as tk
from importlib import reload  # Python 3.4+

fenetre = tk.Tk()


fenetre.title("Gestionnaire de contact")


with open('bd_contact.json') as mon_fichier:
    data = json.load(mon_fichier)


def formAddContact():
    fenetreAdd = tk.Tk()
    fenetreAdd.title("Ajouter un contact")
    etiquette_name = tk.Label(fenetreAdd, text="Nom")
    etiquette_numero = tk.Label(fenetreAdd, text="Numéro")
    etiquette_autres = tk.Label(fenetreAdd, text="Autres")
    champ_name = tk.Entry(fenetreAdd)
    champ_numero = tk.Entry(fenetreAdd)
    champ_autres = tk.Entry(fenetreAdd)
    etiquette_name.pack()
    champ_name.pack()
    etiquette_numero.pack()
    champ_numero.pack()
    etiquette_autres.pack()
    champ_autres.pack()
    tk.Button(fenetreAdd, text="Ajouter", command = lambda: addContact(champ_name, champ_numero, champ_autres)).pack()

  
def addContact(name, numero, autres):
    contact = {
        "id": str(uuid.uuid4()),
	    "name": name.get(),
	    "numero" : numero.get(),
	    "autres": autres.get()
    }
    print(data)
    data.append(contact)
    file = open('bd_contact.json', 'w')
    file.write(json.dumps(data))
    file.close()
    fenetre.update()
    fenetre.update_idletasks()


def deleteContact(id):
    with open('bd_contact.json') as mon_fichier:
        data = json.load(mon_fichier)
    data = list(filter(lambda item: item["id"] != id, data))
    file = open('bd_contact.json', 'w')
    file.write(json.dumps(data))
    file.close()


def refresh():
    fenetre.update()
    fenetre.update_idletasks()


def formUpdateContact(element, fenetre2):
    print(element)
    x = tk.Entry(fenetre2)
    x.insert(0,element["name"])
    x.pack()
    x1 = tk.Entry(fenetre2)
    x1.insert(0,element["numero"])
    x1.pack()
    x2 = tk.Entry(fenetre2)
    x2.insert(0,element["autres"])
    x2.pack()
    tk.Button(fenetre2, text="Valider", command = lambda: updateContact(element["id"], x.get(), x1.get(), x2.get())).pack()


def updateContact(id, name, numero, autres):
    new_contact = {
        "id": id,
	    "name": name,
	    "numero" : numero,
	    "autres": autres
    }
    with open('bd_contact.json') as mon_fichier:
        data = json.load(mon_fichier)
    data = list(filter(lambda item: item["id"] != id, data))
    # print(data)
    data.append(new_contact)
    with open('bd_contact.json', 'w') as mon_fichier:
	    json.dump(data, mon_fichier)


def getIdContact(id):
    fenetre2 = tk.Tk()
    fenetre2.title("Afficher contact")
    print(id)
    with open('bd_contact.json') as mon_fichier:
        data = json.load(mon_fichier)
    for element in data:
        if (element["id"] == id):
            tk.Label(fenetre2, text=element["name"]).pack()
            tk.Label(fenetre2, text=element["numero"]).pack()
            tk.Label(fenetre2, text=element["autres"]).pack()
            tk.Button(fenetre2, text="modifier", command = lambda: formUpdateContact(element, fenetre2)).pack()
            tk.Button(fenetre2, text="générer", command = lambda: genererContact(element)).pack()
    fenetre2.geometry("500x500")
    fenetre2.mainloop()


def genererContact(element):
    f= open(element["name"] + ".txt","w+")
    f.write(element["name"])
    f.write("\n")
    f.write(element["numero"])
    f.write("\n")
    f.write(element["autres"])
    f.close()


def getAll():
    tk.Button(fenetre, text="Ajouter un contact", command = formAddContact).pack()
    for element in data:
        tk.Label(fenetre, text="--------").pack()
        tk.Label(fenetre, text=element["name"]).pack()
        tk.Label(fenetre, text=element["numero"]).pack()
        tk.Button(fenetre, text="afficher", command = lambda: getIdContact(element["id"])).pack()
        tk.Button(fenetre, text="supprimer", command = lambda: deleteContact(element["id"])).pack()
        
getAll()
tk.Button(fenetre, text="Refresh", command = refresh).pack()

fenetre.geometry("1000x1000")

fenetre.mainloop()
