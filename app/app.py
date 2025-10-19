import streamlit as st
from utils import load_data, preprocess_data

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
    st.write(
        "En esta sección se realiza un análisis exploratorio de los datos de taxis.")

elif opcion == "5. Analisis Estadístico":
    st.header("Análisis Estadístico")
    st.write("En esta sección se lleva a cabo un análisis estadístico de los datos.")

elif opcion == "6. Conclusiones":
    st.header("Conclusiones")
    st.write(
        "En esta sección se presentan las conclusiones derivadas del análisis realizado.")
