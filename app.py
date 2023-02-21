#Importem la classe Flask dins de la llibreria flask
from flask import Flask

app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Definem la pagina d'inici (sense ruta extra)
@app.route("/")
def hellow_world():
  return "Hello, world"

print()
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)