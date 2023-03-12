import random, re

# Créer une liste de cartes avec les valeurs et les couleurs
valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As","Joker","Joker"]
couleurs = [(chr(3)),(chr(4)),(chr(5)),(chr(6))]
cartes = []
nb_player = 0
tapis = []

# Boucler sur toutes les couleurs et les valeurs pour créer les 52 cartes
for couleur in couleurs:
    for valeur in valeurs:
        carte = valeur + couleur
        cartes.append(carte)

# Afficher la liste des cartes
# print(cartes)

# Parcourir chaque carte de la liste
for i in range(len(cartes)):
    # Parcourir chaque caractère de la carte
    for j in range(len(cartes[i])):
        # Vérifier si le caractère est imprimable
        if not cartes[i][j].isprintable():
            # Remplacer le caractère par une chaîne vide
            cartes[i] = cartes[i].replace(cartes[i][j], "")

# Afficher la liste de cartes sans les caractères ASCII
print(f"Test : {cartes}")

# Mélanger les cartes
random.shuffle(cartes)

# Demander le nombre de joueurs
nombre_joueurs = int(input("Combien de joueurs y a-t-il ? "))

# Calculer le nombre de cartes à distribuer à chaque joueur
nombre_cartes_par_joueur = len(cartes) // nombre_joueurs

# Distribuer les cartes à chaque joueur
joueurs = []
for i in range(nombre_joueurs):
    main = []
    for j in range(nombre_cartes_par_joueur):
        carte = cartes.pop()
        main.append(carte)
    joueurs.append(main)

# Distribuer les cartes restantes (s'il en reste) à un joueur aléatoire
while cartes:
    joueur_aleatoire = random.randint(0, nombre_joueurs-1)
    carte = cartes.pop()
    joueurs[joueur_aleatoire].append(carte)

    
# Boucler sur les joueurs pour jouer un tour de jeu
joueur_actuel = 0
while True:
    # Afficher la main du joueur actuel
    main_joueur_actuel = joueurs[joueur_actuel]
    print("Joueur", joueur_actuel+1, ", c'est à toi de jouer.")
    print("Ta main :", main_joueur_actuel)
    
    # Demander au joueur de sélectionner une carte à jouer
    choix = int(input("Sélectionnez l'index de la carte à jouer : "))

    # Extraire la carte sélectionnée de la main du joueur
    carte_jouee = main_joueur_actuel.pop(choix)

    # Afficher la carte jouée sur la table
    print("Carte jouée : ", carte_jouee)
    # ...
    
    # Passer au joueur suivant
    joueur_actuel = (joueur_actuel + 1) % nombre_joueurs
