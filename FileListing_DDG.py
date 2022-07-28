import os
import random
import shutil
'''
Este archivo es un dummy data generator para los ejercicios de FileListing
de cliente anonimo
'''
#
# Declaraciones
mercado = '1_MONTHLY' # a eliminar realizando markets
originales = '1_Original'
asignados = '2_Assigned'
terminados = '3_Completed'
origen = 'C:/working/xampp/htdocs/Lab/05202002/daniel/20220727/WorkPerformanceLoad'
types = [
    '_NEED APPROVAL',
    '_MISSING SERIAL',
    '_INCLUDED IN',
    '_OTRO PROBLEMA',
    'borrar'    # <-----
                # aqui coloco los archivos a descubrir en FileListing
                # para ser etiquetados como ToDo
    ]
'''
# a desarrollar
markets = [
    '1_MONTHLY',
    '2_TEST',
    '3_VLT',
    '4_EMEA',
    '5_LATAM'
]
'''
# 
# se calculan rutas
original_dir = origen+'/'+mercado+'/'+originales+'/'
types_dir = origen+'/'+mercado+'/'+asignados+'/'
completed_dir = origen+'/'+mercado+'/'+terminados+'/'
# se crean folders
path3 = os.path.join(types_dir)
os.makedirs(path3)

for a in range(2019,2022):
    yearPath = os.path.join(original_dir + str( a )+'/')
    os.makedirs(yearPath)
    yearPath2 = os.path.join(completed_dir + str( a )+'/')
    os.makedirs(yearPath2)
    for b in range(1,13):
        if len( str(b) ) == 1 :
            b = '0'+ str( b )
        else:
            b = str( b )
        path = os.path.join(yearPath, str( a ) + "-" + b + "/")
        os.makedirs(path)
        path2 = os.path.join(yearPath2, str( a ) + "-" + b + "/")
        os.makedirs(path2)
        # se crean archivos originales
        Noriginales = random.randint(10, 15)
        # se determinan los archivos terminados
        Nterminados = int( Noriginales * 0.6 )
        #
        uniqueFile = str( a ) + "-" + b + "-" + str(random.randint(1, 30))
        for c in range(Noriginales):
            filename = path + uniqueFile + 'archivo' + str( c ) + '.txt'
            filename2 = path2 + uniqueFile + 'archivo' + str( c ) + '.txt'
            filename3 = path3 + uniqueFile + 'archivo' + str( c ) + '.txt'
            open( filename, 'w' )
            if c < ( Nterminados - 1 ):
                shutil.copyfile(filename, filename2)
            else:
                shutil.copyfile(filename, filename3)
# Falto clasificar por año trabajo manual =(
#
from os import listdir
# iterar los archivos 2_Assigned y meterlos en una carpeta

for t in types:
    os.makedirs(types_dir+t)

#Paso 0. Definir la función para buscar archivos
def BuscaArchivos(a):
    f=[]
    files = listdir(a)
    for c in range(len(files)):
        d = files[c]
        e = d.split('.')
        if e[-1] == 'txt': f.append(d)
    return f
    
xAcomodar = BuscaArchivos(types_dir)

for f in xAcomodar:
    f2 = types_dir + f
    carpeta = random.randint(0,len(types)-1)
    shutil.move( types_dir+f, types_dir+types[carpeta]+'/'+f)