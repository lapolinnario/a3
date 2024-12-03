import os
from os.path import join

a =0 

lookfor = "script-aula-teste.bat"
for root, dirs, files in os.walk('C:\\'):
    #print ("searching"), root
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        a = 1 
lookfor = "script-aula.bat"
for root, dirs, files in os.walk('C:\\'):
    #print ("searching"), root
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        a=1
lookfor = "execucao-aula.exe"
for root, dirs, files in os.walk('C:\\'):
    #print ("searching"), root
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        a=1
lookfor = "execucao-aula-teste.exe"
for root, dirs, files in os.walk('C:\\'):
    #print ("searching"), root
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        a=1
    
print (a)
if (a == 1): 
    exit(1)
else:
    exit(0)
