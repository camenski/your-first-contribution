import fonctions


# Menu affiché à l'utilisateur
menu = """"
1. Ajouter un client
2. Lister les utilisateurs
3. Deconnexion
"""

menu_global = """
1. Connexion
2. Mot de passe oublié
"""

while True:
    print(menu_global)  # Affichage des options
    choix = input("Veuillez saisir un menu : ")  # Demande du choix

    if choix == "1":
        user_info = None
       
    
        while not user_info:
            email, password = fonctions.ask_email_pass()
            user_info = fonctions.login(email, password)
        

        if user_info[2] == "ADMIN":  # l'utilisateur est un admin
            print("Bienvenue administrateur : ", user_info[0])
        
            print(menu)
            choix = input("Veuillez saisir un menu : ")

            if choix == "1":
                email, password = fonctions.ask_email_pass()
                fonctions.register(email, password)

            elif choix == "2":  # Mot de passe oublié
                print("list des utilisateurs")

            elif choix == "3":  # Quitter
                print("Déconnexion !")
                break
        else:  # l'utilisateur est un client
            print("Bienvenue client")

    else:
        print("Choix incorrect, veuillez réessayer. ")