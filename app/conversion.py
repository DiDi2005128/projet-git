def celsius_fahrenheit(celsius):
    if celsius < -273.15:
        raise ValueError("Température en dessous du zéro absolu")
    return round((celsius * 9 / 5) + 32, 2)


def km_miles(km):
    if km < 0:
        raise ValueError("La distance ne peut pas être négative")
    return round(km * 0.621371, 2)


taux = {
    "USD": 1.08,
    "GBP": 0.85,
    "JPY": 165.20
}

def euros_devise(montant, devise):
    if montant < 0:
        raise ValueError("Le montant ne peut pas être négatif")
    if devise not in taux:
        raise ValueError("Devise inconnue")
    return round(montant * taux[devise], 2)
