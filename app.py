#Importem la classe Flask dins de la llibreria flask
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Definem la pagina d'inici (sense ruta extra) 
@app.route("/")
def hellow_world():
  return render_template('home.html')

#Intentem afegir icona favicon.ico pero no va
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path,'static'), 'image/pepsi.ico', mimetype = 'image/vnd.microsoft.icon')

  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)