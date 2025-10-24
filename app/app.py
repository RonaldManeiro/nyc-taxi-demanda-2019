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
        "7. Análisis y Conclusiones",
        "8. Bibliografías"
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
    
    st.write("Al incrementar la necesidad del ser humano de recorrer largas distancias para llegar a diferentes sitios en el mundo, no tardaron en aparecer los primeros inventos que permitieron y facilitaron: Tanto el desplazamiento de personas de un lugar a otro, como el desarrollo urbano y social de las ciudades cercanas a estos medios de transporte. Convirtiéndose la movilidad urbana en uno de los ejes más importantes para el funcionamiento eficiente de una gran ciudad. En el caso de las metrópolis como Nueva York, el servicio de taxis juega un papel crucial en el transporte diario de millones de personas al disminuir el uso de transportes privados (sobre todo cuando una persona no posee su propio automóvil por cuestiones personales, o desea evitar el estrés que produce el conducir en el tráfico). Además de que el servicio de taxis proporciona una opción rápida y segura de moverse alrededor de una zona determinada, siendo una de las primeras opciones que buscan las personas a la hora de viajar.")

    st.write("A lo largo de un día, la demanda de taxis no es uniforme ya que existen múltiples variables que pueden interferir o beneficiar al momento de prestar sus servicios al público: Algunas de ellas pueden ser la hora en que se solicita al taxista, el clima que puede cambiar sin previo aviso, el día de la semana (además de encontrarse en una época específica del año, como las vacaciones de verano o de Navidad) o la zona geográfica donde se realizará la ruta solicitada por el cliente. Estas variaciones se ven reflejadas en patrones sociales, económicos y de comportamiento urbano (por ejemplo; desplazamientos laborales en horas punta, actividades nocturnas o turismo).")
    
    st.write("Cuando se tiene una mejor comprensión de estos patrones y sus efectos durante las jornadas diarias de los conductores, tanto las empresas como las autoridades de transporte y cada uno de sus empleados involucrados pueden tomar decisiones más informadas como:")
    
    st.markdown("""
    - Optimizar la distribución de taxis durante las horas pico 
    - Diseñar políticas de movilidad más eficientes 
    - Reducir tiempos de espera para usuarios 
    """)
    
    st.write("De este modo: Se busca con este proyecto analizar la demanda de taxis en la ciudad de Nueva York durante el mes de diciembre del año 2019, con enfoque en patrones horarios y geográficos, utilizando herramientas estadísticas y computacionales modernas.")

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

    st.write("Las Bases Teóricas se encuentran conformadas por los conceptos, proposiciones y filosofías que buscan ofrecer una explicación detallada y precisa sobre el problema de estudio. Para este caso, las Bases Teóricas que respaldan este análisis es la información a continuación:")

    st.write("A medida que fue incrementando la necesidad del ser humano de explorar y llegar a diferentes sitios del mundo que se encuentran a largas distancias del punto de origen (resultando cada vez más difícil y fatigador cumplir ese objetivo únicamente viajando a pie), no tardaron en aparecer los primeros inventos que permitieran facilitar el desplazamiento de un lugar a otro (independientemente de si el camino elegido cubriera o no muchos kilómetros por recorrer). Y con la aparición de la primera rueda que facilitó el comercio y la comunicación entre diferentes culturas, se obtuvo un avance positivo en el desarrollo de tecnologías y sistemas de transporte que cumplieran el objetivo esperado. Reduciendo el tiempo de traslado y facilitando la movilidad activa (caminar o bicicleta) de la gente, convirtiéndose con el transcurso del tiempo en un catalizador de desarrollo urbano y social para los pueblos y ciudades.")

    st.write("De este modo, la introducción de transportes (tanto públicos como privados) a la vida cotidiana de las personas se convirtió en un factor clave para el crecimiento de las grandes ciudades al permitir la generación de empleos en diversas áreas (tanto en el manejo de los transportes como en el mantenimiento de éstos) y, por ende, acelerando el crecimiento de las ciudades cercanas como fue en el caso de las zonas cercanas a estas líneas de transporte. Por ejemplo: La construcción del primer ferrocarril en Inglaterra permitió la generación de empleos al tener una enorme capacidad de transporte grandes cantidades de carga y de personas, así como el crecimiento de las ciudades cercanas a las líneas ferroviarias gracias al impacto positivo que tuvo en el aumento de la eficiencia del comercio. Además de permitir el acceso a empleo, educación y servicios básicos de poblaciones vulnerables.")
    
    st.write("Entonces; se tiene que la Movilidad Urbana es el conjunto de desplazamientos de personas y mercancías dentro de un área urbana y las condiciones en las que estos viajes se realizan, abarcando en este concepto todos los modos de transporte (público, privado, taxis/servicios de viaje compartido) y su impacto en la calidad de vida, el medio ambiente y la eficiencia económica de la ciudad.")

    st.write("Entre los medios de transporte que se usan hoy en día en la sociedad, se encuentran los servicios de Taxi; vehículos de alquiler que incluyen un conductor profesional que se contrata para transportar pasajeros a uno o varios destinos elegidos por ellos (el cliente puede indicar el punto de partida y el de llegada en su viaje). La palabra «taxi», según el Diccionario de la lengua española, es una forma abreviada de la palabra «taxímetro», que a su vez deriva del griego τάξις, «tasa» y μέτρον, que significa «medida». Usualmente, los lugares donde se recoge y se deja al pasajero se deciden por el proveedor (oferente), mientras que el usuario (demandante) los determina.")

    st.write("A diferencia de los otros tipos de transporte de personas, como son las líneas del metro, tranvía o del autobús, el servicio ofrecido por el taxi se caracteriza por ser «puerta a puerta»; es decir, el conductor (al cual se le conoce como “taxista”) recoge a la persona en el punto donde se encuentra y la lleva al lugar deseado por la misma. Sin mencionar que la tarifa se calcula generalmente a través de un taxímetro, aunque suelen estar reguladas por la autoridad local y se suele determinar el precio a pagar antes o después de realizar el recorrido solicitado.")

    st.write("Los tipos de taxis se pueden clasificar en")

    st.markdown("""
    - **Taxi convencional:** es el tipo más común de taxi que se encuentra en la mayoría de las ciudades. Estos taxis suelen ser de color amarillo o negro y están disponibles en las paradas designadas o se pueden llamar por teléfono. Se suelen encontrar en la mayoría de las áreas urbanas y no es necesario reservar con anticipación, además de que tienen en su equipamiento un taxímetro para calcular la tarifa del viaje en función de la distancia recorrida y el tiempo transcurrido. 
    - **Taxis compartido:** es una opción económica y ecológica para moverse ya que (tal y como lo indica su nombre) se puede compartir el viaje con otros pasajeros que se dirigen en la misma dirección. Unas de las ventajas que ofrecen este servicio de taxis es una menor emisión de gases contaminantes al compartir un vehículo con otros pasajeros. 
    - **Taxis adaptado:** este tipo de taxis se encuentran diseñados para personas con discapacidades físicas o movilidad reducida, equipados con rampas o elevadores para facilitar el acceso de sillas de ruedas y otros dispositivos de movilidad. 
    - **Taxis ecológico:** aquel que utiliza tecnologías y combustibles más limpios para reducir las emisiones de carbono y minimizar su impacto en el medio ambiente. Suelen ser vehículos híbridos o eléctricos que funcionan con baterías recargables, por lo que no emiten gases de escape nocivos y son más eficientes en el consumo de combustible. 
    """)
    
    st.write("En Nueva York, los taxis se dividen en dos categorías: amarillo y verde, y son símbolos de la ciudad ampliamente reconocibles. Aunque puede parecer una opción de un precio elevado a la hora de moverse por la cuidad de Nueva York, en realidad los taxis pueden una opción práctica ya que son un medio de transporte moderno y limpio, tienen instalado un GPS a la vista tanto del conductor como del pasajero (lo que permite una visualización clara y precisa del viaje), y son una opción fiable a la hora de moverse por la noche en la ciudad.")

    st.write("Un detalle resaltante de los vehículos de taxi en esta ciudad es que deben tener una “Medalla de Taxi”: Un permiso transferible que permite a un conductor operar un taxi en la ciudad, siendo un sistema creado en 1937 para regular la oferta de taxis y limitar el número de licencias. Desde entonces, el gobierno de Nueva York ha regulado el precio de las medallas, que fluctúan casi diariamente. Para el año 2007, todas las inscripciones en los taxis amarillos fueron rediseñados y se volvieron fáciles de identificar con el número de la medalla seguido de un patrón ajedrezado en la parte trasera de ambos lados, un panel futurista con la tarifa en las puertas traseras y un logo retro con la inscripción **NYC Taxi** en las puertas delanteras con una T amarilla inscrita en un círculo negro (eliminando la parte “axi” en el año 2012 y dejando únicamente el logo NYC y la T en un círculo).")

    st.write("La principal diferencia entre los taxis amarillos y verdes radica en las zonas donde están autorizados para recoger pasajeros:")

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

