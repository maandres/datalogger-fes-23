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
engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

#Consulta la sintaxi a https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#basics-of-statement-execution

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result:
      jobs.append({"title": row.nom,
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
    row = conn.execute(
      text("select * from jobs where id = " + str(id)))
    for row in row:
      if row.nom:
        job = {"title": row.nom,
                "id": row.id,
                "requirements": row.requeriments,
                "response": row.response,
                "location": row.localitzacio,
                "salary": row.salari,
                "currency": row.currency
                }
  return job