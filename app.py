from flask import Flask, render_template, url_for, request, redirect, flash
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clés_flash'
DSN = 'Driver={SQL Server};Server=DESKTOP-2B6AD73\\SQLEXPRESS;Database=gestiondemagasin;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
# uid = <username>;
# pwd = <password>;

#INSERER LES ENTREES DE L'AJOUT DE MAGASIN DANS FORM.HTML
@app.route("/form", methods=["GET","POST"])
def form():
    
   if request.method == 'POST':
      nom_magasin = request.form["nom_magasin"]
      adresse = request.form["adresse"]
      tel = request.form["tel"]
      email = request.form["email"]

      DSN = 'Driver={SQL Server};Server=DESKTOP-2B6AD73\\SQLEXPRESS;Database=gestiondemagasin;'
      conn = pyodbc.connect(DSN)
      cursor = conn.cursor()
      cursor.execute('''
            INSERT INTO Magasin (NomMagasin, Adresse, Tel, Email)
            VALUES (?, ?, ?, ?)
          ''', (nom_magasin, adresse, tel, email))

      conn.commit()
      conn.close()
      flash("Votre Magasin a été enregistré avec succès !", 'info')
      return redirect(url_for('magasin'))
   data = ''
   return render_template("form.html", data=data)

#RECUPERER et AFFICHER LES DONNEES SAISIES SUR LISTE MAGASIN ET DANS LA BD
@app.route("/magasin", methods=['GET','POST'])
def magasin():
      DSN = 'Driver={SQL Server};Server=DESKTOP-2B6AD73\\SQLEXPRESS;Database=gestiondemagasin;'
      conn = pyodbc.connect(DSN)
      cursor.execute("select * from Magasin")
      data = cursor.fetchall()
      conn.close()
      return render_template("magasin.html", data=data)


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
#@app.route("/Magasin")

#def magasin():
   #return render_template("magasin.html")

# quatrieme page
#@app.route("/form")
#def form():
 # return render_template("form.html")

# cinquime page
#@app.route("/cool")
#def cool():
   #return render_template("enr_magasin.html")


# modifier page
#@app.route("/modifier")
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item_id = int(item_id)

    # Connexion à la base de données
    conn = pyodbc.connect(DSN)

    # Création d'un objet curseur
    cursor = conn.cursor()

    # Récupération des données du magasin depuis la base de données
    cursor.execute('SELECT * FROM Magasin WHERE MagasinID = ?', (item_id,))
    data = cursor.fetchone()

    # Si la méthode de la requête est POST, mise à jour des données du produit dans la base de données
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom_magasin = request.form["nom_magasin"]
        adresse = request.form["adresse"]
        tel = request.form["tel"]
        email = request.form["email"]

        # Mise à jour des données du Magasin dans la base de données
        cursor.execute('''
            UPDATE Magasin
            SET NomMagasin = ?, Adresse = ?, Tel = ?, Email = ?
            WHERE MagasinID = ?
        ''', (nom_magasin, adresse, tel, email, item_id))

        # Validation des modifications dans la base de données
        conn.commit()

        # Fermeture de la connexion à la base de données
        conn.close()

        # Affichage d'un message de succès à l'utilisateur
        flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')

        # Redirection de l'utilisateur vers la page du Magasin
        return redirect(url_for('magasin'))

    # Retour du modèle de formulaire du Magasin
    return render_template('form.html', data=data)



@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item_id = int(item_id)

    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Magasin WHERE MagasinID = ?', (item_id,))

    conn.commit()
    conn.close()

    flash(f'Le magasin numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('magasin'))

#@app.route("/Modification")

#def enrModifier():
   #return render_template("enrModif.html")

# supprimer page

@app.route("/supprimer/<int:item_id>", methods=['GET', 'POST'])
def supprimer(item_id):
    item_id = int(item_id)

    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Magasin WHERE MagasinID = ?', (item_id,))
    
    data = cursor.fetchone()
    conn.commit()
    conn.close()
    return render_template("supprimer.html", data=data)


#@app.route("/suppression")
#def enrSupprimer():
   #return render_template("enrSup.html")



if __name__ == "__main__":
    app.run(debug=True)