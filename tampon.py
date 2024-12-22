from tools import effacer_terminal

def afficher_fichier(lignes:list):
    """
    Affiche le contenu du fichier avec les numéros des lignes.
    
    :param lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    """
    effacer_terminal()
    for index, ligne in enumerate(lignes, start=1):
        print(f"{index}: {ligne}")

def afficher_chercher_fichier(fichier_lignes:list, chaine:str):
    """
    Affiche le contenu du fichier avec les numéros des lignes et surligne la chaîne spécifiée.
    
    :param fichier_lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    :param chaine: La chaîne à surligner dans chaque ligne.
    """
    effacer_terminal()
    for index, ligne in enumerate(fichier_lignes, start=1):
        if chaine in ligne:
            debut = ligne.find(chaine)
            fin = debut + len(chaine)
            # Afficher la ligne avec la chaîne surlignée
            ligne_surlignee = (
                ligne[:debut] + 
                '\033[47m' + ligne[debut:fin] + '\033[0m' + 
                ligne[fin:]
            )
            print(f"{index}: {ligne_surlignee}")
        else:
            print(f"{index}: {ligne}")

def modifier_ligne(fichier_lignes:list, numero_ligne:int, nouvelle_ligne:str):
    """
    Modifie la ligne à un numéro donné dans la liste des lignes.
    
    :param fichier_lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    :param numero_ligne: Le numéro de la ligne à modifier (commence à 1).
    :param nouvelle_ligne: La nouvelle ligne qui remplacera l'ancienne.
    
    :return: Liste mise à jour avec la ligne modifiée.
    """
    if 1 <= numero_ligne <= len(fichier_lignes):
        fichier_lignes[numero_ligne - 1] = nouvelle_ligne
        return fichier_lignes
    else:
        print("Numéro de ligne invalide.")
        return fichier_lignes

def inserer_ligne(fichier_lignes:list, numero_ligne:int, nouvelle_ligne:str):
    """
    Insère une nouvelle ligne juste avant la ligne spécifiée.
    
    :param fichier_lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    :param numero_ligne: Le numéro de la ligne avant laquelle insérer la nouvelle ligne (commence à 1).
    :param nouvelle_ligne: La nouvelle ligne à insérer.
    
    :return: Liste mise à jour avec la ligne insérée.
    """
    if 1 <= numero_ligne <= len(fichier_lignes) + 1:
        fichier_lignes.insert(numero_ligne - 1, nouvelle_ligne)
        return fichier_lignes
    else:
        print("Numéro de ligne invalide.")
        return fichier_lignes

def supprimer_ligne(fichier_lignes, numero_ligne):
    """
    Supprime la ligne spécifiée dans la liste des lignes.
    
    :param fichier_lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    :param numero_ligne: Le numéro de la ligne à supprimer (commence à 1).
    
    :return: Liste mise à jour avec la ligne supprimée.
    """
    if 1 <= numero_ligne <= len(fichier_lignes):
        # Supprimer la ligne correspondant au numéro spécifié
        fichier_lignes.pop(numero_ligne - 1)
        return fichier_lignes
    else:
        print("Numéro de ligne invalide.")
        return fichier_lignes

def liste_vers_chaine(fichier_lignes:list):
    """
    Transforme une liste de lignes en une seule chaîne de caractères avec des retours à la ligne.
    
    :param fichier_lignes: Liste de chaînes de caractères représentant les lignes du fichier.
    
    :return: Une seule chaîne avec des retours à la ligne entre chaque ligne.
    """
    return "\n".join(fichier_lignes)

def chaine_vers_liste(chaine:str):
    """
    Transforme une chaîne de caractères avec des retours à la ligne en une liste de lignes.
    
    :param chaine: La chaîne de caractères avec des retours à la ligne.
    
    :return: Liste de chaînes de caractères, chaque chaîne représentant une ligne.
    """
    return chaine.splitlines()

