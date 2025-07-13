# gestion_emprunts.py

from datetime import datetime, timedelta
import utils

def gestion_emprunts(livres, membres, emprunts):
    while True:
        print("\n=== GESTION DES EMPRUNTS ===")
        print("1. Emprunter un livre")
        print("2. Retourner un livre")
        print("3. Voir les emprunts en cours")
        print("4. Voir les livres en retard")
        print("5. Retour au menu principal")

        try:
            sous_choix = int(input("Votre choix : "))
            
            if sous_choix == 1:
                emprunter_livre(livres, membres, emprunts)
            elif sous_choix == 2:
                retourner_livre(livres, membres, emprunts)
            elif sous_choix == 3:
                afficher_emprunts_en_cours(emprunts)
            elif sous_choix == 4:
                afficher_livres_en_retard(emprunts)
            elif sous_choix == 5:
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

def emprunter_livre(livres, membres, emprunts):
    id_membre = input("ID du membre : ")
    id_livre = input("ID du livre : ")

    if id_membre not in membres:
        print("Membre non trouvé.")
        return
    if id_livre not in livres:
        print("Livre non trouvé.")
        return
    if not livres[id_livre]["disponible"]:
        print("Ce livre n'est pas disponible.")
        return

    # Génère ID d'emprunt unique
    id_emprunt = f"EMP{len(emprunts) + 1}"

    # Date actuelle et date de retour prévue (30 jours plus tard)
    date_emprunt = datetime.now().strftime("%Y-%m-%d")
    date_retour_prevue = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    nouvel_emprunt = {
        "id_emprunt": id_emprunt,
        "id_membre": id_membre,
        "id_livre": id_livre,
        "date_emprunt": date_emprunt,
        "date_retour_prevue": date_retour_prevue,
        "date_retour_effective": None,
        "statut": "en_cours"
    }

    emprunts.append(nouvel_emprunt)

    # Met à jour le statut du livre
    livres[id_livre]["disponible"] = False
    membres[id_membre]["livres_empruntes"].append(id_livre)

    print(f"Livre '{livres[id_livre]['titre']}' emprunté avec succès par {membres[id_membre]['prenom']} {membres[id_membre]['nom']}.")
    print(f"Date de retour prévue : {date_retour_prevue}")

def retourner_livre(livres, membres, emprunts):
    id_livre = input("ID du livre à retourner : ")
    id_membre = input("ID du membre : ")

    # Trouver l'emprunt en cours
    for emprunt in emprunts:
        if emprunt["id_livre"] == id_livre and emprunt["id_membre"] == id_membre and emprunt["statut"] == "en_cours":
            date_retour = datetime.now().strftime("%Y-%m-%d")
            emprunt["date_retour_effective"] = date_retour
            emprunt["statut"] = "terminé"

            # Met à jour le livre et le membre
            livres[id_livre]["disponible"] = True
            livres[id_livre]["nombre_emprunts"] += 1
            membres[id_membre]["livres_empruntes"].remove(id_livre)
            membres[id_membre]["historique_emprunts"].append(id_livre)

            # Calcul du retard et de l’amende
            retard = utils.calculer_retard(emprunt["date_retour_prevue"], date_retour)
            amende = utils.calculer_amende(retard)

            print(f"Livre retourné avec succès le {date_retour}.")
            if retard > 0:
                print(f"Retard de {retard} jours. Amende : {amende} €")
            else:
                print("Aucun retard constaté.")
            return

    print("Aucun emprunt en cours trouvé pour ce livre et ce membre.")

def afficher_emprunts_en_cours(emprunts):
    print("\nEmprunts en cours :")
    for emprunt in emprunts:
        if emprunt["statut"] == "en_cours":
            print(f"\nID Emprunt: {emprunt['id_emprunt']}")
            for k, v in emprunt.items():
                print(f"{k}: {v}")

def afficher_livres_en_retard(emprunts):
    print("\nLivres en retard :")
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d")

    for emprunt in emprunts:
        if emprunt["statut"] == "en_cours" and emprunt["date_retour_prevue"] < now:
            retard = utils.calculer_retard(emprunt["date_retour_prevue"])
            amende = utils.calculer_amende(retard)
            print(f"\nID Emprunt: {emprunt['id_emprunt']}")
            print(f"ID Membre: {emprunt['id_membre']}")
            print(f"ID Livre: {emprunt['id_livre']}")
            print(f"Date retour prévue: {emprunt['date_retour_prevue']}")
            print(f"Retard: {retard} jours | Amende: {amende} €")