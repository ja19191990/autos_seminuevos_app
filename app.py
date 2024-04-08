# Importar
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer conjuntos de datos en el DataFrame
# vehicles_us = pd.read_csv(r'C:\Users\LENOVO\Desktop\python\data_science\Tripleten\Modulo_5\sprint5\vehicles_us.csv')
vehicles_us = pd.read_csv('vehicles_us.csv')

# Elaboración de header
st.header('Analísis del sector manufacturero de vehículos')

st.write('Esta aplicación aún no es funcional. En construcción.')


hist_button_price = st.button(
    'Construir histograma de los precio de autos vendidos')
if hist_button_price:
    st.write('Histograma del precio de venta de autos')
    # crear un histograma por precio
    fig = px.histogram(vehicles_us, x='price')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_model_year = st.button(
    'Construir histograma del año de modelo de los autos vendidos')
if hist_button_model_year:
    st.write('Histograma del año de modelo de autos vendidos')
    # crear un histograma por año de modelo
    fig = px.histogram(vehicles_us, x='model_year')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_model = st.button(
    'Construir histograma de los modelos de auto vendidos')
if hist_button_model:
    st.write('Histograma del modelo de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='model')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_condition = st.button(
    'Construir histograma de la condición de los auto vendidos')
if hist_button_condition:
    st.write('Histograma por condición de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='condition')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_cylinders = st.button(
    'Construir histograma del cilindraje de autos vendidos')
if hist_button_cylinders:
    st.write('Histograma por cilindraje de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='cylinders')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_odometer = st.button(
    'Construir histograma del kilometraje recorrido de los autos vendidos')
if hist_button_odometer:
    st.write('Histograma por kilometraje de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='odometer')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_type = st.button(
    'Construir histograma de los tipos de autos vendidos')
if hist_button_type:
    st.write('Histograma por tipos de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='type')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_paint_color = st.button(
    'Construir histograma por color de los autos vendidos')
if hist_button_paint_color:
    st.write('Histograma por color de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='paint_color')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_date_posted = st.button(
    'Construir histograma por fecha de publicación de los autos vendidos')
if hist_button_date_posted:
    st.write('Histograma por fecha de publicación de autos vendidos')
    # crear un histograma por modelo
    fig = px.histogram(vehicles_us, x='date_posted')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Despliegue de botón para dispersión
scatt_button = st.button('Construir dispersión')  # crear un botón

if scatt_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de dispersión para el conjunto de datos del precio de venta de autos y kilometraje')
    # crear la dispersión precio vs odometro
    fig = px.scatter(vehicles_us, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
