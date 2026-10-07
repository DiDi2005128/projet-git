from fastapi import FastAPI
from app.texte import est_palindrome, compter_voyelles, inverser

app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "API fonctionnelle"}


@app.get("/texte/palindrome")
def palindrome(texte: str):
    return {
        "texte": texte,
        "est_palindrome": est_palindrome(texte)
    }

@app.get("/texte/voyelles")
def voyelles(texte: str):
    return {
        "texte": texte,
        "nombre_voyelles": compter_voyelles(texte)
    }

@app.get("/texte/inverser")
def inverser_texte(texte: str):
    return {
        "texte_original": texte,
        "texte_inverse": inverser(texte)
    }