# statistiques.py

def afficher_statistiques(livres, emprunts):
    while True:
        print("\n=== STATISTIQUES ET RAPPORTS ===")
        print("1. Top 5 des livres les plus empruntés")
        print("2. Membres les plus actifs")
        print("3. Livres en retard")
        print("4. Statistiques par genre")
        print("5. Retour au menu principal")

        try:
            sous_choix = int(input("Votre choix : "))

            if sous_choix == 1:
                top_livres_empruntes(livres)
            elif sous_choix == 2:
                membres_plus_actifs()
            elif sous_choix == 3:
                livres_en_retard(emprunts)
            elif sous_choix == 4:
                statistiques_par_genre(livres)
            elif sous_choix == 5:
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

def top_livres_empruntes(livres):
    # Trie les livres par nombre d'emprunts
    top_livres = sorted(
        livres.items(),
        key=lambda x: x[1]["nombre_emprunts"],
        reverse=True
    )

    print("\nTop 5 des livres les plus empruntés :")
    for i, (id_livre, info) in enumerate(top_livres[:5], 1):
        print(f"{i}. {info['titre']} par {info['auteur']} - {info['nombre_emprunts']} emprunts")

def membres_plus_actifs(membres):
    # Compte le nombre total d'emprunts par membre
    from collections import defaultdict
    compte_emprunts = defaultdict(int)

    for id_membre, info in membres.items():
        compte_emprunts[id_membre] = len(info["historique_emprunts"])

    membres_tries = sorted(
        compte_emprunts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nMembres les plus actifs :")
    for i, (id_membre, count) in enumerate(membres_tries[:5], 1):
        nom_complet = f"{membres[id_membre]['prenom']} {membres[id_membre]['nom']}"
        print(f"{i}. {nom_complet} - {count} emprunts")

def livres_en_retard(emprunts):
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d")

    print("\nLivres en retard :")
    for emprunt in emprunts:
        if emprunt["statut"] == "en_cours" and emprunt["date_retour_prevue"] < now:
            retard = utils.calculer_retard(emprunt["date_retour_prevue"])
            amende = utils.calculer_amende(retard)
            print(f"\nID Emprunt: {emprunt['id_emprunt']}")
            print(f"ID Membre: {emprunt['id_membre']}")
            print(f"ID Livre: {emprunt['id_livre']}")
            print(f"Date retour prévue: {emprunt['date_retour_prevue']}")
            print(f"Retard: {retard} jours | Amende: {amende} €")

def statistiques_par_genre(livres):
    from collections import defaultdict

    stats = defaultdict(lambda: {"nombre": 0, "emprunts": 0})

    for info in livres.values():
        genre = info["genre"]
        stats[genre]["nombre"] += 1
        stats[genre]["emprunts"] += info["nombre_emprunts"]

    print("\nStatistiques par genre :")
    for genre, data in stats.items():
        print(f"{genre}: {data['nombre']} livres | {data['emprunts']} emprunts")

# statistiques.py

def afficher_statistiques(livres, emprunts):
    while True:
        print("\n=== STATISTIQUES ET RAPPORTS ===")
        print("1. Top 5 des livres les plus empruntés")
        print("2. Membres les plus actifs")
        print("3. Livres en retard")
        print("4. Statistiques par genre")
        print("5. Générer un rapport PDF")
        print("6. Retour au menu principal")

        try:
            sous_choix = int(input("Votre choix : "))
            
            if sous_choix == 1:
                top_livres_empruntes(livres)
            elif sous_choix == 2:
                membres_plus_actifs(membres)
            elif sous_choix == 3:
                livres_en_retard(emprunts)
            elif sous_choix == 4:
                statistiques_par_genre(livres)
            elif sous_choix == 5:
                from rapport_pdf import generer_rapport_pdf
                generer_rapport_pdf(livres, membres, emprunts)
            elif sous_choix == 6:
                break
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")        