elif opcion == "7. Análisis y Conclusiones":
    st.header("Análisis y Conclusiones")
    
    st.write("Incluso cuando no se trabajó con la base de datos completa del mes de diciembre (debido a la enorme demanda que iba a significar para la capacidad de las computadoras), se obtuvieron unos resultados significativos del subconjunto extraído al limpiar y procesar la BBDD:")

    st.write("De acuerdo con los gráficos generados por medio de Python, se puede observar que las horas pico de trabajo sí pueden llegar a influir en la solicitud de servicios de taxis por los clientes, ya que en el gráfico de barras de “Distribución Porcentual de viajes según la hora del día” el porcentaje es mayor entre las 15 y 20 horas del día. Con la barra de “Horas del día = 18” la mayor en altura con un 6,3484% de viajes en total, mientras que la barra de menor altura es la de “Horas del día = 4” con un 0,7444% de viajes en total. Esto indica que los taxis en Nueva York sí son una opción fiable para moverse por la ciudad durante las horas de la noche, siendo probablemente las horas donde hay un mayor desplazamiento de personas por las calles al poder disfrutar del entretenimiento nocturno que ofrecen al público.")

    st.write("También se puede apreciar que el número de viajes no se encuentra distribuido uniformemente por toda la ciudad de Nueva York: Aunque no se puede asegurar por completo al ser una muestra pequeña con la que se trabajó, hay un número mayor de viajes en el distrito de Manhattan, teniendo como cifra mayor un total de 23,925 km recorridos aproximadamente cerca del centro del distrito, y la menor cifra fue un total de 40 metros recorridos alrededor de las fronteras del distrito. 	Esto no es de extrañar, ya que Manhattan es conocida por un distrito atractivo a los ojos de los turistas que pueden disfrutar de los teatros, diversos eventos culturales y otras atracciones turísticas (refutando lo dicho anteriormente sobre el aumento de la demanda de taxis durante la noche).")

    st.write("Además; se puede visualizar por medio de un gráfico circular generado en Power BI que, entre todos los días de la semana durante el mes de diciembre, los miércoles tuvieron una mayor demanda con un total de 301,18 mil cobrados de pasajeros. No se puede inferir mucho acerca del motivo por el cual hubo una mayor tendencia hacia este día de la semana, pero (al analizar en el gráfico que el total de ingresos fue en aumento desde el lunes hasta el miércoles) se puede teorizar que las jornadas de trabajo suelen ser mayores a inicios de semana y la exigencia va disminuyendo a medida que se acerca el fin de semana (ya que el viernes y el sábado son los únicos días de la semana que no se encuentran presentes en el gráfico). Por lo tanto: Una mayor necesidad de parte de las personas por llegar a tiempo a sus empleos, puede aumentar la demanda de taxis alrededor de una zona y hora en particular.")

    st.write("Entonces, aunque la base de datos elegida para la investigación no es de un tiempo presente; se hizo visible tanto la importancia que tienen las líneas de taxi en Nueva York como el hecho de que la toma de conciencia de esta información puede resultar crucial en la toma de decisiones para mejorar el rendimiento del negocio: Como aumentar el número de taxis en “puntos turísticos determinados”, o aumentar el número de conductores que se encuentran disponibles en horarios donde la movilización de las personas es significativamente mayor que en otros momentos del día.")

elif opcion == "8. Bibliografías":
    st.header("Bibliografias")
