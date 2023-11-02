#from flask import Flask, render_template, url_for
#import pyodbc

# from flask_sqlalchemy import 
#app = Flask(__name__)


#configuration de la bd
#app.config['SQL_SERVER_CONNECTION_STRING'] = r"""
 #  Driver={SQL server};
 #  server=DESKTOP-DLHA7UR\SQLEXPRESS;
 #  Database=vision;
 #  Trusted_Connection=yes;"""
# fichie base
#@app.route("/base")

#def base():
#return render_template("base.html")

#@app.route("/")

#def Login():
 #  return render_template("index.html")
# deuxieme page
#@app.route("/Menu")

#def home():
 #  return render_template("menu.html")

# troisieme page
#@app.route("/Magasin")

#def magasin():
#   return render_template("magasin.html")

# quatrieme page
#@app.route("/formulaire")

#def form():
 #  return render_template("form.html")

# cinquime page
#@app.route("/succès")

#def succès():
#   return render_template("enr_magasin.html")


# modifier page
#@app.route("/modifier")
#def modifier():
 #  return render_template("modifier.html")

#@app.route("/Modification")
#def enrModifier():
 #  return render_template("enrModif.html")

# supprimer page magasin
#@app.route("/supprimer")
#def supprimer():
#   return render_template("supprimer.html")

#@app.route("/suppression")
#def enrSupprimer():
#   return render_template("enrSup.html")


#PARTIE DU PRODUIT

#aller à la page produit
#@app.route("/Produit")
#def produit():
#   return render_template("produit/produit.html")

#aller à la page du formulaire du produit
#@app.route("/Formulaire Produit")
#def formProd():
#   return render_template("produit/formProd.html")

#aller à la page enregistrement produit après avoir cliquer sur valider
#@app.route("/Produit enregistré")
#def enrprod():
#   return render_template("produit/enr_produit.html")

#aller à la page modification produit après avoir cliquer sur modifier
#@app.route("/Modifier Produit")
#def Modifprod():
#   return render_template("produit/Modifprod.html")

#aller à la page modification produit succés après avoir cliquer sur validé
#@app.route("/Produit modifié")
#def prodModifié():
#   return render_template("produit/prodModifié.html")

#aller à la page suppression produit après avoir cliquer sur suppimer
#@app.route("/Suppression Produit")
#def Supprod():
#   return render_template("produit/supprod.html")

#aller à la page suppression du produit succés après avoir cliquer sur validé
#@app.route("/Produit supprimé")
#def prodsupprimé():#
  # return render_template("produit/prodsupprimé.html")


#PARTIE DU stock

#aller à la page stock
#@app.route("/Stock")
#def stock():#
   #return render_template("stock/stock.html")


#PARTIE DE VENTE

#aller à la page vente
#@app.route("/Vente")
#def vente():#
   #return render_template("vente/vente.html")



#if __name__ == "__main__":
  #  app.run(debug=True)