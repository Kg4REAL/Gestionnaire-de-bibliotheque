# gestion_membres.py

def gestion_membres(membres):
    while True:
        print("\n=== GESTION DES MEMBRES ===")
        print("1. Inscrire un nouveau membre")
        print("2. Afficher tous les membres")
        print("3. Rechercher un membre")
        print("4. Voir l'historique d'emprunts")
        print("5. Retour au menu principal")

        try:
            sous_choix = int(input("Votre choix : "))
            
            if sous_choix == 1:
                inscrire_membre(membres)
            elif sous_choix == 2:
                afficher_membres(membres)
            elif sous_choix == 3:
                rechercher_membre(membres)
            elif sous_choix == 4:
                voir_historique(membres)
            elif sous_choix == 5:
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
# gestion_membres.py

def inscrire_membre(membres):
    print("\n=== INSCRIPTION D'UN NOUVEAU MEMBRE ===")

    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    email = input("Email : ").strip()

    # Validation de l'email
    while not utils.valider_email(email):
        print("Adresse email invalide. Veuillez réessayer.")
        email = input("Email : ").strip()

    # Génération automatique de l'ID membre
    id_membre = utils.generer_id_membre(membres)
    print(f"ID généré automatiquement : {id_membre}")

    # Date d'inscription (optionnelle ou automatique)
    reponse = input("Souhaitez-vous entrer une date d'inscription manuelle ? (o/n) : ").lower()
    if reponse == "o":
        date_inscription = input("Date d'inscription (YYYY-MM-DD) : ").strip()
        while not utils.valider_date(date_inscription):
            print("Format de date invalide. Veuillez utiliser YYYY-MM-DD.")
            date_inscription = input("Date d'inscription (YYYY-MM-DD) : ").strip()
    else:
        from datetime import datetime
        date_inscription = datetime.now().strftime("%Y-%m-%d")
        print(f"Date d'inscription définie automatiquement au : {date_inscription}")

    membres[id_membre] = {
        "nom": nom,
        "prenom": prenom,
        "email": email,
        "date_inscription": date_inscription,
        "livres_empruntes": [],
        "historique_emprunts": []
    }

    print(f"\nMembre '{prenom} {nom}' ajouté avec succès !")
    print(f"ID attribué : {id_membre}")
    print(f"Email validé : {email}")
    print(f"Date d'inscription : {date_inscription}")

def afficher_membres(membres):
    print("\nListe des membres :")
    for id_membre, info in membres.items():
        print(f"\nID : {id_membre}")
        for k, v in info.items():
            print(f"{k} : {v}")

def rechercher_membre(membres):
    critere = input("Rechercher par nom ou email : ").lower()
    resultats = []

    for id_membre, info in membres.items():
        if critere in info["nom"].lower() or critere in info["email"].lower():
            resultats.append((id_membre, info))

    if resultats:
        print("\nRésultats de la recherche :")
        for id_membre, info in resultats:
            print(f"\nID : {id_membre}")
            for k, v in info.items():
                print(f"{k} : {v}")
    else:
        print("Aucun membre trouvé.")

def voir_historique(membres):
    id_membre = input("Entrez l'ID du membre : ")
    if id_membre in membres:
        print(f"\nHistorique d'emprunts pour {membres[id_membre]['prenom']} {membres[id_membre]['nom']} :")
        historique = membres[id_membre]["historique_emprunts"]
        if historique:
            for emprunt in historique:
                print(emprunt)
        else:
            print("Aucun emprunt dans l'historique.")
    else:
        print("Membre non trouvé.")