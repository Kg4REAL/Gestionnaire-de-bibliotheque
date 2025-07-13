# gestion_livres.py

def gestion_livres(livres):
    while True:
        print("\n=== GESTION DES LIVRES ===")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Modifier un livre")
        print("5. Retour au menu principal")

        try:
            sous_choix = int(input("Votre choix : "))
            
            if sous_choix == 1:
                ajouter_livre(livres)
            elif sous_choix == 2:
                afficher_livres(livres)
            elif sous_choix == 3:
                rechercher_livre(livres)
            elif sous_choix == 4:
                modifier_livre(livres)
            elif sous_choix == 5:
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

def ajouter_livre(livres):
    id_livre = input("Entrez l'ID du livre (ex: L003) : ")
    titre = input("Titre du livre : ")
    auteur = input("Auteur : ")
    genre = input("Genre : ")
    annee = int(input("Année de publication : "))
    
    livres[id_livre] = {
        "titre": titre,
        "auteur": auteur,
        "genre": genre,
        "annee": annee,
        "disponible": True,
        "nombre_emprunts": 0
    }
    print(f"Le livre '{titre}' a été ajouté avec succès !")

def afficher_livres(livres):
    print("\nListe des livres :")
    for id_livre, info in livres.items():
        print(f"\nID : {id_livre}")
        for k, v in info.items():
            print(f"{k} : {v}")

def rechercher_livre(livres):
    critere = input("Rechercher par titre, auteur ou genre : ").lower()
    resultats = []

    for id_livre, info in livres.items():
        if (critere in info["titre"].lower() or
            critere in info["auteur"].lower() or
            critere in info["genre"].lower()):
            resultats.append((id_livre, info))

    if resultats:
        print("\nRésultats de la recherche :")
        for id_livre, info in resultats:
            print(f"\nID : {id_livre}")
            for k, v in info.items():
                print(f"{k} : {v}")
    else:
        print("Aucun livre trouvé.")

def modifier_livre(livres):
    id_livre = input("Entrez l'ID du livre à modifier : ")
    if id_livre in livres:
        print("Modifier les informations de :", livres[id_livre]["titre"])
        titre = input("Nouveau titre (laisser vide pour garder) : ") or livres[id_livre]["titre"]
        auteur = input("Nouvel auteur (laisser vide pour garder) : ") or livres[id_livre]["auteur"]
        genre = input("Nouveau genre (laisser vide pour garder) : ") or livres[id_livre]["genre"]
        annee = input("Nouvelle année (laisser vide pour garder) : ") or livres[id_livre]["annee"]

        livres[id_livre].update({
            "titre": titre,
            "auteur": auteur,
            "genre": genre,
            "annee": int(annee)
        })
        print("Livre mis à jour avec succès !")
    else:
        print("Livre non trouvé.")