from fnmatch import filter
from os import listdir
import pandas as pd
from bs4 import BeautifulSoup
#Paso 0. Definir la función para buscar archivos
def BuscaArchivos(a,b):
    e=[]
    files= (filter(listdir(a), b))
    for c in range(len(files)):
        d = files[c].split('.')
        e.append(d[0])
    return e
# 
filtro='*'
#Paso 1. Generar lista de files en este directorio(folder)
dirOriginal='C:/working/xampp/htdocs/Lab/05202002/daniel/original/'#pasar al inicio del script
files={} # Archivos pendientes identificados
originalfiles = BuscaArchivos(dirOriginal, filtro)
for each in originalfiles:
    files[str(each)]=''
print('-----')
print (files)
#
#Paso 2. Generar lista de files en este directorio (folder)
#
dirCompleto='C:/working/xampp/htdocs/Lab/05202002/daniel/completo/'#pasar al inicio del script
completedfiles=BuscaArchivos(dirCompleto,filtro)
for completed in completedfiles:
    files[completed] = 'completed'
print('-----')
print(files)
#Paso 3. Tags #pasar al inicio del script
root = 'C:/working/xampp/htdocs/Lab/05202002/daniel/DolordeCabeza/'#pasar al inicio del script
types = [
    '_dañado',
    '_pateo_la_bolita',
    '_problema1',
    '_problema2'
    ]#pasar al inicio del script
#
for tag in types:
    tagfiles = BuscaArchivos( root + tag,filtro)
    for q in files:
        if ( q in tagfiles ):
            files[q] = tag
print('-----')
print(files)
#
for Todo in files:
    if ( files[Todo] == '' ):
        files[Todo] = 'ToDo'
print(files)
#
for z in files.copy():
    if ( files[z] == 'completed' ):
        del(files[z])
print(files)
#
table = pd.DataFrame.from_dict(files, orient='index', columns=['tags'])
print('-----')
print(table)
table = table.to_html()

#
title = "Reporte X"#pasar al inicio del script
top = open('render.html','r')
footer=open('footer.html','r')
html = str(BeautifulSoup(top,'lxml')) + '<h1>'+title+'</h1>' + table + str(BeautifulSoup(footer,'lxml'))
report = open('report.html','w')
report.writelines(html) 
report.close()
