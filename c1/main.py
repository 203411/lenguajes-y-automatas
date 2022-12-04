import ast
import pylightxl as xl
import random
from PyQt5 import QtWidgets, uic
import sys

class main:
   
   D = ""
   testing_macs = ""
   list_resultados = []

   def read_file_xlsx(self,filename):
      data = []
      try:
         db = xl.readxl(fn=filename)
         for row in db.ws(ws='bd').rows:
            data.append([row[0], row[1], row[2], row[3], row[4]])
         return data   
      except Exception as e:
         print(f"El archivo '{filename}' no existe.") 
      
   def read_file_txt(self,filename):
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

   def step_dfa(self,D,q,a):
      try:
         assert(a in D["Sigma"])
         assert(q in D["Q"])
         return D["Delta"][(q,a)]
      except Exception as e:
         return False

   def run_dfa(self,D,w):
      curstate = D["q0"]
      if w == "":
         return curstate
      else:
         return self.run_dfa_h(D,w[1:], self.step_dfa(D,curstate,w[0]))

   def run_dfa_h(self,D,w,q):
      if w == "":
         return q
      else:
         return self.run_dfa_h(D,w[1:], self.step_dfa(D,q,w[0]))

   def accepts_dfa(self,D,w):
      return self.run_dfa(D,w) in D["F"]

   def search(self,mac, database):
      for i in range(0,len(database)):
         if str(mac) == str(database[i][3]):
            return (f"Encontrado -> Matricula: {database[i][0]} Nombre: {database[i][1]} Consumo: {database[i][4]}")
      return "MAC no encontrada en la base de datos"
      
   
   def open_txt_file(self):
      filename = QtWidgets.QFileDialog.getOpenFileName(None, "Abrir archivo", "", "Text files (*.txt)")
      self.D = self.read_file_txt(filename[0])
   
      
   def open_txt_test(self):
      filename = QtWidgets.QFileDialog.getOpenFileName(None, "Abrir archivo", "", "Text files (*.txt)")
      self.testing_macs = self.read_file_txt(filename[0])
      # print(testing_macs)
   
   def imprimir(self):
      print(self.list_resultados)


   def evaluate(self,interfaz):
      database = self.read_file_xlsx("archivo.xlsx")
      # print(database)
      for mac in self.testing_macs:
         if self.accepts_dfa(self.D, mac):
            consumo = self.search(mac, database)
            # print(f"MAC: {mac} -> Aceptada -> {consumo}")
            self.list_resultados.append(f"MAC: {mac} -> Aceptada -> {consumo}")
         else:
            # print(f"MAC: {mac} -> Rechazada")
            self.list_resultados.append(f"MAC: {mac} -> Rechazada")
      # self.imprimir()      
      interfaz.list_result.addItems(self.list_resultados)

      
      
if __name__ == "__main__":   
   app = QtWidgets.QApplication(sys.argv)
   interfaz = uic.loadUi("interfaz.ui")
   interfaz.show()
   main = main()
   
   interfaz.select_automata.clicked.connect(main.open_txt_file)
   
   interfaz.select_test.clicked.connect(main.open_txt_test)
   
   interfaz.evaluate_test.clicked.connect(lambda: main.evaluate(interfaz))
  
   
   
   
   sys.exit(app.exec_())
   
   
   

   
   