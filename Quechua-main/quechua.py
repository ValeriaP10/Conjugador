# -*- coding: utf-8 -*-

## leemos el excel

import pandas as pd
verbos = pd.read_excel('verbos.xlsx')

## diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['espanol'])

dict_que_esp = dict(zip(quechua,espanol))

## importamos streamlit

import streamlit as st

## menú desplegable para seleccionar verbos

option = st.selectbox(
    "Seleccione un verbo en quechua: ",
    quechua)

st.write("Seleccionaste: ", dict_que_esp[option])

## menú desplegable para seleccionar persona

persona = st.radio(
    "Seleccione una persona: ",
    ["primera inclusiva","primera exclusiva","segunda", "tercera"],
    index=None,
)

st.write("Seleccionaste: ", persona)

## menú desplegable para seleccionar numero

numero = st.radio(
    "Seleccione un numero: ",
    ["singular", "Plural"],
    index=None,
)

st.write("Seleccionaste: ", numero)

