import streamlit as st
from utils import (load_data, preprocess_data, trips_per_hour,
                   avg_trip_duration_per_hour, trip_distance_distribution, payment_distribution, fare_tip_relation, trips_per_zone)
import plotly.express as px
import statsmodels.api as sm
import json
import os
import requests
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Configuracion de la pagina.
st.set_page_config(
    page_title="Demanda de Taxis en NYC - Diciembre 2019",
    page_icon="🚕",
    layout="wide"
)

# Titulo principal

st.title("Análisis de la Demanda de Taxis en Nueva York - Diciembre 2019")


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
        "1. Introducción",
        "2. Planteamiento del problema",
        "3. Marco teórico",
        "4. Datos",
        "5. Cuestionario SQL",
        "6. Análisis exploratorio de datos",
        "7. Análisis Estadístico",
        "8. Conclusiones",
        "9. Bibliografías"
    ]
)

# Contenido segun la opcion seleccionada
if opcion == "1. Introducción":
    st.markdown("""
### 📊 Introducción

Este proyecto presenta un análisis sobre el comportamiento de la **demanda de taxis en la ciudad de Nueva York durante diciembre de 2019**.

El objetivo principal es **comprender los patrones de movilidad**, identificar las **zonas con mayor actividad** y analizar cómo **varía la demanda según la hora del día y la ubicación**.

La aplicación está compuesta por:
- 🧠 Un **análisis computacional** desarrollado con **Python y Streamlit**.
- 📈 Un **dashboard en Power BI**.
- 💾 Un **cuestionario SQL** con consultas específicas sobre la base de datos.

---

Puedes explorar los distintos apartados desde el menú lateral ✅
""")

