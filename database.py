import os
from sqlalchemy import create_engine, text

#Link de conexió de sqlAlchemy a DB núbol: https://docs.sqlalchemy.org/en/20/dialects/mysql.html
#Codi copiat:
#engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

#Nota:
#Hem hagut d'instalar pymysql usant la comanda: pip install pymysql

db_connection_string = os.environ['DB_CONNECTION_STRING']

#Habilitem SSL usant el certificat ca obtingut de planet scale a new connection ->
# -> tipo de conexion -> python -> main.py
engine = create_engine(db_connection_string)

#Consulta la sintaxi a https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#basics-of-statement-execution


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result:
      jobs.append({
        "title": row.nom,
        "id": row.id,
        "requirements": row.requeriments,
        "response": row.response,
        "location": row.localitzacio,
        "salary": row.salari,
        "currency": row.currency
      })
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    row = conn.execute(text("select * from jobs where id = " + str(id)))
    for row in row:
      if row.nom:
        job = {
          "title": row.nom,
          "id": row.id,
          "requirements": row.requeriments,
          "response": row.response,
          "location": row.localitzacio,
          "salary": row.salari,
          "currency": row.currency
        }
  return job


def obtenir_dades_actuals(linies):
  with engine.connect() as conn:
    rows = conn.execute(
      text("SELECT * FROM actuals ORDER BY id DESC LIMIT " + str(linies)))
    array = []
    for row in rows:
      actuals = {
        "Id": row.Id,
        "actTorque": row.actTorque,
        "actPower": row.actPower,
        "actCurrent": row.actCurrent,
        "actSpeed": row.actSpeed,
        #Dia i hora donen error. Format de tornada és:
        #'dia':dastetime.date(2023,3,9), 'hora': dateime.timedelta(seconds=54631),
        #"dia": row.dia,
        #"hora": row.hora,
        "eix_habilitat": row.eix_habilitat,
        "actConsigna": row.actConsigna,
        "actTemperatura": row.actTemperatura
      }
      array.append(actuals)
  return array


def obtenir_1_tipus_dada(linies, atributo):
  array_dict = obtenir_dades_actuals(linies)
  array_float = []
  for dict in array_dict:
    array_float.append(dict[atributo])

    #array_float
  array_retorn = []
  for i in range(len(array_float)):
    i += 1
    array_retorn.append(array_float[-i])
  return array_float  # array = [1,2,3,4,5] (tan largo como "linies")


# Us de la documentació:
# https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
def add_application_to_db(job_id, data):
  with engine.connect() as conn:

    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(
      query, {
        "job": job_id,
        "full_name": data['full_name'],
        "email": data['email'],
        "linkedin_url": data['linkedin_url'],
        "education": data['education'],
        "work_experience": data['work_experience'],
        "resume_url": data['resume_url']
      })
