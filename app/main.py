from fastapi import FastAPI, HTTPException
from app.texte import est_palindrome, compter_voyelles, inverser
from app.math import factorielle, est_premier

app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "API fonctionnelle"}


@app.get("/texte/palindrome") 
def palindrome(texte: str = ""): 
    if texte == "": 
        raise HTTPException( 
            status_code=400, 
            detail="Le texte ne peut pas être vide" )
    return {
        "texte": texte,
        "est_palindrome": est_palindrome(texte)
    }

@app.get("/texte/voyelles") 
def voyelles(texte: str = ""): 
    if texte == "": 
        raise HTTPException( 
            status_code=400, detail="Le texte ne peut pas être vide" )
    return {
        "texte": texte,
        "nombre_voyelles": compter_voyelles(texte)
    }

@app.get("/texte/inverser") 
def inverser_texte(texte: str = ""): 
    if texte == "": 
        raise HTTPException( status_code=400, detail="Le texte ne peut pas être vide" )
    return {
        "texte_original": texte,
        "texte_inverse": inverser(texte)
    }

@app.get("/math/factorielle")
def factorielle_endpoint(n: int = 0):
    if n < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif")
    return {
        "nombre": n,
        "factorielle": factorielle(n)
    }

@app.get("/math/premier")
def premier(n: int = 0):
    if n < 0:
        raise HTTPException(status_code=400, detail="Le nombre doit être positif")
    return {
        "nombre": n,
        "est_premier": est_premier(n)
    }
