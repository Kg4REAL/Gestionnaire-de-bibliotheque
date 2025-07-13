# main.py

import json
import os
from gestion_livres import gestion_livres
from gestion_membres import gestion_membres
from gestion_emprunts import gestion_emprunts
from statistiques import afficher_statistiques

FICHIER_SAUV = "bibliotheque.json"

def charger_donnees():
    """Charge les données depuis le fichier JSON s'il existe."""
    if os.path.exists(FICHIER_SAUV):
        with open(FICHIER_SAUV, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return (
                    data.get("livres", {}),
                    data.get("membres", {}),
                    data.get("emprunts", [])
                )
            except json.JSONDecodeError:
                print("Erreur lors de la lecture du fichier JSON. Réinitialisation...")
    return {}, {}, []

def sauvegarder_donnees(livres, membres, emprunts):
    """Sauvegarde les données dans un fichier JSON."""
    data = {
        "livres": livres,
        "membres": membres,
        "emprunts": emprunts
    }
    with open(FICHIER_SAUV, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Données sauvegardées avec succès.")

def main():
    # Charger les données existantes ou initialiser
    livres, membres, emprunts = charger_donnees()

    if not livres:  # Si vide, on ajoute quelques données test
        from test_data import LIVRES_TEST, MEMBRES_TEST, EMPRUNTS_TEST
        livres = LIVRES_TEST
        membres = MEMBRES_TEST
        emprunts = EMPRUNTS_TEST
        sauvegarder_donnees(livres, membres, emprunts)

    while True:
        print("\n=============== BIENVENUE ===============")
        print("=== SYSTÈME DE GESTION DE BIBLIOTHÈQUE ===")
        print("1. Gestion des livres")
        print("2. Gestion des membres")
        print("3. Gestion des emprunts")
        print("4. Statistiques et rapports")
        print("5. Quitter")

        try:
            choix = int(input("Votre choix : "))
            
            if choix == 1:
                gestion_livres(livres)
            elif choix == 2:
                gestion_membres(membres)
            elif choix == 3:
                gestion_emprunts(livres, membres, emprunts)
            elif choix == 4:
                afficher_statistiques(livres, emprunts)
            elif choix == 5:
                sauvegarder_donnees(livres, membres, emprunts)
                print("Merci d'utiliser notre système. Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez choisir entre 1 et 5.")
        
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()