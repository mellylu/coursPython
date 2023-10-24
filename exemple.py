#boucle
x = 1
while x <= 10 :
    if (x % 2 == 0):
        print(x)
    x = x + 1

#liste
liste = ["pomme", "poire", "noix"]
print(liste[0])

#fonction
def saluer(nom):
    print("Bonjour " + nom)
saluer("Madame")

#dictionnaire => chaque clé est associée à une valeur
personne = {"nom": "Lucas", "age":24, "ville":"Saint Germain en Laye"}
print(personne["nom"])
print(personne["ville"])

#input
nom = input("Entrez votre nom :")
print("Bonjour, " + nom)
