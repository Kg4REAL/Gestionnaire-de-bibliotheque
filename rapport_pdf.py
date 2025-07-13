# rapport_pdf.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def generer_rapport_pdf(livres, membres, emprunts):
    nom_fichier = "rapport_bibliotheque.pdf"
    document = SimpleDocTemplate(nom_fichier, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    # Titre
    titre = Paragraph("Rapport de Statistiques de la Bibliothèque", styles['Title'])
    flowables.append(titre)
    flowables.append(Spacer(1, 24))

    # Top 5 des livres les plus empruntés
    flowables.append(Paragraph("Top 5 des Livres les Plus Empruntés", styles['Heading2']))
    data = [["Titre", "Auteur", "Nombre d'emprunts"]]
    top_livres = sorted(
        livres.items(),
        key=lambda x: x[1]["nombre_emprunts"],
        reverse=True
    )
    for id_livre, info in top_livres[:5]:
        data.append([info["titre"], info["auteur"], str(info["nombre_emprunts"])])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    flowables.append(table)
    flowables.append(Spacer(1, 12))

    # Membres les plus actifs
    flowables.append(Paragraph("Membres les Plus Actifs", styles['Heading2']))
    from collections import defaultdict
    compte_emprunts = defaultdict(int)
    for id_membre, info in membres.items():
        compte_emprunts[id_membre] = len(info["historique_emprunts"])
    membres_tries = sorted(compte_emprunts.items(), key=lambda x: x[1], reverse=True)

    data = [["Nom", "Prénom", "Nombre d'emprunts"]]
    for id_membre, count in membres_tries[:5]:
        info = membres[id_membre]
        data.append([info["nom"], info["prenom"], str(count)])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    flowables.append(table)
    flowables.append(Spacer(1, 12))

    # Livres en retard
    flowables.append(Paragraph("Livres en Retard", styles['Heading2']))
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d")
    data = [["ID Emprunt", "ID Membre", "ID Livre", "Retard (jours)", "Amende (€)"]]
    for emprunt in emprunts:
        if emprunt["statut"] == "en_cours" and emprunt["date_retour_prevue"] < now:
            retard = utils.calculer_retard(emprunt["date_retour_prevue"])
            amende = utils.calculer_amende(retard)
            data.append([emprunt["id_emprunt"], emprunt["id_membre"], emprunt["id_livre"], str(retard), f"{amende:.2f} €"])

    if len(data) > 1:
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        flowables.append(table)
    else:
        flowables.append(Paragraph("Aucun livre en retard.", styles['Normal']))

    flowables.append(Spacer(1, 12))

    # Statistiques par genre
    flowables.append(Paragraph("Statistiques par Genre", styles['Heading2']))
    from collections import defaultdict
    stats = defaultdict(lambda: {"nombre": 0, "emprunts": 0})
    for info in livres.values():
        genre = info["genre"]
        stats[genre]["nombre"] += 1
        stats[genre]["emprunts"] += info["nombre_emprunts"]

    data = [["Genre", "Nombre de Livres", "Nombre d'Emprunts"]]
    for genre, valeurs in stats.items():
        data.append([genre, str(valeurs["nombre"]), str(valeurs["emprunts"])])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    flowables.append(table)

    # Génère le PDF
    document.build(flowables)
    print(f"\n✅ Rapport généré avec succès : {nom_fichier}")