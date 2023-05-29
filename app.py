#Importem la classe Flask dins de la llibreria flask
from flask import Flask, render_template, jsonify, request
from database import load_job_from_db, add_application_to_db
from database import obtenir_dades_actuals, obtenir_1_tipus_dada
from mqtt_proba import obtenir_valor_proba
from temps import hora_minuts_segons_int
from numero_a_actual import obtenir_nom_dada, arrodonir, obtenir_titol_dada

#Probes de grafica video: https://www.youtube.com/watch?v=e68S9x3Rh_0
from time import time
from random import random
import json

app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Definem la pagina d'inici (sense ruta extra)

#Web pro per fer grafics en javascript: https://mdbootstrap.com/docs/b4/jquery/javascript/charts/
#Obtenir directament dels sockets: https://www.donskytech.com/python-flask-websockets/?utm_content=cmp-true

#HTMLX imortar del github: https://github.com/app-generator/sample-flask-htmlx

#Dash y flas: https://www.youtube.com/watch?v=fakRnkw0s9o


#Ruta + parametro ("Id","actConsigna","actCurrent""actPower","actSpeed","actTemperatura",
#"actTorque","eix_habilitat")
@app.route("/grafico/<parametro>")
def grafico2(parametro):
  return render_template('grafico3.html', parametre=parametro)


@app.route("/grafico/<parametro>/<parametro2>")
def grafico3(parametro, parametro2):
  array = obtenir_1_tipus_dada(5, parametro2)
  titol = obtenir_titol_dada(parametro2)
  print("hola")
  return render_template('grafico4.html', array=array, titol=titol)


@app.route("/api/grafico")
def grafico():
  #Funcion de obtener dadas de grafica
  #dades = nombre de funcion()
  return render_template('grafico2.html')


@app.route("/sign-in")
def formulari_signin():
  return render_template('sign-in.html')


@app.route("/register")
def formulari_registre():
  return render_template('register.html')


@app.route("/proba/andres")
def chart():
  return render_template('chart.html')


@app.route("/proba/data", methods=["GET", "POST"])
def andres_data():
  data = [time() * 1000, random() * 100]
  response = make_response(json.dumps(data))
  response.content_type = 'application/json'
  return response


@app.route("/")
def hellow_world():
  return render_template('home.html', company_name="Monitoreig remot d'un variador de freqüència")


@app.route("/dataloggator")
def dades_del_motor():
  return render_template('dataloggator.html')

  #for key, value in my_dict.items(): print(key,value)


@app.route("/dataloggator/actuals/<numero>")
def dada_actual_torque(numero):
  nom_dada = obtenir_nom_dada(numero)
  array = obtenir_dades_actuals(1)
  for row in array:
    dades = row
  valor = arrodonir(dades[nom_dada], numero)
  return render_template('dada_actual.html', dada=valor)


@app.route("/proba/temps")
def obtenir_hora_actual():
  temps = hora_minuts_segons_int()
  string = "temps"
  dict = {string: temps}
  return dict


@app.route("/proba/actuals")
def ultim_registre_motor():
  array = obtenir_dades_actuals(5)
  for element in array:
    dades = element
  if not dades:
    return "Not Found", 404
  return jsonify(array)


#-------------------------------------------------------


@app.route("/api/array_dict/<numero>/<parametro>")  #tambien  url
def ultim_registre_moto(numero, parametro):
  array = obtenir_1_tipus_dada(numero, parametro)  # esta es   python
  if not array:
    return "Not Found", 404
  return jsonify(array)


#--------------------------------------------------------


@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["post"])
def apply_to_job(id):
  # Obtenim dades recollides a la url:
  #data = request.args

  #Recollir dades del mètode:
  data = request.form
  job = load_job_from_db(id)
  # store this in the DB
  # send  an email
  # display an acknowledgement
  #return jsonify(data)

  add_application_to_db(id, data)

  return render_template('application_submitted.html', job=job, data=data)


@app.route('/api/job/<id>/')
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route('/api/proba')
def valor_de_proba():
  valor = obtenir_valor_proba()
  return render_template('proba.html', valor=valor)


@app.route('/user_proba/<username>')
def profile(username):
  return f'{username}\'okey'


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
