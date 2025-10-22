import streamlit as st
from utils import (load_data, preprocess_data, trips_per_hour,
                   avg_trip_duration_per_hour, trip_distance_distribution)
import plotly.express as px

# Configuracion de la pagina.
st.set_page_config(
    page_title="Demanda de Taxis en NYC - Dicimebre 2019",
    layout="wide"
)

# Titulo principal

st.title("Análisis de la Demanda de Taxis en NYC - Diciembre 2019")

# Cargar y preparar datos


@st.cache_data
def load_and_prepare():
    df = load_data()
    df = preprocess_data(df)
    return df


df = load_and_prepare()

# Barra lateral de navegacion
st.sidebar.title("Navegación")
opcion = st.sidebar.radio(
    "Ir a:",
    [
        "1. Planteamiento del problema",
        "2. Marco teórico",
        "3. Metodologia",
        "4. Analisis exploratorio de datos",
        "5. Analisis Estadístico",
        "6. Conclusiones"
    ]
)

# Contenido segun la opcion seleccionada
if opcion == "1. Planteamiento del problema":
    st.header("Planteamiento del problema")
    st.write("En esta sección se describe el problema que se pretende resolver con el análisis de los datos de taxis en NYC durante diciembre de 2019.")

elif opcion == "2. Marco teórico":
    st.header("Marco teórico")
    st.write("En esta sección se presenta el marco teórico relacionado con el análisis de la demanda de taxis.")

elif opcion == "3. Metodologia":
    st.header("Metodología")
    st.write(
        "En esta sección se detalla la metodología utilizada para el análisis de los datos.")

elif opcion == "4. Analisis exploratorio de datos":
    st.header("Análisis exploratorio de datos")

    st.subheader("Cantidad de viajes por hora del día")
    # Calcular viajes por hora
    viajes_hora = trips_per_hour(df)

    # Columna de porcentaje
    viajes_hora['porcentaje'] = viajes_hora['num_viajes'] / \
        viajes_hora['num_viajes'].sum() * 100
    # Grafico interactivo
    fig = px.bar(
        viajes_hora,
        x='hour',
        y='porcentaje',
        title="Distribución porcentual de viajes según la hora del día",
        labels={"hour": "Hora del día",
                "porcentaje": "Porcentaje de viajes (%)"}
    )
    st.plotly_chart(fig)

# Grafico de duracion promedio por hora
    st.subheader("Duración promedio del viaje por hora del día")

    # Calcular duracion promedio por hora
    duracion_hora = avg_trip_duration_per_hour(df)

    # Grafico interactivo
    fig2 = px.line(
        duracion_hora,
        x='hour',
        y='duracion_promedio_min',
        markers=True,
        title="Duración promedio del viaje según la hora del día",
        labels={"hour": "Hora del día",
                "duracion_promedio_min": "Duración promedio (minutos)"}
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Histograma de la distribucion de distancias de viajes

    st.subheader("Distribución de la distancia de los viajes")

    # Filtrar y preparar datos
    df_dist = trip_distance_distribution(df)

    # Histograma interactivo

    fig3 = px.histogram(
        df_dist,
        x='trip_distance',
        nbins=60,
        histnorm="percent",
        title="Distribución de la distancia de los viajes (en millas)",
        labels={"trip_distance": "Distancia del viaje (millas)"},
        opacity=0.75
    )

    fig3.update_layout(bargap=0.05)
    st.plotly_chart(fig3, use_container_width=True)


elif opcion == "5. Analisis Estadístico":
    st.header("Análisis Estadístico")
    st.write("En esta sección se lleva a cabo un análisis estadístico de los datos.")

elif opcion == "6. Conclusiones":
    st.header("Conclusiones")
    st.write(
        "En esta sección se presentan las conclusiones derivadas del análisis realizado.")
