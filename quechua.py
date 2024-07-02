# -*- coding: utf-8 -*-

## leemos el excel

import pandas as pd
import os

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

################## TEMA #####################

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #FFF7E8;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#page_bg_img = """
#<style>
#[data-testid="stAppViewContainer"] {
#background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCVYk_ZdjOviMt9YFiLlMd-h7yHzYzakEhLw&s);
#bacground-size: cover;
#}

#[data-testid="stHeader"] {
#background-color: rgba(0, 0, 0, 0);
#}
#</style>
#"""

#st.markdown(page_bg_img, unsafe_allow_html=True)

########### TÍTULO #############

#st.title(':violet[Conjugador de verbos en quechua]')

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');
    .title-font {
        font-family: 'Calibri';
        color: purple;
        text-align: center;
        font-size: 50px;
    }
    </style>
    <h1 class="title-font">Conjugador de verbos en quechua</h1>
    """,
    unsafe_allow_html=True,
)

########### INTRODUCCIÓN #############

#container = st.container(border=True)
#container.write("Esta página web tiene el objetivo de crear conjugaciones de los verbos quechuas más comunes. Al seleccionar un verbo, un número, una persona y un tiempo, se podrá obtener la forma conjugada de dicho verbo con los sufijos correspondientes. Se ofrecen también explicaciones para algunos conceptos de persona y tiempo verbal que pueden resultar confusos. ¡Anímate a conocer más sobre el quechua! 😄")
#st.write("*La variedad de la lengua usada en esta página web es el quechua chanca, hablado en la región de Ayacucho, Perú.")

st.markdown(
    """
    <style>
    .custom-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 5px; /* Añadir espacio debajo del contenedor */
        text-align: justify; 
    }
    .outside-text {
        margin-top: 20px; /* Añadir espacio arriba del texto */
        margin-left: 10px; /* Añadir espacio a la izquierda del texto */
        margin-right: 10px; /* Añadir espacio a la derecha del texto */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-container">
        Esta página web tiene el objetivo de crear conjugaciones de los verbos quechuas más comunes. Al seleccionar un verbo, un número, una persona y un tiempo, se podrá obtener la forma conjugada de dicho verbo con los sufijos correspondientes. Se ofrecen también explicaciones para algunos conceptos de persona y tiempo verbal que pueden resultar confusos. ¡Anímate a conocer más sobre el quechua! 😄
    </div>
    """,
    unsafe_allow_html=True
)

# Texto fuera del contenedor con márgenes ajustados
st.markdown(
    """
    <p class="outside-text">
    *La variedad de la lengua usada en esta página web es el quechua chanca, hablado en la región de Ayacucho, Perú.
    </p>
    """,
    unsafe_allow_html=True
)


from PIL import Image

# Ruta de la imagen local
ruta_imagen_local = "arco-ayacucho.jpg"

# Abre la imagen
image = Image.open(ruta_imagen_local)

# CSS para centrar la imagen
st.markdown(
    """
    <style>
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%; /* Ajusta este valor para cambiar el tamaño de la imagen */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Usar st.image para cargar la imagen con la opción de usar el ancho de la columna
st.image(image, caption='Arco de Ayacucho', use_column_width=False, width=200)

# HTML para centrar la imagen
st.markdown("""
    <img src="{ruta_imagen_local}" class="centered-image">
    """, unsafe_allow_html=True)
    
########### menú desplegable para seleccionar VERBOS #################

st.header('Verbo', divider='rainbow')

base = st.selectbox(
    "Seleccione un verbo en quechua: ",
    quechua)

st.write("Seleccionaste: ", dict_que_esp[base])

if base.endswith('y'):
    base = base[:-1]

############## menú desplegable para seleccionar NUMERO ##############

st.header('Número', divider='rainbow')

numero = st.radio(
    "Seleccione un número: ",
    ["singular","plural"],
    index=0,
)

#st.write("Seleccionaste: ", numero)

# Diccionario de explicaciones
explicaciones_persona = {
    "primera inclusiva": "La primera persona inclusiva se refiere a 'nosotros', incluyendo a la persona con la que se habla.",
    "primera exclusiva": "La primera persona exclusiva se refiere a 'nosotros', excluyendo a la persona con la que se habla.",
    "segunda": "La segunda persona se refiere a 'tú' o 'usted'.",
    "tercera": "La tercera persona se refiere a 'él', 'ella' o 'ellos'."
}

explicaciones_tiempo = {
    "presente 1": "El presente 1 es el presente simple. Este se usa para describir acciones que ocurren regularmente a lo largo del tiempo.",
    "presente 2": "El presente 2 es el presente progresivo. Este se usa para describir acciones que están ocurriendo en este momento.",
    "presente 3": "El presente 3 es el presente habitual. Este se usa para describir acciones que se repiten en el tiempo de manera finita, como hábitos o rutinas.",
    "pasado experimentado 1": "El pasado experimentado 1 es el pasado experimentado simple. Este se usa para describir acciones que ocurrieron en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
    "pasado experimentado 2": "El pasado experimentado 2 es el pasado experimentado progresivo. Este se usa para describir acciones que estuvieron ocurriendo en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
    "pasado experimentado 3": "El pasado experimentado 3 es el pasado experimentado habitual. Este se usa para describir acciones que ocurrían regularmente en el pasado y que le constan al sujeto por ser testigo directo de la acción.",
    "pasado no experimentado 1": "El pasado no experimentado 1 es el pasado no experimentado simple. Este se usa para describir acciones que ocurrieron en el pasado sin la participación o el conocimiento directo del sujeto.",
    "pasado no experimentado 2": "El pasado no experimentado 2 es el pasado no experimentado progresivo. Este se usa para describir acciones que estuvieron ocurriendo en el pasado sin la participación o el conocimiento directo del sujeto.",
    "pasado no experimentado 3": "El pasado no experimentado 3 es el pasado no experimentado habitual. Este se usa para describir acciones que ocurrían regularmente en el pasado sin la participación o el conocimiento directo del sujeto."
}

###### menú desplegable para seleccionar PERSONA ######

st.header('Persona', divider='rainbow')

#persona = st.radio(
    #"Seleccione una persona: ",
    #["primera inclusiva","primera exclusiva","segunda","tercera"],
    #index=0,
#)
    
#st.write("Seleccionaste: ", persona)

persona = st.selectbox("Seleccione una persona: ", list(explicaciones_persona.keys()), index=0)
explicacion_persona_placeholder = st.empty()
explicaciones_persona["primera inclusiva"] += "<br><br>Ejemplo: '(Todos) Nosotros vamos al mercado.'"
explicaciones_persona["primera exclusiva"] += "<br><br>Ejemplo: 'Nosotros (pero no tú) vamos al mercado.'"

explicacion_persona_placeholder.markdown("**Explicación de persona seleccionada:** " + explicaciones_persona[persona], unsafe_allow_html=True)


#################### menú desplegable para seleccionar TIEMPO ###################

st.header('Tiempo', divider='rainbow')

#tiempo = st.radio(
    #"Seleccione un tiempo: ",
    #["presente 1","presente 2","presente 3","pasado experimentado 1","pasado experimentado 2","pasado experimentado 3","pasado no experimentado 1","pasado no experimentado 2","pasado no experimentado 3"],
    #index=0,
#)

#st.write("Seleccionaste: ", tiempo)

st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tiempo = st.selectbox("Seleccione un tiempo: ", list(explicaciones_tiempo.keys()), index=0)
explicacion_tiempo_placeholder = st.empty()
explicaciones_tiempo["presente 1"] += "<br><br>Ejemplo: 'Yo veo televisión.'"
explicaciones_tiempo["presente 2"] += "<br><br>Ejemplo: 'Yo estoy viendo televisión.'"
explicaciones_tiempo["presente 3"] += "<br><br>Ejemplo: 'Yo suelo ver televisión.'"
explicaciones_tiempo["pasado experimentado 1"] += "<br><br>Ejemplo: 'Yo veía televisión.'"
explicaciones_tiempo["pasado experimentado 2"] += "<br><br>Ejemplo: 'Yo estaba viendo televisión.'"
explicaciones_tiempo["pasado experimentado 3"] += "<br><br>Ejemplo: 'Yo solía ver televisión.'"
explicaciones_tiempo["pasado no experimentado 1"] += "<br><br>Ejemplo: '(Dicen que) Yo veía televisión.'"
explicaciones_tiempo["pasado no experimentado 2"] += "<br><br>Ejemplo: '(Dicen que) Yo estaba viendo televisión.'"
explicaciones_tiempo["pasado no experimentado 3"] += "<br><br>Ejemplo: '(Dicen que) Yo solía ver televisión.'"

explicacion_tiempo_placeholder.markdown("**Explicación de tiempo seleccionado:** " + explicaciones_tiempo[tiempo], unsafe_allow_html=True)
    
#resultado = conj_final(base,numero,persona,tiempo)
#st.write("El verbo conjugado es: ", resultado)

#resultado = conj_final(base, numero, persona, tiempo)
#if resultado:
    #st.write("El verbo conjugado es: ", resultado)

# Mostrar explicaciones
#st.write("### Explicaciones")
#explicacion_persona = st.selectbox("Seleccione una persona para ver la explicación:", list(explicaciones_persona.keys()))
#explicacion_tiempo = st.selectbox("Seleccione un tiempo para ver la explicación:", list(explicaciones_tiempo.keys()))

#st.write("Explicación de la persona seleccionada: ", explicaciones_persona[explicacion_persona])
#st.write("Explicación del tiempo seleccionado: ", explicaciones_tiempo[explicacion_tiempo])

################## RESULTADO ####################

st.header('Resultado', divider='rainbow')

#st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)

if base and numero and persona and tiempo:
    resultado = conj_final(base, numero, persona, tiempo)
    if resultado:
        st.write("El verbo conjugado es: ")
        st.markdown(f'<p style="font-size:24px; text-align:center;">{resultado}</p>', unsafe_allow_html=True)
else:
    st.error("Por favor, asegúrese de que todas las opciones estén seleccionadas.")