if opcion == "2. Planteamiento del problema":
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
    - Explorar la variación de la demanda a lo largo del día, identificando horas pico.
    - Analizar la distribución geográfica de los viajes para determinar zonas de mayor concentración de demanda.
    - Construir un dashboard en Power BI que permita visualizar los patrones temporales y espaciales.
    - Desarrollar una aplicación en Python (Streamlit) para interactuar dinámicamente con los datos y realizar análisis básicos.
    - Realizar un breve análisis estadístico descriptivo que permita interpretar los resultados obtenidos.
    """)


elif opcion == "3. Marco teórico":
    st.header("Marco teórico")

    st.subheader("Antecedentes de la Investigación")

    st.write("Los antecedentes permiten definir e interpretar el problema planteado mediante la síntesis de un marco referencial conformado por las exploraciones y trabajos vinculados a la investigación, estableciendo un enfoque teórico y metodológico de la misma. Los antecedentes que sustentan esta investigación son las que mencionan a continuación:")

    st.write("En “Analysis and prediction of New York City taxi and Uber demands” (realizado por D. Correa y C. Moyano), analizan sobre la distribución espacio/temporal y el nivel de demanda tanto de los taxis (amarillos y verdes) como del servicio de Uber. Y no solamente se llegó a la conclusión de que los dos servicios son imprescindibles en Nueva York, sino que también el más utilizado es el de los taxis amarillos con un 86% del total de viajes registrados (se analizaron más de 90 millones de viajes, y 78.382.423 fueron de los taxis amarillos).  Además de la aplicación de herramientas estadísticas como el “modelo de regresión lineal” para el análisis de los resultados.")

    st.write("También se encuentra el artículo “Testimonios del Taxi: Aprendizajes de 15 años de viajes en Nueva York” (hecho por Fernando A. Ramírez, en el año 2024), donde el autor explica la manera en que las apps de movilidad han impactado en los negocios tradicionales de taxis en Nueva York (aunque no tomó en cuenta por completo el año 2019 durante la realización del análisis, debido a la aparición del Covid-19 durante aquella época y el impacto predecible que iba a tener en los medios de transporte debido a la cuarentena). Se puede resaltar el hecho de que los taxis amarillos no estaban “captando muchos viajes cortos que son más rentables por minuto de conducción”, mientras que con las apps de movilidad ocurría el caso contrario hacían “un mejor trabajo captando viajes más cortos y menos planificados gracias a la ubicuidad y facilidad de pago que ofrecen estas aplicaciones móviles”.")

    st.subheader("Bases Teóricas")

    st.write("Se tiene que la Movilidad Urbana es el conjunto de desplazamientos de personas y mercancías dentro de un área urbana y las condiciones en las que se realizan. Este concepto abarca todos los modos de transporte (público, privado, taxis/servicios de viaje compartido) y su impacto en la calidad de vida, el medio ambiente y la eficiencia económica de la ciudad.")

    st.write("Entre los medios de transporte que se usan hoy en día en la sociedad, el Taxi es un vehículo de alquiler que incluye un conductor profesional que se contrata para transportar pasajeros a uno o varios destinos elegidos por ellos (el cliente puede indicar el punto de partida y el de llegada en su viaje). La palabra «taxi», según el Diccionario de la lengua española, es una forma abreviada de la palabra «taxímetro», que a su vez deriva del griego τάξις, «tasa» y μέτρον, que significa «medida». Usualmente, los lugares donde se recoge y se deja al pasajero se deciden por el proveedor (oferente), mientras que el usuario (demandante) los determina.")

    st.write("A diferencia de los otros tipos de transporte de personas, como son las líneas del metro, tranvía o del autobús, el servicio ofrecido por el taxi se caracteriza por ser «puerta a puerta». La persona que tiene por oficio la conducción de un taxi se le llama «taxista». Sin mencionar que la tarifa se calcula generalmente a través de un taxímetro, aunque suelen estar reguladas por la autoridad local.")

    st.write("Los tipos de taxis se pueden clasificar por su nivel de servicio (ejecutivo, convencional), tecnología (eléctrico, autónomo), accesibilidad (adaptado) o función (colectivo). También existen clasificaciones locales, como los taxis de sitio, libres o de radio en algunas ciudades, o el tipo de vehículo usado.")

    st.markdown("**Según el tipo de servicio y vehículo:**")

    st.markdown("""
    - **Taxis convencionales:** Vehículos estándar que se pueden tomar en la calle o en paradas. 
    - **Taxis ejecutivos:** Suelen ser vehículos de gama alta, más cómodos y con un servicio exclusivo. 
    - **Taxis adaptados:** Diseñados para personas con discapacidades, equipados con rampas o elevadores. 
    - **Taxis eléctricos:** Vehículos de cero emisiones, impulsados por energía eléctrica. 
    - **Taxis autónomos:** Vehículos que operan sin conductor humano, gracias a la tecnología avanzada. 
    - **Taxis acuáticos:** En ciudades con cuerpos de agua, ofrecen transporte sobre el agua, como en ríos o lagos.
    """)

    st.markdown("**Según la modalidad y operación:**")

    st.markdown("""
    - **Taxis de sitio:** Tienen una ubicación fija y se solicitan a través de una central telefónica.
    - **Taxis libres:** Se pueden encontrar en la calle o en paradas designadas.
    - **Taxis colectivos:** Comparten ruta y precio predeterminado entre varios pasajeros. A veces se les llama "colectivos" o "carro de ruta".
    """)

    st.markdown("**Según el país:**")

    st.markdown("""
    - **Taxis amarillos:** Característicos en muchas ciudades, a menudo asociados con el transporte público general. 
    - **Taxis de sitio o "pulmonías":** En ciertas regiones, son vehículos específicos con un color o característica distintiva, como en Mazatlán. 
    - **Cocotaxis:** Vehículos motorizados con forma de coco, típicos de Cuba. 
    - **Tuc tuc:** Mototaxis que se encuentran en ciudades de Tailandia y otras partes del mundo.
    """)

    st.write("En Nueva York, los taxis son de dos variedades: amarillo y verde (son símbolos de la ciudad ampliamente reconocibles). Los vehículos de taxi deben tener una medalla de taxi para operar: este sistema fue creado en 1937 como una limitación impuesta por el gobierno en la oferta de taxis; pero luego, Nueva York ya no vendió más medallas hasta 1996 después de una subasta donde se presentaría más adelante una escasez que, para el 2014, se vendían a más de un millón de dólares cada una). La principal diferencia entre los taxis amarillos y verdes radica en las zonas donde están autorizados para recoger pasajeros:")

    st.markdown("""
    - **Los taxis amarillos (“medallion taxis”)** pueden recoger pasajeros en cualquier punto de la ciudad de Nueva York, incluyendo los cinco distritos y los aeropuertos. Además de que se pueden detener en la calle con la mano o encontrar en las paradas designadas para taxis.
    - **Los taxis verdes** (comúnmente conocidos como **"boro taxis"**, que empezaron a aparecer en agosto del 2013), están autorizados para recoger pasajeros en los distritos de Queens, Brooklyn, Bronx y Staten Island, así como en la parte alta de Manhattan (por encima de la calle 96 Este y la calle 110 Oeste). No pueden recoger pasajeros que los detengan en la calle en el centro de Manhattan (la "zona de exclusión de llamadas") ni en los aeropuertos de LaGuardia y JFK.

    """)

elif opcion == "4. Datos":
    st.header("Muestra y Estructura de los Datos")

    st.markdown("""
        Aquí se muestra una **muestra aleatoria** del DataFrame resultante después del proceso de limpieza. 
        Este es el conjunto de datos final utilizado para la aplicación; en la aplicacion se utilizó una muestra de 500.000 datos.
    """)

    # Mostrar una muestra significativa (ej. las primeras 1000 filas)
    st.subheader("Muestra de Datos (2,000 Filas)")
    st.dataframe(
        df.head(2000),
        use_container_width=True,
        # Opcional: ajustar altura si el DF es muy grande visualmente
        # height=400
    )

elif opcion == "5. Cuestionario SQL":
    import pandas as pd

    st.header("🔑 Resultados Clave del Cuestionario")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    kpis_path = os.path.join(current_dir, "..", "data", "processed",
                             "resultados_consolidados.csv")

    try:
        # Cargar el archivo con la ruta absoluta
        df_kpis = pd.read_csv(kpis_path)

    except FileNotFoundError:
        # Se ejecutara si no se encuentra el archivo
        st.error(
            f"Error (Archivo no encontrado): Verifique que 'resultados_consolidados.csv' esté en: {kpis_path}"
        )
        st.stop()

    try:
        # 1. Título principal de la sección
        st.subheader("Resultados Detallados por Consulta SQL")
        st.markdown("---")

        # 2. Iterar por cada consulta en orden (1, 2, 3, 4, ...)
        for id_consulta in sorted(df_kpis['ID_Consulta'].unique()):
            # Filtrar el DataFrame para la consulta actual
            df_consulta = df_kpis[df_kpis['ID_Consulta'] == id_consulta].copy()

            # Obtener el nombre de la consulta para el título
            nombre_consulta = df_consulta['Consulta'].iloc[0]

            # Título de la sección
            st.markdown(f"### 🔍 Consulta {id_consulta}: {nombre_consulta}")
            st.markdown("---")

            # Lógica de visualización específica por ID

            if id_consulta == 1:
                # C1: Distancia promedio y tiempo promedio
                col1, col2 = st.columns(2)

                # Distancia Promedio
                dist_row = df_consulta[df_consulta['Etiqueta']
                                       == 'Distancia promedio'].iloc[0]
                col1.metric("Distancia Promedio",
                            f"{dist_row['Valor Numerico']} {dist_row['Unidad']}")

                # Tiempo Promedio
                tiempo_row = df_consulta[df_consulta['Etiqueta']
                                         == 'Tiempo promedio'].iloc[0]
                col2.metric(
                    "Tiempo Promedio", f"{tiempo_row['Valor Numerico']} {tiempo_row['Unidad']}")

            elif id_consulta == 2:
                # C2: Método de pago más común

                # 1. Obtener el nombre del método
                metodo_row = df_consulta[df_consulta['Etiqueta']
                                         == 'Método de pago más usado'].iloc[0]
                metodo = metodo_row['Unidad']

                # 2. Obtener el conteo
                conteo_row = df_consulta[df_consulta['Etiqueta']
                                         == 'Cantidad de viajes que lo usaron'].iloc[0]
                conteo = int(conteo_row['Valor Numerico'])

                st.metric("Método de Pago Más Común",
                          metodo.title(),
                          f"{conteo:,} viajes registrados")

            elif id_consulta == 3:
                # C3: Propina promedio según tipo de pago
                st.write("Propina Promedio por Método de Pago (Propina > 0):")
                df_display = df_consulta[['Etiqueta', 'Valor Numerico', 'Unidad']].rename(columns={
                    'Etiqueta': 'Tipo de Pago',
                    'Valor Numerico': 'Propina Promedio',
                    'Unidad': 'Unidad'
                })
                st.dataframe(df_display, hide_index=True)

            elif id_consulta == 4:
                # C4: Porcentaje de viajes por tipo de tarifa
                st.write("Distribución Porcentual por Tipo de Tarifa:")
                df_display = df_consulta[['Etiqueta', 'Valor Numerico', 'Unidad']].rename(columns={
                    'Etiqueta': 'Tipo de Tarifa',
                    'Valor Numerico': 'Porcentaje',
                    'Unidad': 'Unidad'
                })
                # Formatear el porcentaje a dos decimales
                df_display['Porcentaje'] = df_display['Porcentaje'].round(2)
                st.dataframe(df_display, hide_index=True)

            elif id_consulta == 5:
                # C5: Categoría de Distancia.
                st.write("Conteo de Viajes por Categoría de Distancia:")
                df_display = df_consulta[['Etiqueta', 'Valor Numerico', 'Unidad']].rename(columns={
                    'Etiqueta': 'Categoría de Distancia',
                    'Valor Numerico': 'Conteo de Viajes',
                    'Unidad': 'Unidad'
                })
                # Convertir a entero para mejor lectura
                df_display['Conteo de Viajes'] = df_display['Conteo de Viajes'].astype(
                    int)
                st.dataframe(df_display, hide_index=True)

            # Espacio al final de cada consulta
            st.markdown("---")

    except Exception as e:
        # Si la carga fue exitosa pero la extracción falló
        st.error(
            "Error (Fallo de Extracción): Se encontró un error al procesar los datos del CSV. Revise las etiquetas y el formato."
        )
        st.exception(e)

elif opcion == "6. Análisis exploratorio de datos":

    st.header("Análisis exploratorio de datos")

    # Grafico de cantidad de viajes por hora del dia

    st.subheader("Cantidad de viajes por hora del día")

    # Filtro
    dias = df['day_of_week'].unique()
    dias_ordenados = ['Monday', 'Tuesday',
                      'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dias = [d for d in dias_ordenados if d in dias]
    dias_seleccionado = st.selectbox("Selecciona el día de la semana:", dias)

    df_filtrado = df[df['day_of_week'] == dias_seleccionado]

    # Calcular viajes por hora
    viajes_hora = trips_per_hour(df_filtrado)

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

    # Filtro horario
    st.markdown("### 🔍 Filtros de visualización para ambos Mapas")
    hora_min, hora_max = st.slider(
        "Selecciona el rango horario (según hora de recogida y llegada):",
        0, 23, (0, 23)
    )

    df_filtrado = df[
        (df['tpep_pickup_datetime'].dt.hour >= hora_min) &
        (df['tpep_pickup_datetime'].dt.hour <= hora_max)

    ]

    st.subheader("Mapa del Total de Viajes por Zona de Recogida")

    from utils import trips_per_zone
    zonas, geojson = trips_per_zone(df_filtrado)

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
    zonas_drop, geojson_drop = trips_per_dropoff_zone(df_filtrado)

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


elif opcion == "7. Análisis Estadístico":
    st.header("Análisis Estadístico")
    st.write("En esta sección se lleva a cabo un análisis estadístico de los datos.")

elif opcion == "8. Conclusiones":
    st.header("Conclusiones")
    st.write(
        "En esta sección se presentan las conclusiones derivadas del análisis realizado.")

elif opcion == "9. Bibliografías":
    st.header("Bibliografias")
