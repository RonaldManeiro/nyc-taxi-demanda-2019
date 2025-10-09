# ANÁLISIS DE LA DEMANDA DE TAXIS EN NEW YORK - DICIEMBRE 2019

# PLANTEAMIENTO DEL PROBLEMA
La movilidad urbana es uno de los ejes más importantes para el funcionamiento eficiente de una gran ciudad. En metrópolis como Nueva York, el servicio de taxis juega un rol crucial en el transporte diario de millones¡ de personas.
A lo largo del día, la demanda de taxis no es uniforme: varía según la hora, el día de la semana y la zona geográfica. Estas variaciones reflejan patrones sociales, económicos y de comportamiento urbano (por ejemplo, desplazamientos laborales en horas punta, actividades nocturnas o turismo).
  Este proyecto busca analizar la demanda de taxis en la ciudad de Nueva York durante 2019, con enfoque en patrones horarios y geográficos, utilizando herramientas estadísticas y computacionales modernas.

# OBJETIVO GENERAL 
Analizar la distribución temporal y espacial de la demanda de taxis en Nueva York durante el mes de diciembre del año 2019, para identificar zonas y horarios de alta demanda que puedan aportar conclusiones útiles desde el punto de vista estadístico y urbano.

# OBJETIVO ESPECIFICOS
- Procesar y limpiar el dataset para obtener un subconjunto representativo.
- Identificar horas pico y zonas de alta demanda.
- Visualizar patrones mediante dashboards en Power BI.
- Desarrollar una app interactiva en Streamlit.
- Aplicar estadística descriptiva para interpretar los resultados.

# BASE DE DATOS: NYC TAXI TRIPS 2019 (KAGGLE)
Este dataset proviene de la New York City Taxi & Limousine Commission (TLC) y está disponible en Kaggle. Contiene información detallada de millones de viajes en taxi durante el mes de diciembre del 2019.

# ESTRUCTURA DEL PROYECTO

- `data/`: Datos crudos y procesados.
- `notebooks/`: Análisis exploratorio, visualizaciones y modelado.
- `sql/`: Consultas para extracción y transformación de datos.
- `powerbi/`: Dashboards interactivos para visualización.

# FUNDAMENTOS ESTADISTICOS

Se aplican técnicas de **estadística descriptiva** para resumir y visualizar la demanda:

- Medidas de tendencia central: media, mediana, moda.
- Medidas de dispersión: desviación estándar, rangos.
- Histogramas, heatmaps y líneas temporales.
- Agrupamientos por hora, día y zona.


# METODOLOGIA A USAR

1. **Obtención y limpieza de datos**
   - Descarga desde Kaggle.
   - Filtrado de columnas relevantes.
   - Selección de enero 2019.
   - Limpieza de fechas, distancias y nulos.

2. **Análisis exploratorio**
   - Extracción de variables horarias y geográficas.
   - Agrupamiento por zona y hora.

3. **Visualización interactiva**
   - Dashboard en Power BI con mapas y gráficos.
   - Filtros por día de la semana y zona.

4. **Aplicación web**
   - App en Streamlit con selector de fecha/hora.
   - Gráficos dinámicos y filtros interactivos.

5. **Conclusiones estadísticas**
   - Identificación de patrones de demanda.
   - Redacción de hallazgos útiles.
  
# HERRAMIENTAS/LIBRERIAS UTILIZADAS
__• Powerbi • Python • Sqlite • Pandas • Numpy • Streamlit • Seaborn • Matplotlib.pyplot_

# RESULTADOS ESPERADOS
- Dataset limpio y manejable.
- Dashboard con picos horarios y mapas de demanda.
- App funcional en Python para exploración interactiva.
- Consultas SQL para análisis por zona y hora.
- Conclusiones claras sobre patrones de movilidad urbana.

# DELIMITACION DEL PROYECTO
- Se analiza solo el mes de diciembre de 2019.
- Se usan columnas temporales y geográficas básicas.
- No se abordan tarifas, duración ni correlaciones complejas.
