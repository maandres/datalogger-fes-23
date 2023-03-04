#Importem la classe Flask dins de la llibreria flask
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Creem una llista d'elements simulnt base de dades
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location':'Bengaluru,Intia',
    'salary': 'Rs. 10000000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location':'Delhi,Intia',
    'salary': 'Rs. 1520000'
  },
  {
    'id': 3,
    'title': 'Zapaterp',
    'location':'Monodpat,Intia',
    'salary': 'Rs. 20000'
  },
  {
    'id': 4,
    'title': 'Heladoer',
    'location':'Putas,Intia',
    'salary': 'Rs. 1000000'
  }
]


#Definem la pagina d'inici (sense ruta extra) 
@app.route("/")
def hellow_world():
  return render_template('home.html', jobs=JOBS)

#Intentem afegir icona favicon.ico pero no va
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path,'static'), 'image/pepsi.ico', mimetype = 'image/vnd.microsoft.icon')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)