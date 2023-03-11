import paho.mqtt.client as mqtt

def conectat(client,userdata,flags,rc):
  if rc == 0:
    print("Client conectat OK")
    client.subscribe("demo")
  else: 
    print("Client no s'ha pogut conectar")

def receptor(client,userdata,missatge):
  valor = missatge.payload
  return valor

def obtenir_valor_proba():
  #Creem l'objecte
  client = mqtt.Client("raspberry")
  client.connect("54.172.36.38",1883)
  
  client.on_connect = conectat
  client.on_message = receptor
  
  #client.loop_forever()
  client.loop(timeout=10.0, max_packets=1)
  
  #data = "hola_funciono"
  #data = [10,3]
  
  #client.publish("demo", bytearray(data))
  
  print("Fi de programa")