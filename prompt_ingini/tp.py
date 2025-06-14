


def calculer(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Erreur : division par zéro"
    else:
        return "Erreur : opération non supportée"

# Exemple d'utilisation :
print(calculer(10, 5, '+'))  # Affiche 15
print(calculer(10, 5, '/'))  # Affiche 2.0
print(calculer(10, 0, '/'))  # Affiche une erreur





def calculate(a, b, op):
    """
    Effectue une opération arithmétique entre deux entiers.

    Paramètres :
    a (int) : Le premier entier.
    b (int) : Le second entier.
    op (str) : L'opération à effectuer. Doit être l'une des chaînes suivantes : '+', '-', '*', '/'.

    Retourne :
    float ou int : Le résultat de l'opération, arrondi à deux décimales dans le cas d'une division.
    str : Un message d'erreur si l'opération est invalide ou en cas de division par zéro.

    Exemples :
    >>> calculate(10, 5, '+')
    15
    >>> calculate(10, 5, '/')
    2.0
    >>> calculate(10, 0, '/')
    'Erreur : division par zéro'
    >>> calculate(10, 5, '^')
    'Erreur : opération invalide'
    """
    # Vérification de l'opération demandée
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Erreur : division par zéro"
        else:
            return round(a / b, 2)  # Arrondi à deux décimales
    else:
        return "Erreur : opération invalide"

# Exemples d'utilisation :
print(calculate(10, 5, '+'))  # 15
print(calculate(10, 0, '/'))  # Erreur : division par zéro
print(calculate(7, 3, '/'))   # 2.33
print(calculate(8, 2, '^'))   # Erreur : opération invalide





def calculate(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Paramètres :
    ----------
    a : int
        Le premier entier.
    b : int
        Le deuxième entier.
    op : str
        L'opération à effectuer : '+', '-', '*', ou '/'.

    Retour :
    -------
    float | int
        Le résultat de l'opération, arrondi à deux décimales pour la division.
    
    Lève :
    -----
    ValueError : si l'opérateur est invalide.
    ZeroDivisionError : en cas de division par zéro.

    Exemples :
    ---------
    >>> calculate(10, 5, '+')
    15
    >>> calculate(7, 3, '/')
    2.33
    >>> calculate(8, 0, '/')
    ZeroDivisionError: Division par zéro non autorisée.
    >>> calculate(4, 2, '%')
    ValueError: Opérateur invalide : %
    """
    # Vérifie que les paramètres sont bien des entiers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Les paramètres 'a' et 'b' doivent être des entiers.")

    # Effectue l'opération en fonction de l'opérateur
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return round(a / b, 2)
    else:
        raise ValueError(f"Opérateur invalide : {op}")

# Exemples d'utilisation
if __name__ == "__main__":
    try:
        print(calculate(10, 5, '+'))   # 15
        print(calculate(7, 3, '/'))    # 2.33
        print(calculate(8, 0, '/'))    # Déclenche une exception
    except Exception as e:
        print(f"Erreur : {e}")
