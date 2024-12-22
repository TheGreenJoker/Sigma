#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools import texte_vers_binaire, binaire_en_chaine, definput

def existe_fichier(nom:str):
    """
    Vérifie si un fichier existe.
    :param nom: nom du fichier
    :return: => 1 si le fichier existe sinon 0
    """
    try:
        with open(nom):
            return 1
    except FileNotFoundError:
        return 0

def lire(chemin:str, binaire=0):
    """
    Retourne le contenu d'un fichier.

    :param chemin: chemin vers le fichier
    :param binaire: lire en binaire ou en texte (0=t/1=b)
    :return: contenu du fichier
    """
    if existe_fichier(chemin):
        if binaire:
            fichier = open(chemin, 'rb')
            contenu = binaire_en_chaine(fichier.read())
        else:
            try:
                fichier = open(chemin, 'r')
                contenu = str(fichier.read())
            except UnicodeDecodeError:
                print("\033[31mFormat de fichier incorrect\033[0m\nEssayez de l'ouvrir en format binaire")
                exit(1)

        fichier.close()
        return contenu
    if definput("Le fichier spécifié n'existe pas, voulez-vous le creer (O/N)", "O").lower() == 'o':
        ecrire('', chemin)
        return ''
    else:
        exit()

            
def ecrire(contenu:str, chemin:str, binaire=0):
    """
    Ecris le contenu d'un fichier.
    :param contenu: contenu du fichier
    :param chemin: chemin vers le fichier
    :param binaire: lire en binaire ou en texte (0=binaire/1=texte)
    """
    if binaire:
        with open(chemin, 'wb') as fichier:
            fichier.write(texte_vers_binaire(contenu))
    else:
        with open(chemin, 'w') as fichier:
            fichier.write(contenu)