def factorielle (n: int) -> int:
    if n < 0:
        raise ValueError("Le nombre doit être positif")
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat