#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tampon as gestionaire
from tools import effacer_terminal, definput
import fichier as disque

def lancement():
    fichier = input("Entrez le nom du fichier: ")
    binaire = 0 if definput("Voulez-vous ouvrir le fichier en binaire (O/N)", "N").lower() == 'n' else 1
    run(fichier, binaire=binaire)



def run(nom_fichier, binaire=0):
    """
    Editeur de texte entier
    """
    sigma = True
    fichier_lignes = gestionaire.chaine_vers_liste(disque.lire(nom_fichier, binaire=binaire))
    
    gestionaire.afficher_fichier(fichier_lignes)
    while sigma:
        if binaire:
            print("\n\nLes retours a la ligne ne changent rien ici, ils sont juste présents pour plus de lisibilité.")
        choix = input("[M]odifier une ligne, [I]nsérer une ligne, s[U]pprimer une ligne, [C]hercher une chaîne, [S]auvegarder, [Q]uitter: ").strip().lower()

        if choix == 'm':
            try:
                numero_ligne = int(input("Numéro de la ligne à modifier : "))
                nouvelle_ligne = definput("Nouvelle ligne", fichier_lignes[numero_ligne-1])
                fichier_lignes = gestionaire.modifier_ligne(fichier_lignes, numero_ligne, nouvelle_ligne)
            except ValueError:
                pass # c'est moche mais ca marche
            gestionaire.afficher_fichier(fichier_lignes)
        
        elif choix == 'i':
            if fichier_lignes != []:
                try:
                    numero_ligne = int(input("Numéro de la ligne avant laquelle insérer : "))
                    nouvelle_ligne = input("Nouvelle ligne à insérer : ")
                    fichier_lignes = gestionaire.inserer_ligne(fichier_lignes, numero_ligne, nouvelle_ligne)
                except ValueError:
                    pass # c'est moche mais ca marche
            else:
                nouvelle_ligne = input("Nouvelle ligne à insérer : ")
                fichier_lignes = gestionaire.inserer_ligne(fichier_lignes, 1, nouvelle_ligne)
            gestionaire.afficher_fichier(fichier_lignes)

        elif choix == 'u':
            if fichier_lignes != []:
                try:
                    numero_ligne = int(input("Numéro de la ligne à supprimer : "))
                    fichier_lignes = gestionaire.supprimer_ligne(fichier_lignes, numero_ligne)
                except ValueError:
                    pass # c'est moche mais ca marche
            gestionaire.afficher_fichier(fichier_lignes)

        elif choix == 'c':
            chaine = input("Entrez la chaîne à surligner : ")
            gestionaire.afficher_chercher_fichier(fichier_lignes, chaine)
        
        elif choix == 's':
            fichier = gestionaire.liste_vers_chaine(fichier_lignes)
            nom_future_fichier = definput("Entrez le nom du fichier a écrire", nom_fichier)
            if definput(f"Voulez-vous remplacer le contenu de {nom_future_fichier} avec le tampon (O/N)", "N").lower() == 'o':
                nom_fichier = nom_future_fichier
                disque.ecrire(fichier, nom_fichier, binaire=binaire)
            gestionaire.afficher_fichier(fichier_lignes)
        
        elif choix == 'q':
            effacer_terminal()
            sigma = False

        else:
            gestionaire.afficher_fichier(fichier_lignes)

if __name__ == "__main__":
    try:
        lancement()
    except Exception as e:
        print(f"\033[31mErreur: {e}\033[0m")