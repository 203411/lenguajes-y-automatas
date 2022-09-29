import ast
import pylightxl as xl
import random

def read_file_xlsx(filename):
   data = []
   try:
      db = xl.readxl(fn=filename)
      for row in db.ws(ws='bd').rows:
         data.append([row[0], row[1], row[2], row[3], row[4]])
      return data   
   except Exception as e:
      print(f"El archivo '{filename}' no existe.") 
   
def read_file_txt(filename):
   try:
      with open(filename, 'r', encoding='utf-8') as file:
         if "test" in filename:
            content = file.read().split('\n')
            return content
         else:
            content = file.read()
      DFA = ast.literal_eval(content)
      return DFA
   except Exception as e:
      print(f"El archivo '{filename}' no existe.") 

def step_dfa(D,q,a):
   try:
      assert(a in D["Sigma"])
      assert(q in D["Q"])
      return D["Delta"][(q,a)]
   except:
      return False

def run_dfa(D,w):
   curstate = D["q0"]
   if w == "":
      return curstate
   else:
      return run_dfa_h(D,w[1:], step_dfa(D,curstate,w[0]))

def run_dfa_h(D,w,q):
   if w == "":
      return q
   else:
      return run_dfa_h(D,w[1:], step_dfa(D,q,w[0]))

def accepts_dfa(D,w):
   return run_dfa(D,w) in D["F"]

def search(mac, database):
   for i in range(0,len(database)):
      if str(mac) == str(database[i][3]):
         return (f"Encontrado -> Matricula: {database[i][0]} Nombre: {database[i][1]} Consumo: {database[i][4]}")
   return "MAC no encontrada en la base de datos"
   
if __name__ == "__main__":   
   D = read_file_txt('automata.txt') 
   testing_macs = read_file_txt('test.txt') 
   database = read_file_xlsx('archivo.xlsx')
   i = 1
   # print(database)
   for mac in testing_macs:
      if accepts_dfa(D,mac):
         consumo = search(mac, database)
         print(f"ACEPTADO {i}  ({mac}) {consumo}")
      else:
         print(f"RECHAZADO {i} ({mac})")
      i+=1
   
   
   