from flask import Flask, request, jsonify 
from .texte import est_palindrome
app = Flask(__name__)
@app.route("/texte/palindrome", methods=["GET"]) 
def palindrome(): 
    texte = request.args.get("texte")
    if texte is None:
        return jsonify({"erreur": "Le paramètre texte est obligatoire"}), 400

    return jsonify({
        "texte": texte,
        "est_palindrome": est_palindrome(texte)
    })
