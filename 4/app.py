from flask import Flask, render_template, redirect, request, url_for
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired

app= Flask(__name__)

mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"]= "localhost"
app.config["MYSQL_DATABASE_USER"]= "root"
app.config["MYSQL_DATABASE_PASSWORD"]= ""
app.config["MYSQL_DATABASE_DB"]= "warung_makan" #isi bro nama tabel
mysql.init_app(app)

app.config['SECRET_KEY'] = 'thisissecret' #kalo pake wtforms
class add_categories(FlaskForm):
    id = IntegerField('id')
    name = StringField('name', validators = [InputRequired()])

class add_makanan(FlaskForm):
   id = StringField('id')
   makanan = StringField('Name', validators = [InputRequired()])
   kategori = StringField('Kategori', validators = [InputRequired()])
   stok = StringField('Stok')
   gambar = StringField('Gambar', validators = [InputRequired()])
   deskripsi = TextAreaField('Deskripsi', render_kw={'class': 'form-control', 'rows':'5'})

#route
@app.route('/')
def index():
   form= add_makanan()
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM categories ORDER BY id")
   data_kategori = cursor.fetchall()
   cursor.execute("SELECT * FROM foods")
   data_foods = cursor.fetchall()
   datalist_kategori = []
   datalist_foods = []
   if data_kategori and data_foods is not None :
      for item in data_kategori:
         container= {
               'id': item[0],
               'name':item[1]
            }
         datalist_kategori.append(container)
      for item2 in data_foods:
         container2 = {
            'id' :item2[0],
            'name':item2[1],
            'stok':item2[2],
            'image':item2[3],
            'deskripsi':item2[4],
            'category_id':item2[5],
         }
         datalist_foods.append(container2)
         
      return render_template('index.html', datalist_kategori = datalist_kategori, datalist_foods= datalist_foods, form=form)
   return render_template('index.html')


@app.route('/add2', methods =['POST'])
def tambah_makanan():
   form = add_makanan()
   nama = request.form['makanan']
   kategori = request.form['kategori']
   stok = request.form['stok']
   deskripsi = request.form['deskripsi']
   
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute("INSERT IGNORE INTO categories(name) VALUES(%s)", (kategori))
   cursor.execute("INSERT INTO foods(name, stok,deskripsi) VALUES(%s,%s,%s)", (nama,stok,deskripsi))
   cursor.execute("UPDATE foods SET category_id = (SELECT id FROM categories WHERE name =(%s)) WHERE category_id is NULL", kategori)
   conn.commit()
   conn.close()
   return redirect(url_for('index'))

@app.route('/beli/<int:id_makanan>', methods= ["GET"])
def beli(id_makanan):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE foods SET stok = stok-1 WHERE id =(%s)", id_makanan)
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__== "__main__":
    app.run(debug=True)
