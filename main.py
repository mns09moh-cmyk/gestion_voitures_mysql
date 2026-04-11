from voiture import Voiture
from crud_db import connecter_db, ajouter_voiture, supprimer_voiture, recuperer_voitures, modifier_voiture


def tester_connexion():
    print("=== TEST CONNEXION ===")
    connexion = connecter_db()

    if connexion is not None:
        print("Connexion à MySQL réussie.")
        connexion.close()
        print("Connexion fermée.")
    else:
        print("Échec de la connexion.")