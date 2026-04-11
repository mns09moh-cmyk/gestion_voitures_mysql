import json
import mysql.connector

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




