{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import streamlit as st\
\
# 
\f1 \uc0\u55357 \u56593 
\f0  API Key de Notion\
NOTION_API_KEY = "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"\
\
# 
\f1 \uc0\u55357 \u56514 
\f0  ID de la base de datos de Notion\
DATABASE_ID = "18948f9bb0e481be86f1f5af7816af4a"\
\
# 
\f1 \uc0\u55357 \u56545 
\f0  Headers para la API de Notion\
HEADERS = \{\
    "Authorization": f"Bearer \{NOTION_API_KEY\}",\
    "Content-Type": "application/json",\
    "Notion-Version": "2022-06-28",\
\}\
\
# 
\f1 \uc0\u55357 \u57056 
\f0  Funci\'f3n para obtener los proyectos de Notion\
def obtener_proyectos():\
    url = f"https://api.notion.com/v1/databases/\{DATABASE_ID\}/query"\
    response = requests.post(url, headers=HEADERS)\
\
    if response.status_code == 200:\
        return response.json()["results"]\
    else:\
        st.error(f"
\f1 \uc0\u10060 
\f0  Error al conectar con Notion: \{response.status_code\}")\
        return []\
\
# Obtener proyectos desde Notion\
proyectos = obtener_proyectos()\
\
# Variables de suma\
total_monto = 0\
total_monto_general = 0\
num_proyectos_pagados = 0\
\
# Procesar datos\
for proyecto in proyectos:\
    propiedades = proyecto["properties"]\
    \
    # Obtener estatus y monto\
    estatus = propiedades["Estatus de cartera"]["select"]["name"]\
    monto = propiedades["Monto mensual"]["number"]\
\
    # Sumar al total general\
    total_monto_general += monto\
\
    # Filtrar por "Finalizado y pagado"\
    if estatus == "Finalizado y pagado":\
        total_monto += monto\
        num_proyectos_pagados += 1\
\
# Calcular porcentaje\
porcentaje_pagado = (total_monto / total_monto_general) * 100 if total_monto_general > 0 else 0\
\
# ---------------------\
# 
\f1 \uc0\u55357 \u56522 
\f0  INTERFAZ EN STREAMLIT\
# ---------------------\
st.set_page_config(page_title="Reporte de Proyectos", layout="wide")\
\
st.markdown("<h2 style='text-align: center;'>Resumen de Proyectos Finalizados</h2>", unsafe_allow_html=True)\
\
# Tarjeta con dise\'f1o visual\
st.markdown(\
    f"""\
    <div style='display: flex; justify-content: center; align-items: center; background-color: #E8F5E9; padding: 20px; border-radius: 10px; width: 60%; margin: auto;'>\
        <div style='flex: 1;'>\
            <h3 style='color: #2E7D32;'>Pagado</h3>\
            <p style='font-size: 24px; color: #2E7D32; font-weight: bold;'>$\{total_monto:,.2f\} MM</p>\
        </div>\
        <div style='flex: 1; text-align: right;'>\
            <p style='font-size: 20px; color: #555;'>\{porcentaje_pagado:.1f\}%</p>\
        </div>\
    </div>\
    """,\
    unsafe_allow_html=True\
)\
\
st.write(f"
\f1 \uc0\u55357 \u56524 
\f0  **Total de proyectos finalizados y pagados:** \{num_proyectos_pagados\}")\
st.write(f"
\f1 \uc0\u55357 \u56524 
\f0  **Monto total en base de datos:** $\{total_monto_general:,.2f\} MM")\
}
