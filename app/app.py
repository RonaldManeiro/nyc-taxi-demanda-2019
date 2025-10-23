import streamlit as st
from utils import (load_data, preprocess_data, trips_per_hour,
                   avg_trip_duration_per_hour, trip_distance_distribution, payment_distribution, fare_tip_relation, trips_per_zone)
import plotly.express as px
import statsmodels.api as sm
import json
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


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
    st.write("""
                La movilidad urbana es uno de los ejes más importantes para el funcionamiento eficiente de una gran ciudad. En metrópolis como Nueva York, el servicio de taxis juega un rol crucial en el transporte diario de millones de personas. A lo largo del día, la demanda de taxis no es uniforme: varía según la hora, el día de la semana y la zona geográfica. Estas variaciones reflejan patrones sociales, económicos y de comportamiento urbano (por ejemplo, desplazamientos laborales en horas punta, actividades nocturnas o turismo).
             """)
    st.write("Comprender estos patrones permite a empresas, autoridades de transporte y conductores tomar decisiones más informadas, como:")
    st.markdown("""
    - Optimizar la distribución de taxis durante las horas pico 
    - Diseñar políticas de movilidad más eficientes 
    - Reducir tiempos de espera para usuarios 
    """)
    st.write("Este proyecto busca analizar la demanda de taxis en la ciudad de Nueva York durante 2019, con enfoque en patrones horarios y geográficos, utilizando herramientas estadísticas y computacionales modernas.")
    
    st.subheader("Objetivo General")
    st.write("Analizar la distribución temporal y espacial de la demanda de taxis en Nueva York durante el año 2019, para identificar zonas y horarios de alta demanda que puedan aportar conclusiones útiles desde el punto de vista estadístico y urbano.")

    st.subheader("Objetivos Especificos")
    st.markdown("""
    - Procesar y limpiar la base de datos de viajes en taxi para obtener un subconjunto representativo manejable.
    - Explorar la variación de la demanda a lo largo del día, identificando horas pico y horas valle.
    - Analizar la distribución geográfica de los viajes para determinar zonas de mayor concentración de demanda.
    - Construir un dashboard en Power BI que permita visualizar los patrones temporales y espaciales.
    - Desarrollar una aplicación en Python (Streamlit) para interactuar dinámicamente con los datos y realizar análisis básicos.
    - Realizar un breve análisis estadístico descriptivo que permita interpretar los resultados obtenidos.
    """)


