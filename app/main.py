from fastapi import FastAPI
from app.texte import est_palindrome

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