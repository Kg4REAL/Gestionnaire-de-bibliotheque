# utils.py

import re
from datetime import datetime

def generer_id_membre(membres):
    """Génère un nouvel ID unique pour un membre"""
    max_id = 0
    for id_membre in membres:
        if id_membre.startswith("M") and id_membre[1:].isdigit():
            num = int(id_membre[1:])
            if num > max_id:
                max_id = num
    return f"M{max_id + 1}"

def generer_id_livre(livres):
    """Génère un nouvel ID unique pour un livre"""
    max_id = 0
    for id_livre in livres:
        if id_livre.startswith("L") and id_livre[1:].isdigit():
            num = int(id_livre[1:])
            if num > max_id:
                max_id = num
    return f"L{max_id + 1}"

def valider_email(email):
    """Valide le format d'email"""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

def valider_date(date_str):
    """Vérifie si la date est au format YYYY-MM-DD"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculer_retard(date_prevue, date_effective=None):
    """Calcule le nombre de jours de retard entre deux dates"""
    from datetime import datetime

    date_prevue = datetime.strptime(date_prevue, "%Y-%m-%d")
    date_effective = datetime.strptime(date_effective or datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
    delta = (date_effective - date_prevue).days
    return max(0, delta)  # Ne retourne que les retards positifs

def calculer_amende(retard_jours):
    """Calcule l'amende à 0.5€ par jour de retard"""
    return round(retard_jours * 0.5, 2)