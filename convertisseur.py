from flask import Flask, request, jsonify, render_template
import requests




app = Flask(__name__)
@app.route('/')
def accueil():
    return 'Bienvenue sur le convertisseur de devises. Utilisez /convertir avec les paramètres appropriés.'

def obtenir_taux_de_change(devise_source, devise_cible):
    url = f"https://api.exchangerate-api.com/v4/latest/{devise_source}"
    reponse = requests.get(url)
    donnees = reponse.json()
    taux = donnees['rates'][devise_cible]
    return taux

@app.route('/convertir', methods=['GET'])
def convertir():
    if 'montant' in request.args and 'devise_source' in request.args and 'devise_cible' in request.args:
        montant = request.args.get('montant', type=float)
        devise_source = request.args.get('devise_source', type=str)
        devise_cible = request.args.get('devise_cible', type=str)
        taux = obtenir_taux_de_change(devise_source, devise_cible)
        montant_converti = montant * taux
        return jsonify({"montant_converti": montant_converti})
    else:
        # Afficher le formulaire si aucun paramètre n'est fourni
        return render_template('convertir.html')

if __name__ == '__main__':
    app.run(debug=True)



