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
def tester_ajout():
    print("\n=== TEST AJOUT ===")
    v1 = Voiture("Toyota", "Corolla", 2020, 18500.00)
    v2 = Voiture("Honda", "Civic", 2019, 17200.50)
    v3 = Voiture("Ford", "Focus", 2018, 14999.99)

    ajouter_voiture(v1)
    ajouter_voiture(v2)
    ajouter_voiture(v3)

    print("Voitures ajoutées :")
    v1.afficher_voiture()
    v2.afficher_voiture()
    v3.afficher_voiture()

    return v1, v2, v3