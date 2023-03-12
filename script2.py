import random

# Définition des constantes
NOMBRE_JOUEURS = 4
PASSE = -1
CARTES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi', 'as']
VALEURS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'valet': 11, 'dame': 12, 'roi': 13, 'as': 14}

# Définition des fonctions
def creer_paquet():
    """Crée un paquet de 52 cartes"""
    paquet = []
    for carte in CARTES:
        paquet.append(carte + ' de coeur')
        paquet.append(carte + ' de pique')
        paquet.append(carte + ' de carreau')
        paquet.append(carte + ' de trèfle')
    return paquet
# print(creer_paquet())
paquet = creer_paquet()

def distribuer_cartes(paquet, nombre_joueurs):
    """Distribue les cartes aux joueurs"""
    random.shuffle(paquet)
    mains = [paquet[i::nombre_joueurs] for i in range(nombre_joueurs)]
    resultat = ""
    for i, main in enumerate(mains):
        resultat += f"Joueur {i+1}: {', '.join(main)}\n\n"
    return resultat.strip()
print(distribuer_cartes(paquet, 2))

def jouer_un_tour(joueurs, carte_maitresse):
    """Permet à chaque joueur de jouer une carte"""
    cartes_jouees = []
    for joueur in joueurs:
        # print(f"C'est au joueur {joueur['nom']} de jouer.")
        print(f"La carte maîtresse est : {carte_maitresse}")
        carte_jouee = None
        while carte_jouee not in joueur['cartes'] and carte_jouee != PASSE:
            print(f"Cartes du joueur {joueur['nom']} : {joueur['cartes']}")
            carte_jouee = input("Quelle carte voulez-vous jouer ? (tapez 'passe' pour passer) ")
            if carte_jouee.lower() == 'passe':
                carte_jouee = PASSE
            elif carte_jouee in joueur['cartes']:
                joueur['cartes'].remove(carte_jouee)
        if carte_jouee != PASSE:
            cartes_jouees.append(carte_jouee)
        print()
    return cartes_jouees
print(jouer_un_tour("yolo","6 de coeur"))

def trouver_cartes_gagnantes(cartes_jouees):
    """Trouve les cartes gagnantes"""
    cartes_gagnantes = []
    for carte in cartes_jouees:
        if not cartes_gagnantes or VALEURS[carte[:-10]] > VALEURS[cartes_gagnantes[0][:-10]]:
            cartes_gagnantes = [carte]
        elif VALEURS[carte[:-10]] == VALEURS[cartes_gagnantes[0][:-10]]:
            cartes_gagnantes.append(carte)
    return cartes_gagnantes

def afficher_gagnant(tour, gagnant):
    """Affiche le gagnant du tour"""
    print(f"Tour {tour} : le gagnant est {gagnant['nom']} !\n")

def afficher_perdant(tour, perdant):
    """Affiche le perdant du tour"""
    print(f"Tour {tour} : le perdant est {perdant['nom']} !\n")