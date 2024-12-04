import os
from os.path import join

a =0 
lista = ["script-aula-teste.bat","script-aula.bat","execucao-aula.exe","execucao-aula-teste.exe"]

for root, dirs, files in os.walk('C:\\'):
    for lookfor in lista:
        if lookfor in files:
            print ("found: %s" % join(root, lookfor))
            a = 1 

    

exit(a)

