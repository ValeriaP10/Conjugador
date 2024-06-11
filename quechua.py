# -*- coding: utf-8 -*-

## leemos el excel

import pandas as pd

verbos = pd.read_excel('verbos.xlsx')

##########################################################################
##########################################################################

import pandas as pd

quechua_suf = pd.read_excel('quechua.xlsx')
quechua_suf = pd.ExcelFile('quechua.xlsx')
D = {}


for hoja in quechua_suf.sheet_names: 
    df = pd.read_excel('quechua.xlsx', sheet_name=hoja)     
    c = df.columns                                          
    df.set_index(c[0], inplace=True)                        
    d = df.to_dict()                                        
    D[hoja] = d

def conj_quechua(base, numero, persona, tiempo):
    return base + D[tiempo][numero][persona]

quechua_pronombres = pd.read_excel('pronombres.xlsx')
quechua_pronombres = pd.ExcelFile('pronombres.xlsx')
DP = {}
dfp = pd.read_excel('pronombres.xlsx')      
c = dfp.columns                             
dfp.set_index(c[0], inplace=True)           
dp = dfp.to_dict()

def conj_final(base,numero,persona,tiempo):
    if numero not in dp:
        st.error(f"Clave '{numero}' no encontrada en el diccionario 'dp'.")
        return
    if persona not in dp[numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'dp[{numero}]'.")
        return
    if tiempo not in D:
        st.error(f"Clave '{tiempo}' no encontrada en el diccionario 'D'.")
        return
    if numero not in D[tiempo]:
        st.error(f"Clave '{numero}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}]'.")
        return
    if persona not in D[tiempo][numero]:
        st.error(f"Clave '{persona}' no encontrada en el diccionario anidado dentro de 'D[{tiempo}][{numero}]'.")
        return
    return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

##########################################################################
##########################################################################

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit

import streamlit as st

st.title(':violet[Conjugador de verbos en quechua]')

## menú desplegable para seleccionar verbos

st.header('Verbo', divider='rainbow')

base = st.selectbox(
    "Seleccione un verbo en quechua: ",
    quechua)

st.write("Seleccionaste: ", dict_que_esp[base])

if base.endswith('y'):
    base = base[:-1]

## menú desplegable para seleccionar numero

st.header('Número', divider='rainbow')

numero = st.radio(
    "Seleccione un numero: ",
    ["singular","plural"],
    index=0,
)

#st.write("Seleccionaste: ", numero)

## menú desplegable para seleccionar PERSONA

st.header('Persona', divider='rainbow')

persona = st.radio(
    "Seleccione una persona: ",
    ["primera inclusiva","primera exclusiva","segunda","tercera"],
    index=0,
)

with st.popover("Abre para responder dudas"):
    st.markdown("Escribe el concepto que desconoces y obtén una explicación de este 😄")
    name = st.text_input("Escribe el concepto")

st.write("Explicación: ", name)
    
#st.write("Seleccionaste: ", persona)

st.header('Tiempo', divider='rainbow')

tiempo = st.radio(
    "Seleccione un tiempo: ",
    ["presente 1","presente 2","presente 3","pasado experimentado 1","pasado experimentado 2","pasado experimentado 3","pasado no experimentado 1","pasado no experimentado 2","pasado no experimentado 3"],
    index=0,
)

#st.write("Seleccionaste: ", tiempo)

#resultado = conj_final(base,numero,persona,tiempo)
#st.write("El verbo conjugado es: ", resultado)

#resultado = conj_final(base, numero, persona, tiempo)
#if resultado:
    #st.write("El verbo conjugado es: ", resultado)
    
st.header('Resultado', divider='rainbow')


#st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

if base and numero and persona and tiempo:
    resultado = conj_final(base, numero, persona, tiempo)
    if resultado:
        st.write("El verbo conjugado es: ")
        st.markdown(f'<p style="font-size:24px; text-align:center;">{resultado}</p>', unsafe_allow_html=True)
else:
    st.error("Por favor, asegúrese de que todas las opciones estén seleccionadas.")


