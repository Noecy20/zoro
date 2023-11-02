from flask import Flask, render_template, url_for, request, redirect, flash 
import pyodbc

#configuration de la bd
conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-DLHA7UR\SQLEXPRESS;DATABASE=Zorobd;')

cursor = conn.cursor()
#cursor.execute("select * from produit")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clés_flash'

# fichie base
@app.route("/base")
def base():
   return render_template("base.html")

@app.route("/")
def Login():
   return render_template("index.html")

# deuxieme page
@app.route("/Menu")
def home():
   return render_template("menu.html")

# troisieme page
@app.route("/Magasin")
def magasin():
   return render_template("magasin.html")

# quatrieme page
@app.route("/formulaire")
def form():
   return render_template("form.html")

# cinquime page
@app.route("/succès")
def succès():
   return render_template("enr_magasin.html")

# modifier page
@app.route("/modifier")
def modifier():
   return render_template("modifier.html")

@app.route("/Modification")
def enrModifier():
   return render_template("enrModif.html")

# supprimer page magasin
@app.route("/supprimer")
def supprimer():
   return render_template("supprimer.html")

@app.route("/suppression")
def enrSupprimer():
   return render_template("enrSup.html")


#PARTIE DU PRODUIT
#aller à la page produit
@app.route("/Produit")
def produit():
   cursor = conn.cursor()
   s = "SELECT * FROM Produit"
   cursor.execute(s)#pour exécuter la requete
   listProd = cursor.fetchall()
   return render_template("produit/produit.html", listProd = listProd)

#aller à la page du formulaire du produit
@app.route("/Formulaire Produit",methods=['POST','GET'])
def formProd():
   if request.method=='POST':
      nomProd = request.form['nomProd']
      categorie = request.form['categorie']
      prix = request.form['prix']
      quantite = request.form['quantite']
      cursor = conn.cursor()
      cursor.execute("INSERT INTO Produit (nomProd, categorie, prix, quantite) VALUES (?,?,?,?)", (nomProd, categorie, prix, quantite))
      conn.commit()
      flash('Produit Ajouté !', 'success')
      return redirect(url_for("produit"))
   return render_template("produit/formProd.html")

#aller à la page modification produit après avoir cliquer sur modifier
@app.route("/Modifier Produit/<string:id_produit>",methods=['POST','GET'])
def Modifprod(id_produit):
   if request.method=='POST':
      nomProd = request.form['nomProd']
      categorie = request.form['categorie']
      prix = request.form['prix']
      quantite = request.form['quantite']
      cursor = conn.cursor()
      cursor.execute("UPDATE Produit set nomProd=?,categorie=?,prix=?,quantite=? where id_produit=?", (nomProd, categorie, prix, quantite, id_produit))
      conn.commit()
      flash('Produit Modifié !', 'success')
      return redirect(url_for("produit"))
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM Produit where id_produit=?",(id_produit,))
   data=cursor.fetchone()
   return render_template("produit/Modifprod.html",datas=data)

#aller à la page suppression produit après avoir cliquer sur suppimer
@app.route("/Suppression Produit/<string:id_produit>",methods=['GET'])
def Supprod(id_produit):
   cursor = conn.cursor()
   cursor.execute("DELETE FROM Produit where id_produit=?", (id_produit))
   conn.commit()
   flash('Produit Supprimé !', 'warning')
   return redirect(url_for("produit"))

#PARTIE DU stock

#aller à la page stock
@app.route("/Stock")
def stock():
   return render_template("stock/stock.html")


#PARTIE DE VENTE

#aller à la page vente
@app.route("/Vente")
def vente():
   return render_template("vente/vente.html")



if __name__ == "__main__":
   
    app.run(debug=True)