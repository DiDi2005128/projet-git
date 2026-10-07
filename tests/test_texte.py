def est_palindrome(texte):
    return texte == texte[::-1]

print(est_palindrome("radar"))
print(est_palindrome("bonjour"))