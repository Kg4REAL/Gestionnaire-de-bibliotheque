# Système de Gestion de Bibliothèque

📚 Ce projet est un système de gestion de bibliothèque développé en Python.  
Il permet de gérer les livres, les membres, les emprunts, ainsi que de générer des statistiques et rapports.

---

## 🧩 Fonctionnalités

- ✅ Ajouter, modifier et afficher des livres
- ✅ Inscrire et gérer des membres
- ✅ Gérer les emprunts et retours avec calcul d’amende
- ✅ Statistiques : top 5 des livres, membres actifs, livres en retard
- ✅ Sauvegarde automatique dans un fichier JSON
- ✅ Génération d’un rapport PDF des statistiques

---

## 🗂️ Structure du Projet
bibliotheque/
├── main.py                  # Point d'entrée du programme
├── gestion_livres.py        # Fonctions pour gérer les livres
├── gestion_membres.py       # Fonctions pour gérer les membres
├── gestion_emprunts.py      # Fonctions pour gérer les emprunts
├── statistiques.py          # Statistiques et rapports
├── utils.py                 # Fonctions utilitaires (dates, emails, ID…)
├── rapport_pdf.py           # Génération de rapports PDF
└── test_data.py             # Données de test initiales 


 
---

## ⚙️ Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/votre-nom/bibliotheque.git 
   cd bibliotheque
   

2. Installe les dépendances nécessaires :
   ```bash
   pip install reportlab
3.  Lance le programme : 
  
  
💾 Données sauvegardées 

Les données sont sauvegardées automatiquement dans un fichier nommé bibliotheque.json. 
 
📊 Rapport PDF 

Depuis le menu des statistiques, vous pouvez générer un rapport PDF qui inclut : 

    Le top 5 des livres
    Les membres les plus actifs
    Les livres en retard
    Des statistiques par genre
     

 
📌 Utilisation 

Le programme propose un menu interactif permettant de naviguer entre les différentes fonctionnalités : 

    Gestion des livres
    Gestion des membres
    Gestion des emprunts
    Affichage des statistiques
    Génération de rapports PDF
     

 
🤝 Contribution 

Les contributions sont bienvenues !
N’hésite pas à améliorer ce projet ou à ajouter de nouvelles fonctionnalités comme une interface graphique ou une base de données SQLite. 
 
© Licence 

Ce projet est sous licence MIT. 
 



