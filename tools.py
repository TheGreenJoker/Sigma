#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system # Effacer le terminal
import platform       # Portabilitée du programe


def effacer_terminal():
    """
    Efface le contenu du terminal en fonction du système d'exploitation.
    Utilise `clear` pour Linux/macOS et `cls` pour les rabats joie.
    """
    systeme = platform.system().lower()
    if systeme == 'linux' or systeme == 'darwin':
        system('clear')
    elif systeme == 'windows':
        system('cls')
    else:
        print("Système non pris en charge pour l'effacement du terminal.")

def texte_vers_binaire(texte: str):
    """
    Convertit une chaîne de caractères binaire (composée uniquement de '0' et '1') en un objet de type `bytes`.
    
    :param texte: Une chaîne de caractères contenant uniquement des '0' et '1', représentant un nombre binaire.
    :return: Un objet `bytes` représentant la valeur binaire de la chaîne.
    :raises ValueError: Si la chaîne contient des caractères autres que '0' ou '1'.
    """
    texte = texte.replace("\n", "")
    for char in texte:
        if (char != '0') and (char != '1'):
            raise ValueError("\033[31mLa chaine de caractère doit être constituée uniquement de 0 et de 1\033[0m")
    
    return int(texte, 2).to_bytes((len(texte) + 7) // 8, byteorder="big")

def binaire_en_chaine(bin_data):
    """
    Convertit une séquence d'octets en une chaîne binaire.

    :param bin_data: Séquence d'octets (type `bytes` ou `bytearray`) à convertir en chaîne binaire.
    :return: Une chaîne de caractères composée des bits des octets en représentation binaire.
    """
    try:
        return ''.join(format(byte, '08b') for byte in bin_data)
    except TypeError:
        effacer_terminal()
        print("\033[31mFormat de fichier incorrect\033[0m")
        exit(1)

def definput(phrase:str, defaut:str):
    """
    Demande une entrée utilisateur avec une valeur par défaut.
    
    :param phrase: La question ou le texte affiché à l'utilisateur pour demander une entrée.
    :param defaut: La valeur par défaut à retourner si l'utilisateur ne saisit rien.
    
    :return: La réponse de l'utilisateur ou la valeur par défaut si l'utilisateur ne répond rien.
    """
    reponse = input(f"{phrase} [{defaut}]: ")
    return defaut if reponse == '' else reponse
