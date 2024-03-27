from gestion_rv import GestionRendezVous
def menu_connecte():
    while gestion_rdv.logged_in_client:
        print("\nMenu connecté:")
        print("1. Créer un rendez-vous")
        print("2. Afficher les rendez-vous")
        print("3. Choisir un rendez-vous")
        print("4. Se déconnecter")
            
        inner_choice = input("Choisissez une option: ")

        if inner_choice == "1":
            date_heure = input("Heure du rendez-vous (format HH:MM): ")
            id_client = gestion_rdv.logged_in_client.id
            typeRV = input("Type de rendez-vous: ")
            gestion_rdv.create_appointment(date_heure, id_client, typeRV)

        elif inner_choice == "2":
            gestion_rdv.display_appointments()

        elif inner_choice == "4":
            gestion_rdv.logout()
            break

        elif inner_choice == "3":
            heure_choisie = input("Entrez l'heure du rendez-vous (format HH:MM): ")
            if any(appointment.date_heure.strftime("%H:%M") == heure_choisie for appointment in gestion_rdv.appointments):
                print("Cette heure est déjà prise.")
            else:
                print("Cette heure est disponible.")

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")



gestion_rdv = GestionRendezVous()

while True:
    print("\nMenu:")
    print("1. Créer un compte")
    print("2. Se connecter")
    print("3. Se déconnecter")
    print("4. Quitter")

    choice = input("Choisissez une option: ")

    if choice == "1":
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        date_naissance = input("Date de naissance: ")
        tel = input("Téléphone: ")
        email = input("Email: ")
        adress = input("Adresse: ")
        user = input("Nom d'utilisateur: ")
        password = input("Mot de passe: ")
        gestion_rdv.create_account(nom, prenom, date_naissance, tel, email, adress, user, password)
        menu_connecte()  # Appeler le menu connecté après la création du compte

    elif choice == "2":
        if gestion_rdv.logged_in_client:
            print("Vous êtes déjà connecté.")
        else:
            username = input("Nom d'utilisateur: ")
            password = input("Mot de passe: ")
            gestion_rdv.login(username, password)
            menu_connecte()  # Appeler le menu connecté après la connexion

    elif choice == "3":
        if gestion_rdv.logged_in_client:
            gestion_rdv.logout()
        else:
            print("Vous n'êtes pas connecté.")

    elif choice == "4":
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
