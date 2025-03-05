import json
import os
import random
import typing

file_name = "/Users/imac_j06/Desktop/your-first-contribution/python-25/user-management/db.json"
bd_content:dict[str, list[dict]] = {}

with open(file_name, "r") as file:
    bd_content = json.load(file)


def login(email: str, password: str):
    users = bd_content.get("Users",[])

    for user in users:
        if user["email"] == email and user["password"] == password:
            return user

    

def register(email: str, password: str):
    if os.path.exists(file_name):
            data = load_db(file_name)
            data["Users"].append({"email": email, "password": password, "role": "USER"})
            save_db(data, file_name)
    else:
        data = {"Users": [{"email": email, "password": password, "role": "USER"}]}
        save_db(data, file_name)

    print("Inscription réussie !")

def forgot_password(email: str):

    db_content = load_db(file_name)

    users = db_content["Users"]

    for user in users:  # Parcours de la liste des comptes enregistrés
        if email == user["email"]:  # Vérification de l'existence de l'email
            verification_code = str(
                random.randint(1000, 9999)
            )  # Génération d'un code aléatoire à 4 chiffres
            print(f"Code de vérification : {verification_code}")
            user_code = input("Veuillez entrer le code affiché : ")

            while user_code != verification_code:
                print("Le code saisi est incorrect. ")
                verification_code = str(
                    random.randint(1000, 9999)
                )  # Génération d'un code aléatoire à 4 chiffres
                print(f"Code de vérification : {verification_code}")
                user_code = input("Veuillez entrer le code affiché : ")

            new_password = input("Entrez votre nouveau mot de passe : ")
            user["password"] = new_password  # Mise à jour du nouveau mot de passe
            db_content['Users'] = users
            save_db(db_content, file_name)
            return True
    return False

def load_db(file):
    """Charge les utilisateurs depuis le fichier JSON."""
    with open(file, "r") as f:
        return json.load(f)

def save_db(data, file):
    """Sauvegarde les données dans le fichier JSON."""
    with open(file, "w") as file:
        json.dump(data, file, indent=4)


def list_users(file):
    """Affiche la liste des utilisateurs enregistrés."""
    bd_content = load_db(file)  # On charge les données du fichier JSON
    users = bd_content.get("Users", [])  # On récupère la liste des utilisateurs

    if not users:  # Si la liste est vide
        print("Aucun utilisateur enregistré.")
        return

    print("Liste des utilisateurs :")
    for user in users:  # On parcourt chaque utilisateur
        print(f"Email: {user['email']}, Rôle: {user['role']}")  # On affiche son email et son rôle

def ask_email_pass():
    email = input("Veuillez saisir votre adresse email : ")
    password = input("Veuillez saisir votre mot de passe : ")

    return (email, password)

