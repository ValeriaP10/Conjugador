# -*- coding: utf-8 -*-

## leemos el excel

import pandas as pd
verbos = pd.read_excel('verbos.xlsx')

##########################################################################
##########################################################################

import pandas as pd
quechua = pd.read_excel('quechua.xlsx')
quechua = pd.ExcelFile('quechua.xlsx')
D = {}


for hoja in quechua.sheet_names: 
    df = pd.read_excel('quechua.xlsx', sheet_name=hoja)     
    c = df.columns                                          
    df.set_index(c[0], inplace=True)                        
    d = df.to_dict()                                        
    D[hoja] = d

quechua_pronombres = pd.read_excel('pronombres.xlsx')
quechua_pronombres = pd.ExcelFile('pronombres.xlsx')
DP = {}
dfp = pd.read_excel('pronombres.xlsx')      
c = dfp.columns                             
dfp.set_index(c[0], inplace=True)           
dp = dfp.to_dict()

def conj_final(base,numero,persona,tiempo):
    return dp[numero][persona] + ' ' + base + D[tiempo][numero][persona]

##########################################################################
##########################################################################

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit

import streamlit as st

## menú desplegable para seleccionar verbos

base = st.selectbox(
    "Seleccione un verbo en quechua: ",
    quechua)

# st.write("Seleccionaste: ", dict_que_esp[base])

## menú desplegable para seleccionar persona

persona = st.radio(
    "Seleccione una persona: ",
    ["primera inclusiva","primera exclusiva","segunda", "tercera"],
    index=None,
)

#st.write("Seleccionaste: ", persona)

## menú desplegable para seleccionar numero

numero = st.radio(
    "Seleccione un numero: ",
    ["singular", "plural"],
    index=None,
)

#st.write("Seleccionaste: ", numero)

tiempo = st.radio(
    "Seleccione un tiempo: ",
    ["presente simple","presente progresivo","presente habitual","pasado experimentado simple","pasado experimentado progresivo","pasado experimentado habitual","pasado no experimentado simple","pasado no experimentado progresivo","pasado no experimentado habitual"],
    index=None,
)

#st.write("Seleccionaste: ", tiempo)

st.write("El verbo conjugado es: ",conj_final(base,numero,persona,tiempo))