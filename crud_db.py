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




