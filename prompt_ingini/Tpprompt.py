def format_product_code(product_id):
    """
    Formate un identifiant produit de 10 caractères alphanumériques.

    Cette fonction insère un tiret après le 3e et le 7e caractère, retournant
    une chaîne au format 'XXX-XXXX-XXX'.

    Paramètres :
    -----------
    product_id : str
        Une chaîne de 10 caractères alphanumériques.

    Retour :
    -------
    str
        L'identifiant formaté avec des tirets.

    Lève :
    -----
    ValueError : si l'identifiant n'a pas 10 caractères ou contient des caractères non alphanumériques.

    Exemples :
    ---------
    >>> format_product_code("A1B2C3D4E5")
    'A1B-2C3D-4E5'

    >>> format_product_code("1234567890")
    '123-4567-890'
    """
    # Vérifie la longueur et le contenu alphanumérique
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    # Insertion des tirets : après les 3e et 7e caractères
    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
    

# Exemples d'utilisation
if __name__ == "__main__":
    try:
        print(format_product_code("A1B2C3D4E5"))  # A1B-2C3D-4E5
        print(format_product_code("1234567890"))  # 123-4567-890
        print(format_product_code("INVALID!"))    # Erreur
    except ValueError as e:
        print(f"Erreur : {e}")






def format_product_code(product_id):
    """
    Formate un identifiant produit alphanumérique de 10 caractères.

    Cette fonction insère des tirets après le 3e et le 6e caractère, 
    retournant une chaîne au format 'XXX-XXX-XXXX'.

    Paramètre :
    ----------
    product_id : str
        Une chaîne alphanumérique de 10 caractères.

    Retour :
    -------
    str
        L'identifiant formaté, par exemple 'ABC-123-DEF4'.

    Lève :
    -----
    ValueError : si la chaîne n’a pas exactement 10 caractères ou contient des caractères non alphanumériques.

    Exemple :
    --------
    >>> format_product_code("ABC123DEF4")
    'ABC-123-DEF4'
    """
    # Vérification de la validité de la chaîne
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    # Formatage selon le modèle 'XXX-XXX-XXXX'
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


# Exemple d'utilisation
if __name__ == "__main__":
    try:
        print(format_product_code("ABC123DEF4"))  # Résultat : 'ABC-123-DEF4'
    except ValueError as e:
        print(f"Erreur : {e}")





def format_product_code(product_id):
    """
    Formate un identifiant produit alphanumérique de 10 caractères.

    Cette fonction insère des tirets après le 3e et le 6e caractère, 
    retournant une chaîne au format 'XXX-XXX-XXXX'.

    Paramètre :
    ----------
    product_id : str
        Une chaîne alphanumérique de 10 caractères.

    Retour :
    -------
    str
        L'identifiant formaté, par exemple 'ABC-123-DEF4'.

    Lève :
    -----
    ValueError : si la chaîne n’a pas exactement 10 caractères ou contient des caractères non alphanumériques.

    Exemples :
    ---------
    >>> format_product_code("ABC123DEF4")
    'ABC-123-DEF4'

    >>> format_product_code("XYZ987GHIJ")
    'XYZ-987-GHIJ'

    >>> format_product_code("SHORT")
    ValueError: Le product_id doit être une chaîne de 10 caractères alphanumériques.
    """
    # Vérification de la validité de la chaîne
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne de 10 caractères alphanumériques.")

    # Formatage : insertion de tirets après le 3e et le 6e caractère
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


# Exemples d'utilisation
if __name__ == "__main__":
    try:
        print(format_product_code("ABC123DEF4"))  # 'ABC-123-DEF4'
        print(format_product_code("XYZ987GHIJ"))  # 'XYZ-987-GHIJ'
        print(format_product_code("SHORT"))       # Lève ValueError
    except ValueError as e:
        print(f"Erreur : {e}")
