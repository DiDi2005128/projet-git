# projet-git

Projet Python basé sur une API FastAPI qui expose des fonctionnalités de calcul mathématique, de traitement de texte et de conversion unitaire.

Langage principal : Python

## Description

Ce projet contient une petite API REST permettant de :

- vérifier si un texte est un palindrome ;
- compter les voyelles dans un texte ;
- inverser une chaîne de caractères ;
- calculer la factorielle d'un nombre ;
- tester si un nombre est premier ;
- calculer le PGCD de deux nombres ;
- convertir des températures, distances et montants entre devises.

Le projet est structuré en modules Python séparés et comprend des tests unitaires avec pytest.

---

## Structure du projet

```bash
projet-git/
├── app/
│   ├── __init__.py
│   ├── conversion.py
│   ├── erreurs.py
│   ├── main.py
│   ├── math.py
│   └── texte.py
├── tests/
│   ├── test_conversion.py
│   ├── test_math.py
│   └── test_texte.py
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

---

## Fonctionnalités

### Textes
- `est_palindrome(texte)`
- `compter_voyelles(texte)`
- `inverser(texte)`

### Mathématiques
- `factorielle(n)`
- `est_premier(n)`
- `pgcd(n, m)`

### Conversion
- `celsius_fahrenheit(celsius)`
- `km_miles(km)`
- `euros_devise(montant, devise)`

Les taux de conversion disponibles sont :
- USD : 1.08
- GBP : 0.85
- JPY : 165.20

---

## API REST

L'application expose ces routes FastAPI :

### Accueil
- `GET /`

### Texte
- `GET /texte/palindrome?texte=radar`
- `GET /texte/voyelles?texte=Bonjour`
- `GET /texte/inverser?texte=bonjour`

### Conversion
- `GET /conversion/celsius-fahrenheit?celsius=20`
- `GET /conversion/km-miles?km=10`
- `GET /conversion/euros-devise?montant=100&devise=USD`

### Mathématiques
- `GET /math/factorielle?n=5`
- `GET /math/premier?n=7`

> Le calcul de PGCD est implémenté dans le module `app.math` mais n'est pas exposé comme route HTTP dans `app/main.py` pour l'instant.

---

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine.

Installez ensuite les dépendances :

```bash
pip install fastapi uvicorn pytest
```

Si vous utilisez un environnement virtuel, il est aussi conseillé d'installer les dépendances depuis le fichier `requirements.txt` après l'avoir complété selon vos besoins.

---

## Lancer l'application

Depuis la racine du projet :

```bash
uvicorn app.main:app --reload
```

Ensuite, ouvrez votre navigateur à :

```bash
http://127.0.0.1:8000
```

La documentation Swagger est également accessible ici :

```bash
http://127.0.0.1:8000/docs
```

---

## Exemples d'utilisation

### Vérifier un palindrome

```bash
curl "http://127.0.0.1:8000/texte/palindrome?texte=radar"
```

Réponse :

```json
{
  "texte": "radar",
  "est_palindrome": true
}
```

### Compter les voyelles

```bash
curl "http://127.0.0.1:8000/texte/voyelles?texte=Bonjour"
```

Réponse :

```json
{
  "texte": "Bonjour",
  "nombre_voyelles": 3
}
```

### Inverser un texte

```bash
curl "http://127.0.0.1:8000/texte/inverser?texte=bonjour"
```

Réponse :

```json
{
  "texte_original": "bonjour",
  "texte_inverse": "ruojnob"
}
```

### Convertir des Celsius en Fahrenheit

```bash
curl "http://127.0.0.1:8000/conversion/celsius-fahrenheit?celsius=20"
```

Réponse :

```json
{
  "celsius": 20,
  "fahrenheit": 68.0
}
```

### Convertir des kilomètres en miles

```bash
curl "http://127.0.0.1:8000/conversion/km-miles?km=10"
```

Réponse :

```json
{
  "km": 10,
  "miles": 6.21
}
```

### Convertir des euros vers une devise

```bash
curl "http://127.0.0.1:8000/conversion/euros-devise?montant=100&devise=USD"
```

Réponse :

```json
{
  "montant": 100,
  "devise": "USD",
  "resultat": 108.0
}
```

### Calculer une factorielle

```bash
curl "http://127.0.0.1:8000/math/factorielle?n=5"
```

Réponse :

```json
{
  "nombre": 5,
  "factorielle": 120
}
```

### Tester si un nombre est premier

```bash
curl "http://127.0.0.1:8000/math/premier?n=7"
```

Réponse :

```json
{
  "nombre": 7,
  "est_premier": true
}
```

---

## Tests

Le projet contient des tests unitaires pour vérifier le bon fonctionnement des fonctions.

Pour exécuter les tests :

```bash
pytest
```

Les tests couvrent :

- factorielle de nombres normaux et limites ;
- nombres premiers et cas négatifs ;
- chaînes de caractères vides et valides ;
- calculs sur les voyelles et inversion de texte ;
- conversion Celsius/Fahrenheit, km/miles et euro vers devise ;
- PGCD sur plusieurs cas.

---

## Remarques

- Le fichier `requirements.txt` est actuellement vide ou incomplet dans son état actuel.
- Pour un usage réel, il est recommandé de l'ajouter avec les dépendances nécessaires :

```txt
fastapi
uvicorn
pytest
```

---

## Licence

Ce projet est fourni à titre éducatif et peut être adapté selon vos besoins.
