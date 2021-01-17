from flask import Flask, render_template,request,redirect,url_for 
from bson import ObjectId 
from pymongo import MongoClient 
import os  



app = Flask(__name__)
client = MongoClient("mongodb+srv://christelle:1234@cluster0.hwb6z.mongodb.net/?retryWrites=true&w=majority")
db=client.don_bosco_db.don_bosco_db

db = client.get_database('don_bosco_db')
collections= db.don_bosco_db
#cette fonction redirige la connexion vers la premiere page et les pages qui suivent .
def redirect_url():
    return request.args.get('next') or request.referrer or url_for('index')




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def formulaire():
    return render_template('formulaire.html')
    
@app.route("/sauvegarder", methods=['POST'])    
def action ():      
    nom=request.values.get("nom")    
    prenom=request.values.get("prenom")    
    email=request.values.get("email")    
    adresse=request.values.get("adresse_postale")   
    promise=request.values.get("promise")    
    conditions=request.values.get("conditions")   
    collections.insert_one({ "nom":nom, "prenom":prenom, "email":email, "adresse":adresse, "promise":promise,"conditions":conditions})    
    return redirect("/liste")

@app.route("/liste")    
def lists ():       
    dons_l= collections.find()       
    return render_template('liste.html',dons=dons_l)






 #PARTIE A METTRE EN BAS DE LA PAGE POUR LANCER L APPLI PAS AU MILIEU DU CODE SINON CA REND LE CODE NUL
if __name__ == '__main__':
    app.run(debug=True)