def est_palindrome(texte):
    return texte == texte[::-1]

def compter_voyelles(texte): 
    voyelles = "aeiouy" 
    compteur = 0
    for lettre in texte.lower():
        if lettre in voyelles:
            compteur += 1

    return compteur
