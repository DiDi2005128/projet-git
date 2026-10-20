from fastapi import FastAPI, HTTPException
from app.texte import est_palindrome, compter_voyelles, inverser
from app.conversion import celsius_fahrenheit, km_miles, euros_devise
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
@app.get("/conversion/celsius-fahrenheit")
def convertir_celsius(celsius: float):
    try:
        resultat = celsius_fahrenheit(celsius)
        return {"celsius": celsius, "fahrenheit": resultat}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/conversion/km-miles")
def convertir_km(km: float):
    try:
        resultat = km_miles(km)
        return {"km": km, "miles": resultat}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/conversion/euros-devise")
def convertir_euros(montant: float, devise: str):
    try:
        resultat = euros_devise(montant, devise)
        return {"montant": montant, "devise": devise, "resultat": resultat}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))