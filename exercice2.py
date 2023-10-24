#Créer votre propre interface à l'aide de Tkinter, pour afficher une interface d'inscription donc  Pseudo, mdp, email.
#Et lorsqu'on valide l'inssription ca m'affiche sur le terminal les données 

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Inscription")

def action_validerBouton():
    dict = {}
    
    if (champ_pseudo.get() == "" or champ_email.get() == "" or champ_mdp.get() == "" or champ_mdpConfirm.get() == ""):
        etiquette_response = tk.Label(fenetre, text="Erreur : Tous les champs sont obligatoires")
    else:  
        if (champ_mdp.get() != champ_mdpConfirm.get()):
            etiquette_response = tk.Label(fenetre, text="Erreur : les deux mots de passe saisies sont différents")
        else:
            etiquette_response = tk.Label(fenetre, text="Vous êtes inscrits ! ")
            dict["Pseudo"] = champ_pseudo.get()
            dict["Email"] = champ_email.get()
            dict["Mot de passe"] = champ_mdp.get()
            for element in dict:
                print(element + " : " + dict[element])
    
    etiquette_response.pack()
    

etiquette_pseudo = tk.Label(fenetre, text="Pseudo")
etiquette_email = tk.Label(fenetre, text="Email")
etiquette_mdp = tk.Label(fenetre, text="Mot de passe")
etiquette_mdpconfirm = tk.Label(fenetre, text="Confirmer votre mot de passe")

champ_pseudo = tk.Entry(fenetre)
champ_email = tk.Entry(fenetre)
champ_mdp = tk.Entry(fenetre)
champ_mdpConfirm = tk.Entry(fenetre)

etiquette_pseudo.pack()
champ_pseudo.pack()
etiquette_email.pack()
champ_email.pack()
etiquette_mdp.pack()
champ_mdp.pack()
etiquette_mdpconfirm.pack()
champ_mdpConfirm.pack()

bouton = tk.Button(fenetre, text="Envoyer", command=action_validerBouton)
bouton.pack()

etiquette_response = tk.Label(fenetre, text=" ")
etiquette_response.pack()


fenetre.geometry("500x400")

fenetre.mainloop() #la fenêtre reste ouverte jusqu'à la fermeture utilisateur

