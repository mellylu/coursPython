#Créer un programme qui permet à l'utilisateur de saisir et de gérer des informations personnelles telles que le nom, l'âge, 
#la taille, la liste des fruits préférés, un message de salutation personnalisé, les propriétés d'un produit, la manipulation 
#de chaînes de caractères et l'entrée de l'utilisateur.

prenom = input("Bonjour, quel est votre prénom ? ")
prenom = prenom.capitalize() 
nom = input ("Bonjour " + prenom + ", quel est votre nom de famille ? ")
nom = nom.upper()
print("Enchanté " + prenom + " " + nom)

information = {"nom" : nom, "prenom" : prenom}
produit = {}
fini = "yes"
while (fini != "no") :
    nomProduit = input("Quel produit voulez vous ajouter dans votre panier ? ")
    priceProduit = input("Quel est son prix ? ")
    if (isinstance(priceProduit, (int, float)) == False and priceProduit.isdigit() == False ):
        priceProduit = input("Erreur : ce n'est pas un nombre, quel est le prix de l'article ? ")
    produit[nomProduit] = priceProduit
    fini = input('Voulez vous rajouter des produits (yes/no): ')

print(information["prenom"] + " " + information["nom"] + ", " + "vous avez dans votre panier : ")

i = 1
for element in produit:
    print("Article " + str(i) + " : " + element + " => " + produit[element] + " euros")
    i += 1
    