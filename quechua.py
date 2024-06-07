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

## menú desplegable para seleccionar numero

numero = st.radio(
    "Seleccione un numero: ",
    ["singular","plural"],
    index=None,
)

#st.write("Seleccionaste: ", numero)

## menú desplegable para seleccionar persona

persona = st.radio(
    "Seleccione una persona: ",
    ["primera inclusiva","primera exclusiva","segunda","tercera"],
    index=None,
)

#st.write("Seleccionaste: ", persona)

tiempo = st.radio(
    "Seleccione un tiempo: ",
    ["Presente simple","Presente progresivo","Presente habitual","Pasado experimentado simple","Pasado experimentado progresivo","Pasado experimentado habitual","Pasado no experimentado simple","Pasado no experimentado progres","Pasado no experimentado habitua"],
    index=None,
)

#st.write("Seleccionaste: ", tiempo)

resultado = conj_final(base,numero,persona,tiempo)

st.write("El verbo conjugado es: ", resultado)