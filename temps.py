from datetime import datetime

def hora_minuts_segons_str():
  time_now = datetime.now()
  current_time = time_now.strftime("%S")
  return current_time

def hora_minuts_segons_int():
  time_now = datetime.now()
  current_time = time_now.strftime("%S")
  current_time_int = int(current_time)
  return current_time_int