# test_data.py

LIVRES_TEST = {
    "L001": {
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupéry",
        "genre": "Fiction",
        "annee": 1943,
        "disponible": True,
        "nombre_emprunts": 0
    },
    "L002": {
        "titre": "1984",
        "auteur": "George Orwell",
        "genre": "Dystopie",
        "annee": 1949,
        "disponible": True,
        "nombre_emprunts": 5
    }
}

MEMBRES_TEST = {
    "M001": {
        "nom": "Dupont",
        "prenom": "Jean",
        "email": "jean.dupont@email.com",
        "date_inscription": "2024-01-15",
        "livres_empruntes": [],
        "historique_emprunts": []
    },
    "M002": {
        "nom": "Martin",
        "prenom": "Marie",
        "email": "marie.martin@email.com",
        "date_inscription": "2024-02-10",
        "livres_empruntes": [],
        "historique_emprunts": []
    }
}

EMPRUNTS_TEST = [
    {
        "id_emprunt": "EMP001",
        "id_membre": "M001",
        "id_livre": "L001",
        "date_emprunt": "2024-03-15",
        "date_retour_prevue": "2024-04-15",
        "date_retour_effective": None,
        "statut": "en_cours"
    }
]