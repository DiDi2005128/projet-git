def est_palindrome(texte):
    return texte == texte[::-1]

print(est_palindrome("radar"))
print(est_palindrome("bonjour"))

def compter_voyelles(texte): 
    voyelles = "aeiouy" 
    compteur = 0
    for lettre in texte.lower():
        if lettre in voyelles:
            compteur += 1

    return compteur

print(compter_voyelles("Bonjour"))
print(compter_voyelles("Python"))