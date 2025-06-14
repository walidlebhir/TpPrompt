
####TP : Ingénierie de prompt appliquée à la génération de code avec l’IA 




Exercices 2.1 : 

Prompt1 : "Écris une fonction pour faire des opérations entre deux nombres en Python." 
code : 

def calculer(a, b, operation):
    """
    Effectue une opération entre deux nombres.
    
    :param a: premier nombre
    :param b: deuxième nombre
    :param operation: une chaîne parmi '+', '-', '*', '/'
    :return: le résultat de l'opération
    """
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
        return "Opération non reconnue"


Prompt 2 : "Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une 
chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer 
les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux 
décimales. Ajoute un docstring détaillé et des commentaires. "   --> Prompt Spécifique :

code : 

def calculate(a, b, op):
    """
    Effectue une opération mathématique entre deux entiers.

    Paramètres :
    a (int) : le premier entier
    b (int) : le deuxième entier
    op (str) : une chaîne représentant l'opération à effectuer : 
               '+' pour addition, '-' pour soustraction, 
               '*' pour multiplication, '/' pour division

    Retourne :
    float ou int : le résultat de l'opération si valide
    str : un message d'erreur si l'opération est invalide ou en cas de division par zéro

    Exemple :
    >>> calculate(10, 5, '+')
    15
    >>> calculate(10, 0, '/')
    'Erreur : division par zéro'
    >>> calculate(10, 5, '/')
    2.0
    """
    
    # Vérifie l'opération et effectue le calcul
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
            return round(a / b, 2)
    else:
        return "Erreur : opération invalide"



ptompt 3 : "En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers 
et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être 
robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les 
divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des 
commentaires clairs " --> Prompt avec Persona 


def calculate(a, b, op):
    """
    Effectue une opération mathématique de base entre deux entiers.

    Paramètres
    ----------
    a : int
        Le premier entier.
    b : int
        Le second entier.
    op : str
        L'opération à effectuer. Doit être l'un des caractères suivants :
        '+', '-', '*', '/'.

    Retours
    -------
    float ou int
        Le résultat de l'opération. Si l'opération est une division, le
        résultat est arrondi à deux décimales.
    str
        Un message d'erreur si l'opération est invalide ou en cas de
        division par zéro.

    Exemples
    --------
    >>> calculate(10, 5, '+')
    15
    >>> calculate(7, 2, '/')
    3.5
    >>> calculate(4, 0, '/')
    'Erreur : division par zéro'
    >>> calculate(3, 3, '%')
    'Erreur : opérateur invalide'
    """

    # Vérifie si les paramètres sont bien des entiers
    if not isinstance(a, int) or not isinstance(b, int):
        return "Erreur : les deux paramètres doivent être des entiers"

    # Exécute l'opération selon l'opérateur donné
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Erreur : division par zéro"
        return round(a / b, 2)
    else:
        return "Erreur : opérateur invalide"



Exercices2.2 : 


prompt1 :   "Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le 
7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non 
alphanumériques, elle doit lever une ValueError. Inclue un docstring." ---> Prompt basé sur la Règle (zéro-Shot Prompting)


code : (python ) 

