from flask import Flask, render_template, url_for
# from flask_sqlalchemy import 
app = Flask(__name__)

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

# supprimer page
@app.route("/supprimer")

def supprimer():
   return render_template("supprimer.html")

@app.route("/suppression")
def enrSupprimer():
   return render_template("enrSup.html")



if __name__ == "__main__":
    app.run(debug=True)