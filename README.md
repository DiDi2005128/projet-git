# projet-git

Projet Python basé sur une API FastAPI qui expose des fonctionnalités de calcul mathématique et de traitement de texte.

Langage principal : Python

## Description

Ce projet contient une petite API REST permettant de :

- vérifier si un texte est un palindrome ;
- compter les voyelles dans un texte ;
- inverser une chaîne de caractères ;
- calculer la factorielle d'un nombre ;
- tester si un nombre est premier ;
- calculer le PGCD de deux nombres.

Le projet est structuré en modules Python séparés et inclut des tests unitaires avec pytest.

---

## Structure du projet

```bash
projet-git/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── math.py
│   ├── texte.py
│   └── erreurs.py
├── tests/
│   ├── test_math.py
│   └── test_texte.py
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

---

## Fonctionnalités

### Mathématiques
- `factorielle(n)`
- `est_premier(n)`
- `pgcd(n, m)`

### Texte
- `est_palindrome(texte)`
- `compter_voyelles(texte)`
- `inverser(texte)`

### API REST
L'application expose des routes FastAPI :

- `GET /`
- `GET /texte/palindrome`
- `GET /texte/voyelles`
- `GET /texte/inverser`
- `GET /math/factorielle`
- `GET /math/premier`

---

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine.

Installez ensuite les dépendances :

```bash
pip install fastapi uvicorn pytest
```

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

---

## Exemple de résultats attendus

Les tests couvrent notamment :

- factorielle de nombres normaux et limites ;
- nombres premiers et cas négatifs ;
- chaînes de caractères vides et valides ;
- calculs sur les voyelles et inversion de texte ;
- PGCD sur plusieurs cas.

---

## Remarques

- Le fichier `requirements.txt` est vide ou incomplet dans son état actuel.
- Pour un usage réel, il est recommandé d'y ajouter les dépendances nécessaires, par exemple :
  ```txt
  fastapi
  uvicorn
  pytest
  ```

---

## Licence

Ce projet est fourni à titre éducatif et peut être adapté selon vos besoins.
