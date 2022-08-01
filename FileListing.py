from os import listdir
import pandas as pd
#
import streamlit as st
#
#Paso 0. Inicia Streamlit
#
PAGE_TITLE = "File listing"
st.set_page_config(
    page_title = "File listing",
    page_icon="🧊",
    #layout="wide",
    initial_sidebar_state="expanded",
)
#
#Paso 10. cosmeticos
#
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#
#Paso 1. Variables Iniciales
#
# función para buscar archivos
def BuscaArchivos(a):
    e=[]
    files= listdir(a)
    for c in range(len(files)):
        d = files[c].split('.')
        e.append(d[0])
    return e
# 
yyyy = [2019,2020,2021]
mmmm = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
#Paso 2 agregamos Filtros a utilizar
#
#st.sidebar.checkbox('yes')#st.sidebar.button('Click')#st.sidebar.radio('Pick your gender',['Male','Female'])
year = st.sidebar.selectbox( 'Choose the year', yyyy )
month = st.sidebar.selectbox( 'Choose the month', mmmm )
#st.sidebar.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])#st.sidebar.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])#st.sidebar.slider('Pick a number', 0,50)
#
#Paso 3  se define los numeros que corresponden a cada mes, es decir la mascara en el path que corresponde a cada mes
#
#MonthMask = ['01_Jan', '02_Feb', '03_Mar', '04_Apr', '05_May', '06_Jun', '07_Jul', '08_Aug', '09_Sep', '10_Oct', '11_Nov', '12_Dec']
MonthMask = ['02', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for m in range(len(MonthMask)):
    if month == mmmm[m]:
        MonthValue = MonthMask[m] #Es el enmascarado del path que corresponde al mes del filtro
#
#Paso 4 Generar lista de files en este directorio(folder)
dirOriginal='C:/working/xampp/htdocs/Lab/05202002/daniel/20220727/WorkPerformanceLoad/1_MONTHLY/1_Original/'+str(year)+'/'+str(year)+'-'+MonthValue+'/'#pasar al inicio del script
#
st.title ( PAGE_TITLE )
st.header( str(year) + ' / ' + str(month) )
#st.markdown("this is the header")#st.subheader("this is the subheader")#st.caption("this is the caption")#st.code("x=2021")#st.latex(r''' a+a r^1+a r^2+a r^3 ''')
#
#Paso 5. Definir los archivos pendientes
#
files={} # Archivos pendientes identificados
originalfiles = BuscaArchivos(dirOriginal)
for each in originalfiles:
    files[str(each)]=''
#print('-----')
#print (files)
#
#Paso 6. Generar lista de files en este directorio (folder)
#
dirCompleto='C:/working/xampp/htdocs/Lab/05202002/daniel/20220727/WorkPerformanceLoad/1_MONTHLY/3_Completed/'+str(year)+'/'+str(year)+'-'+MonthValue+'/'#pasar al inicio del script
completedfiles=BuscaArchivos(dirCompleto)
for completed in completedfiles:
    files[completed] = 'completed'
#print('-----')
#print(files)
#
#Paso 7. Tags 
#
root = 'C:/working/xampp/htdocs/Lab/05202002/daniel/20220727/WorkPerformanceLoad/1_MONTHLY/2_Assigned/'#pasar al inicio del script
types = [
    '_INCLUDED IN',
    '_MISSING SERIAL',
    '_NEED APPROVAL',
    '_OTRO PROBLEMA'
    ]#pasar al inicio del script
#
for tag in types:
    tagfiles = BuscaArchivos( root + tag)
    for q in files:
        if ( q in tagfiles ):
            files[q] = tag
#print('-----')
#print(files)
#
for Todo in files:
    if ( files[Todo] == '' ):
        files[Todo] = 'ToDo'
#print(files)
#
for z in files.copy():
    if ( files[z] == 'completed' ):
        del(files[z])
#
#Paso 8. Filtrar resultados
#
# definimos filtros
TagsFilter = st.sidebar.multiselect('choose a tag',types, default=types)
#st.sidebar.write('You selected:', ' / '.join(TagsFilter))
# los files encontrados y clasificados son contratados con el filtro
FilteredFiles={}
for i in files:
    if files[i] in TagsFilter:
        #print(files[i])#tag
        #print([i])#file
        FilteredFiles[i]=files[i]
#
#Paso 8. Files filtrados a pandas 
#
table = pd.DataFrame.from_dict(FilteredFiles, orient='index', columns=['tags'])
#print('-----')
#
#Paso 9. Pandas a streamlit 
#
st.dataframe(data=table, width=None, height=None)