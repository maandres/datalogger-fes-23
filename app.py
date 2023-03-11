#Importem la classe Flask dins de la llibreria flask
from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from mqtt_proba import obtenir_valor_proba
from temps import hora_minuts_segons_str, hora_minuts_segons_int

app = Flask(__name__)

#L'arroba representa el "domain name"
#El que ve després és el path (exemple:/inicio)

#Definem la pagina d'inici (sense ruta extra) 
@app.route("/")
def hellow_world():
  return render_template('home.html', company_name="Dataloggator")

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  
  return jsonify(jobs)

@app.route("/proba/temps")
def obtenir_hora_actual():
  temps = hora_minuts_segons_int()
  dict = {"temps": temps}
  return dict

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

@app.route("/api/grafico")
def grafico():
  return render_template('grafico.html')

@app.route('/user_proba/<username>')
def profile(username):
    return f'{username}\'okey'
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
