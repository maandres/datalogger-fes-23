def obtenir_nom_dada(numero):
  variables = ["actTorque",       #0
               "actPower",        #1
               "actCurrent",      #2
               "actSpeed",        #3
               "eix_habilitat",   #4
               "actConsigna",     #5
               "actTemperatura"]  #6
  return variables[int(numero)]

def arrodonir(valor_in, numero):
  if numero == "0":
    valor = round(valor_in ,2)
  elif numero == "1":
    valor = round(valor_in ,2)
  elif numero == "2":
    valor = round(valor_in ,3)
  elif numero == "3":
    valor = round(valor_in)
  elif numero == "5":
    valor = round(valor_in)
  elif numero == "6":
    valor = round(valor_in ,1)
  else:
    valor = valor_in
  return valor
  

  
  