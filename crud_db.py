import json
import mysql.connector
def connecter_db():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    connexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
    return connexion