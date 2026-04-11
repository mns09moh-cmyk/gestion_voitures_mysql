import json
import mysql.connector
from voiture import Voiture

def connecter_db():
    try:
        with open("config.json", "r", encoding="utf-8") as fichier:
            config = json.load(fichier)

        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        return connexion

    except FileNotFoundError:
        print("Erreur : fichier config.json introuvable.")
        return None
    except json.JSONDecodeError:
        print("Erreur : format JSON invalide dans config.json.")
        return None
    except mysql.connector.Error as err:
        print(f"Erreur MySQL : {err}")
        return None
def creer_table_voiture(connexion):
    try:
        curseur = connexion.cursor()

        requete = """
        CREATE TABLE IF NOT EXISTS voiture(
            id INT AUTO_INCREMENT PRIMARY KEY,
            marque VARCHAR(50),
            modele VARCHAR(50),
            annee INT,
            prix DECIMAL(10,2)
        )
        """

        curseur.execute(requete)
        connexion.commit()
        curseur.close()

    except mysql.connector.Error as err:
        print(f"Erreur lors de la création de la table : {err}")
def ajouter_voiture(voiture):
    connexion = connecter_db()

    if connexion is None:
        return

    try:
        creer_table_voiture(connexion)

        curseur = connexion.cursor()
        requete = """
        INSERT INTO voiture (marque, modele, annee, prix)
        VALUES (%s, %s, %s, %s)
        """
        valeurs = (voiture.marque, voiture.modele, voiture.annee, voiture.prix)

        curseur.execute(requete, valeurs)
        connexion.commit()

        voiture.id = curseur.lastrowid

        print("Voiture ajoutée avec succès.")
        curseur.close()
        connexion.close()

    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout : {err}")
def supprimer_voiture(id_voiture):
    connexion = connecter_db()

    if connexion is None:
        return

    try:
        curseur = connexion.cursor()
        requete = "DELETE FROM voiture WHERE id = %s"

        curseur.execute(requete, (id_voiture,))
        connexion.commit()

        if curseur.rowcount > 0:
            print(f"Voiture avec ID {id_voiture} supprimée avec succès.")
        else:
            print(f"Aucune voiture trouvée avec ID {id_voiture}.")

        curseur.close()
        connexion.close()

    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression : {err}")
def recuperer_Voitures():
    connexion = connecter_db()

    if connexion is None:
        return []

    voitures = []

    try:
        curseur = connexion.cursor()
        requete = "SELECT id, marque, modele, annee, prix FROM voiture"
        curseur.execute(requete)

        resultats = curseur.fetchall()

        for ligne in resultats:
            voiture = Voiture(
                marque=ligne[1],
                modele=ligne[2],
                annee=ligne[3],
                prix=float(ligne[4]),
                id_voiture=ligne[0]
            )
            voitures.append(voiture)

        curseur.close()
        connexion.close()

    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err}")

    return voitures
def modifier_voiture(voiture):
    connexion = connecter_db()

    if connexion is None:
        return

    try:
        curseur = connexion.cursor()
        requete = """
        UPDATE voiture
        SET marque = %s, modele = %s, annee = %s, prix = %s
        WHERE id = %s
        """
        valeurs = (voiture.marque, voiture.modele, voiture.annee, voiture.prix, voiture.id)

        curseur.execute(requete, valeurs)
        connexion.commit()

        if curseur.rowcount > 0:
            print(f"Voiture avec ID {voiture.id} modifiée avec succès.")
        else:
            print(f"Aucune voiture trouvée avec ID {voiture.id}.")

        curseur.close()
        connexion.close()

    except mysql.connector.Error as err:
        print(f"Erreur lors de la modification : {err}")





