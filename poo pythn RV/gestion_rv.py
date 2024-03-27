from datetime import datetime, date
from client import Client
from rv import RendezVous
from medcin import Medecin  # Importer la classe Medecin depuis votre fichier medecin.py

class GestionRendezVous:
    next_id = 1  # Définition de next_id comme attribut de classe     
    next_client_id = 1
    next_medecin_id = 1

    def __init__(self):
        self.clients = []
        self.medecins = []  # Ajout de la liste des médecins
        self.logged_in_client = None
        self.logged_in_medecin = None
        self.appointments = []

    def create_account(self, nom, prenom, date_naissance, tel, email, adress, user, password):
        new_client = Client(GestionRendezVous.next_id, nom, prenom, date_naissance, tel, email, adress, user, password)
        self.clients.append(new_client)
        print("Compte créé avec succès. ID:", GestionRendezVous.next_id)
        GestionRendezVous.next_id += 1  # Incrémentez l'ID pour le prochain client

    def create_appointment(self, heure, id_client, typeRV):
        # Utiliser le format "%H:%M" pour correspondre à l'entrée "10:00"
        date_heure = datetime.combine(date.today(), datetime.strptime(heure, "%H:%M").time())
        statut = self.determine_status(date_heure)  # Déterminer automatiquement le statut du rendez-vous
        new_appointment_id = len(self.appointments) + 1  # ID du rendez-vous basé sur le nombre actuel de rendez-vous
        new_appointment = RendezVous(new_appointment_id, date_heure, statut, id_client, typeRV)
        self.appointments.append(new_appointment)
        print("Rendez-vous créé avec succès.")

    def create_medecin_account(self, nom, prenom, specialite, user, password):
        new_medecin = Medecin(GestionRendezVous.next_medecin_id, nom, prenom, specialite, user, password)
        self.medecins.append(new_medecin)
        print("Compte médecin créé avec succès. ID:", GestionRendezVous.next_medecin_id)
        GestionRendezVous.next_medecin_id += 1

    def determine_status(self, date_heure):
        if date_heure.time() < datetime.strptime("09:00", "%H:%M").time():
            return "NON DISPONIBLE"
        else:
            return "DISPONIBLE"

    def display_appointments(self):
        if self.appointments:
            print("Liste des rendez-vous:")
            for appointment in self.appointments:
                print(f"ID: {appointment.id}, Date et heure: {appointment.date_heure}, Statut: {appointment.statut}, ID client: {appointment.id_client}, Type: {appointment.typeRV}")
        else:
            print("Aucun rendez-vous trouvé.")

    def login(self, username, password):
        for client in self.clients:
            if client.user == username and client.password == password:
                self.logged_in_client = client
                print("Connexion réussie.")
                return
        print("Nom d'utilisateur ou mot de passe incorrect.")

    def logout(self):
        self.logged_in_client = None
        print("Déconnexion réussie.")