elif opcion == "2. Marco teórico":
    st.header("Marco teórico")

    st.subheader("Antecedentes de la Investigación")
   
    st.write("Los antecedentes permiten definir e interpretar el problema planteado mediante la síntesis de un marco referencial conformado por las exploraciones y trabajos vinculados a la investigación, estableciendo un enfoque teórico y metodológico de la misma. Los antecedentes que sustentan esta investigación son las que mencionan a continuación:")
    
    st.write("En “Analysis and prediction of New York City taxi and Uber demands” (realizado por D. Correa y C. Moyano), analizan sobre la distribución espacio/temporal y el nivel de demanda tanto de los taxis (amarillos y verdes) como del servicio de Uber. Y no solamente se llegó a la conclusión de que los dos servicios son imprescindibles en Nueva York, sino que también el más utilizado es el de los taxis amarillos con un 86% del total de viajes registrados (se analizaron más de 90 millones de viajes, y 78.382.423 fueron de los taxis amarillos).  Además de la aplicación de herramientas estadísticas como el “modelo de regresión lineal” para el análisis de los resultados.")
    
    st.write("También se encuentra el artículo “Testimonios del Taxi: Aprendizajes de 15 años de viajes en Nueva York” (hecho por Fernando A. Ramírez, en el año 2024), donde el autor explica la manera en que las apps de movilidad han impactado en los negocios tradicionales de taxis en Nueva York (aunque no tomó en cuenta por completo el año 2019 durante la realización del análisis, debido a la aparición del Covid-19 durante aquella época y el impacto predecible que iba a tener en los medios de transporte debido a la cuarentena). Se puede resaltar el hecho de que los taxis amarillos no estaban “captando muchos viajes cortos que son más rentables por minuto de conducción”, mientras que con las apps de movilidad ocurría el caso contrario hacían “un mejor trabajo captando viajes más cortos y menos planificados gracias a la ubicuidad y facilidad de pago que ofrecen estas aplicaciones móviles”.")

    st.subheader("Bases Teóricas")
    
    st.write("Se tiene que la Movilidad Urbana es el conjunto de desplazamientos de personas y mercancías dentro de un área urbana y las condiciones en las que se realizan. Este concepto abarca todos los modos de transporte (público, privado, taxis/servicios de viaje compartido) y su impacto en la calidad de vida, el medio ambiente y la eficiencia económica de la ciudad.")
    
    st.write("Entre los medios de transporte que se usan hoy en día en la sociedad, el Taxi es un vehículo de alquiler que incluye un conductor profesional que se contrata para transportar pasajeros a uno o varios destinos elegidos por ellos (el cliente puede indicar el punto de partida y el de llegada en su viaje). La palabra «taxi», según el Diccionario de la lengua española, es una forma abreviada de la palabra «taxímetro», que a su vez deriva del griego τάξις, «tasa» y μέτρον, que significa «medida». Usualmente, los lugares donde se recoge y se deja al pasajero se deciden por el proveedor (oferente), mientras que el usuario (demandante) los determina.")

    st.write("A diferencia de los otros tipos de transporte de personas, como son las líneas del metro, tranvía o del autobús, el servicio ofrecido por el taxi se caracteriza por ser «puerta a puerta». La persona que tiene por oficio la conducción de un taxi se le llama «taxista». Sin mencionar que la tarifa se calcula generalmente a través de un taxímetro, aunque suelen estar reguladas por la autoridad local.")

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

    # Grafico de la distribucion de metodos de pago
    st.subheader("Método de pago más utilizado")
    from utils import payment_distribution
    pagos = payment_distribution(df)

    fig4 = px.pie(
        pagos,
        names="Método de pago",
        values="Cantidad de viajes",
        title="Distribución de los métodos de pago",
        hole=0.4
    )
    st.plotly_chart(fig4)

    # Grafico de relacion entre tarifa total y propina

    st.subheader("Relación entre tarifa total y propina")
    from utils import fare_tip_relation

    df_fare_tip = fare_tip_relation(df)

    fig5 = px.scatter(
        df_fare_tip,
        x='total_amount',
        y='tip_amount',
        opacity=0.6,
        title="Relación entre Tarifa Total y Propina (con línea de tendencia)",
        labels={
            "total_amount": "Tarifa total (USD)",
            "tip_amount": "Propina (USD)"
        },
        trendline="ols",
        color_discrete_sequence=["#1f77b4"]
    )

    # Análisis estadistico automatico
    # Calcular la correlacion entre ambas variables
    correlacion = df_fare_tip['total_amount'].corr(df_fare_tip["tip_amount"])

    # Interpretar la correlacion
    if correlacion > 0.7:
        interpretacion = "fuerte y positiva"
    elif correlacion > 0.3:
        interpretacion = "moderada y positiva"
    elif correlacion > 0:
        interpretacion = "débil y positiva"
    elif correlacion < -0.7:
        interpretacion = "fuerte y negativa"
    elif correlacion < -0.3:
        interpretacion = "moderada y negativa"
    elif correlacion < 0:
        interpretacion = "débil y negativa"
    else:
        interpretacion = "nula o inexistente"

    # Texto interpretativo
    analisis = f"""
    **Análisis de la relación entre tarifa total y propina:**
    - Coeficiente de correlación: **{correlacion:.3f}**
    - Interpretación: Existe una correlación {interpretacion} entre el monto total del viaje y la propina.
    """

    st.plotly_chart(fig5)
    st.markdown(analisis)

    # Mapa de calor de zonas
    st.subheader("Mapa del Total de Viajes por Zona de Recogida")

    from utils import trips_per_zone
    zonas, geojson = trips_per_zone(df)

    fig6 = px.choropleth_mapbox(
        zonas,
        geojson=geojson,
        color="Total_viajes",
        locations="location_id",
        featureidkey="properties.location_id",
        hover_name="Zone",
        hover_data=["Borough", "Total_viajes"],
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        center={"lat": 40.7128, "lon": -74.0060},
        zoom=9,
        opacity=0.6,
        title="Total de Viajes por Zona de Recogida"
    )
    st.plotly_chart(fig6, use_container_width=True)

    # Mapa del total de viajes por zona de llegada
    st.subheader("Mapa del Total de Viajes por Zona de Llegada")

    from utils import trips_per_dropoff_zone
    zonas_drop, geojson_drop = trips_per_dropoff_zone(df)

    fig7 = px.choropleth_mapbox(
        zonas_drop,
        geojson=geojson_drop,
        color="Total_viajes",
        locations="location_id",
        featureidkey="properties.location_id",
        hover_name="Zone",
        hover_data=["Borough", "Total_viajes"],
        color_continuous_scale="Viridis",
        mapbox_style="carto-positron",
        center={"lat": 40.7128, "lon": -74.0060},
        zoom=9,
        opacity=0.6,
        title="Total de viajes por zona de llegada"
    )
    st.plotly_chart(fig7, use_container_width=True)


elif opcion == "5. Analisis Estadístico":
    st.header("Análisis Estadístico")
    st.write("En esta sección se lleva a cabo un análisis estadístico de los datos.")

elif opcion == "6. Conclusiones":
    st.header("Conclusiones")
    st.write(
        "En esta sección se presentan las conclusiones derivadas del análisis realizado.")
