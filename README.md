# ANÁLISIS DE LA DEMANDA DE TAXIS EN NEW YORK - DICIEMBRE 2019
# PLANTEAMIENTO DEL PROBLEMA
__La movilidad urbana es uno de los ejes más importantes para el funcionamiento eficiente de una gran ciudad. En metrópolis como Nueva York, el servicio de taxis juega un rol crucial en el transporte diario de millones de personas.
A lo largo del día, la demanda de taxis no es uniforme: varía según la hora, el día de la semana y la zona geográfica. Estas variaciones reflejan patrones sociales, económicos y de comportamiento urbano (por ejemplo, desplazamientos laborales en horas punta, actividades nocturnas o turismo).
  Este proyecto busca analizar la demanda de taxis en la ciudad de Nueva York durante 2019, con enfoque en patrones horarios y geográficos, utilizando herramientas estadísticas y computacionales modernas.__

# OBJETIVO GENERAL 
__Analizar la distribución temporal y espacial de la demanda de taxis en Nueva York durante el año 2019, para identificar zonas y horarios de alta demanda que puedan aportar conclusiones útiles desde el punto de vista estadístico y urbano.__

# BASE DE DATOS: NYC TAXI TRIPS 2019 (KAGGLE) 🛢
__Este dataset proviene de la New York City Taxi & Limousine Commission (TLC) y está disponible en Kaggle. URL: https://www.kaggle.com/datasets/dhruvildave/new-york-city-taxi-trips-2019 . Contiene información detallada de millones de viajes en taxi durante 2019.__
# CÓMO UTILIZAR? ✍🏻
__1️⃣ Clonar el Repositorio__

```bash
git clone https://github.com/RonaldManeiro/nyc-taxi-demanda-2019.git
cd nyc-taxi-demanda-2019 
```
__2️⃣ Instalar las dependencias 👨🏼‍💻__
```bash
pip install -r requirements.txt
```
__3️⃣ Cargar los datos originales 💾__

La base de datos original (`2019-12.sqlite`) debe colocarse en las siguiente ruta para que los *notebooks* y la aplicación funcionen correctamente.

> **Nota:** Estas carpetas (`data/raw/` y `data/processed/tripdata_clean.csv`) debido al tamaño de la base de datos, se ignoran en Git, por lo que debes colocar los archivos manualmente después de la clonación.

| Archivo | Ruta de Destino | Contenido |
| :--- | :--- | :--- |
| **`2019-12.sqlite`** | `data/raw/` | El *dataset* inicial. |

__4️⃣ Ejecutar los Notebooks__

Debes ejecutar los *notebooks* en orden. Este proceso es **esencial** porque genera los archivos procesados que consumirán **Power BI** y la aplicación **Streamlit**.
* **`exploracion_inicial.ipynb`**: Inspecciona la estructura inicial de los datos y realiza el análisis preliminar.
* **`02_depuracion_datos.ipynb`**:
    * Carga y limpia el *dataset* de 6.6M de filas.
    * **Genera el archivo grande** (`tripdata_clean.csv`) en `data/processed` para Power BI.
* Por último debes ejecutar el archivo (`tripdata_sample.py`) que está en (`app/`) para generar la muestra representativa de la base de datos que utilizará la aplicacion **Streamlit**. Este sample se generará en (`data/processed/`) con el nombre de (`tripdata_sample.csv`).

__5️⃣ Ejecutar la aplicación__
```bash
streamlit run app.py
```
**Siguiendo estos pasos, podrás ejecutar NYC-Taxi-Demanda-2019 ✅**
# HERRAMIENTAS/LIBRERIAS UTILIZADAS 📊
__• Powerbi • Python • Sqlite • Pandas • Numpy • Streamlit • Seaborn • Matplotlib.pyplot • Jupyter • Statsmodels__

# Visita nuestra app 💪
https://nyc-taxi-demanda-2019.streamlit.app/
# Proyecto desarrollado por
👤 Ronald Maneiro 

👤 Alejandro Vegas

👤 Carmen Briceño 

👤 Maria Herrera 
 