def format_product_code(product_id):
   
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("L'identifiant doit contenir exactement 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"


prompt2 : "Crée une fonction Python format_product_code(product_id). Le product_id doit être une 
chaîne de 10 caractères alphanumériques. Voici un exemple d'entrée-sortie:
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit 
lever une ValueError si l'entrée est invalide. Inclue un docstring." --> Prompt avec un Exemple (One-Shot Prompting) 

code : 
def format_product_code(product_id):
    
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("L'identifiant doit contenir exactement 10 caractères alphanumériques.")

    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


prompt 3 : on utilisant la prompt precedant et en ajout des autre exemple :
format_product_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ", incluant un cas 
d'erreur : format_product_code("SHORT") devrait lever une ValueError


code : 
def format_product_code(product_id):
    
    if len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("L'identifiant doit contenir exactement 10 caractères alphanumériques.")

    # Formatage avec des tirets : 3 premiers, 3 suivants, puis le reste
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"

exercices 2.3 :  (void les fichies html css )et document word 



Partie 3 : Débogage et Amélioration du Code  : 



Exercices 3.2 : 

code corege par l'outils d'integence generatif ai : 

def calculate_average(numbers_list):
    
    total = 0
    count = 0

    for num in numbers_list:
        if isinstance(num, (int, float)):
            total += num
            count += 1

    if count == 0:
        raise ValueError("Aucun nombre valide dans la liste.")

    return total / count


# Exemple d'utilisation
my_nums = [1, 2, 'three', 4]
try:
    avg = calculate_average(my_nums)
    print(f"Moyenne : {avg}")
except ValueError as e:
    print(f"Erreur : {e}")



3- teste unitaire : 

import pytest
from typing import List

# Supposons que c'est ta fonction corrigée :
def calculate_average(numbers_list: List[float]) -> float:
    """
    Calcule la moyenne des nombres numériques dans une liste.
    Ignore les éléments non numériques.
    Renvoie 0 si aucun nombre valide n'est présent.
    """
    total = 0
    count = 0
    for num in numbers_list:
        if isinstance(num, (int, float)):
            total += num
            count += 1
    if count == 0:
        return 0
    return total / count

# ------------------------
#         TESTS
# ------------------------

def test_average_all_integers():
    assert calculate_average([2, 4, 6]) == 4.0

def test_average_with_floats():
    assert calculate_average([1.5, 2.5, 3.0]) == pytest.approx(2.333, 0.001)

def test_average_with_non_numeric():
    assert calculate_average([1, 'two', 3]) == 2.0

def test_average_empty_list():
    assert calculate_average([]) == 0

def test_average_only_strings():
    assert calculate_average(['a', 'b', 'c']) == 0

def test_average_with_none():
    assert calculate_average([1, None, 2]) == 1.5

def test_average_mixed_types():
    assert calculate_average([1, '2', 3.5, True, [4], 0]) == pytest.approx((1 + 3.5 + 1 + 0)/4, 0.001)


Exercices 3.2 : Refactoring avec l’IA



1- le type de trie utiliser est trie par selection par une maniere naif d'ordre croissant . 
2- Prompt utiliser "pour se code de trie fait une reformulation bien structure et utiliser des commantaire pour bien expliquer les inscrution du code " 
code regenerer par generative ai : 
# Déclaration de la liste non triée
a = [5, 3, 8, 6, 7, 2]

# Parcourir chaque élément de la liste
for i in range(len(a)):
    # Comparer l'élément courant avec tous les éléments suivants
    for j in range(i + 1, len(a)):
        # Si l'élément à l'indice i est plus grand que celui à j, on échange
        if a[i] > a[j]:
            # Échange des éléments pour les mettre dans le bon ordre
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

# Afficher la liste triée
print("Liste triée :", a)


3-Prompt avec les contraintes : "Crée un programme Python qui trie une liste d'entiers en ordre croissant. Le code doit respecter les contraintes suivantes :

Respecter les conventions PEP8 (indentation, espaces, noms de variables explicites, etc.),

Ajouter un docstring au niveau du module, ainsi qu’à chaque fonction pour expliquer clairement leur rôle,

Le code doit être modulaire : chaque partie du traitement (lecture, tri, affichage) doit être placée dans une fonction séparée,

Les noms des variables et fonctions doivent être clairs, explicites et en anglais,

Ajouter un bloc if __name__ == "__main__": pour encapsuler l'exécution principale du script. "


code python pour le trie : 





"""
Module to sort a list of integers in ascending order using a simple sorting algorithm.
The code is modular, well-documented, and follows PEP8 style guidelines.
"""

def get_numbers():
    """
    Returns a predefined list of integers to sort.
    In a real-world scenario, this could be replaced with user input or file input.
    
    Returns:
        list: A list of integers.
    """
    return [5, 3, 8, 6, 7, 2]


def sort_numbers_ascending(numbers):
    """
    Sorts a list of integers in ascending order using a simple bubble sort algorithm.
    
    Args:
        numbers (list): The list of integers to sort.
    
    Returns:
        list: A new list sorted in ascending order.
    """
    sorted_list = numbers.copy()
    length = len(sorted_list)

    for i in range(length):
        for j in range(i + 1, length):
            if sorted_list[i] > sorted_list[j]:
                # Swap values
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    
    return sorted_list


def display_sorted_numbers(sorted_numbers):
    """
    Prints the sorted list of integers.
    
    Args:
        sorted_numbers (list): The sorted list of integers to display.
    """
    print("Sorted numbers in ascending order:", sorted_numbers)


if __name__ == "__main__":
    """
    Main entry point of the program.
    """
    numbers = get_numbers()
    sorted_numbers = sort_numbers_ascending(numbers)
    display_sorted_numbers(sorted_numbers)





Exercices 3.3 : 


1) voila le prompt que j'ais donnes au generative ai pour realiser la tache : 

" Générez un docstring complet et conforme aux standards (type NumPy ou Google) pour la fonction get_user_permissions(user_id, system_context). Le docstring doit expliquer le rôle de la fonction, décrire les paramètres, la valeur de retour, et inclure un exemple d'utilisation." 


code : 

def get_user_permissions(user_id, system_context):
    """
    Retrieve the list of permissions assigned to a user based on their role in the system.

    Args:
        user_id (str or int): The unique identifier of the user.
        system_context (dict): A dictionary containing user roles and their associated user IDs.
            Expected keys include 'admins' and 'editors', each mapping to a list of user IDs.

    Returns:
        list of str: A list of permission strings granted to the user.
            Possible permissions include 'read', 'write', 'delete', and 'admin'.

    Example:
        >>> context = {
        ...     'admins': ['user1', 'user2'],
        ...     'editors': ['user3', 'user4']
        ... }
        >>> get_user_permissions('user1', context)
        ['read', 'write', 'delete', 'admin']
        >>> get_user_permissions('user4', context)
        ['read', 'write']
        >>> get_user_permissions('user5', context)
        ['read']
    """
    if user_id in system_context.get('admins', []):
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context.get('editors', []):
        return ['read', 'write']
    else:
        return ['read']



2) 

Prompt : "Génère une section Markdown intitulée "Usage of get_user_permissions function" pour un fichier README.md. Cette section doit expliquer clairement comment utiliser la fonction get_user_permissions(user_id, system_context), décrire le format attendu du paramètre system_context, et fournir plusieurs exemples d'appels avec leurs résultats attendus. Sois clair et concis." 


code : 

## Usage of `get_user_permissions` function

The `get_user_permissions` function is used to retrieve the list of permissions assigned to a user based on their role within the system.

### Prerequisites

- The function requires a `user_id` which can be a string or integer uniquely identifying a user.
- The `system_context` parameter must be a dictionary that includes at least the following keys:
  - `admins`: a list of user IDs with administrator privileges.
  - `editors`: a list of user IDs with editor privileges.

Example format of `system_context`:

```python
system_context = {
    'admins': ['user1', 'user2'],
    'editors': ['user3', 'user4']
}




