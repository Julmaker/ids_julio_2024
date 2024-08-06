"""Mapa de Calor de Indices de soporte Julio 2024 Con filtro"""

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

# Título de la aplicación
st.title("Mapa de Calor Índices de Soporte Julio 2024")

# Ruta del archivo Excel
archivo_excel = "ids_jul_dentro_mex.xlsx"

# Cargar datos desde el archivo Excel
df = pd.read_excel(archivo_excel)

# Mostrar el DataFrame
#st.write("Datos cargados:", df)

# Filtrar por semana
semanas = ['Todas'] + df['Semana'].unique().tolist()
semana_seleccionada = st.selectbox("Filtrar por semana:", semanas)

# Filtrar por región
regiones = ['Todas'] + df['Region'].unique().tolist()
region_seleccionada = st.selectbox("Filtrar por región:", regiones)

# Filtrar el DataFrame según la selección de semana y región
df_filtrado = df
if semana_seleccionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['Semana'] == semana_seleccionada]
if region_seleccionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['Region'] == region_seleccionada]

# Centro del mapa en la República Mexicana
centro_mexico = [23.634501, -102.552784]

# Crear el mapa de calor
m = folium.Map(location=centro_mexico, zoom_start=5)

# Añadir puntos de calor
heat_data = [[row['Latitud'], row['Longitud']] for index, row in df_filtrado.iterrows()]
HeatMap(heat_data).add_to(m)

# Mostrar el mapa en Streamlit
folium_static(m)
