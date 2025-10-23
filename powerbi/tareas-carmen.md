#  Registro de tareas — Proyecto Taxi NYC 2019

Este documento resume las tareas realizadas durante el desarrollo del dashboard "Resumen General", incluyendo fechas aproximadas, avances técnicos y validaciones.

---

##  Cronología de trabajo

- **Oct 15–17**: Importación y exploración inicial del CSV
- **Oct 18–19**: Transformaciones en Power Query (limpieza, renombrado, extracción de hora)
- **Oct 20**: Creación de medidas DAX y visualizaciones principales
- **Oct 21**: Validación de métricas y segmentaciones
- **Oct 22**: Documentación técnica y organización del repositorio

---

## Tareas completadas

- Importación de 1,000,000 registros desde `tripdata_clean.csv`
- Transformaciones completas en Power Query documentadas en `powerquery-transformaciones.md`
- Creación de medidas DAX documentadas en `dax-resumen-general.md`
- Construcción del dashboard “Resumen General” con:
  - Tarjetas de métricas clave
  - Gráfico de dispersión
  - Gráfico de barras por hora
  - Gráfico de barras por método de pago
  - Gráfico circular por día de la semana
- Organización del repositorio con carpetas técnicas (`dax/`, `powerquery/`, `screenshots/`)
- Documentación completa en Markdown para GitHub


##  Validaciones

- Coherencia entre medidas DAX y visualizaciones
- Rendimiento aceptable con 1M de registros
- Legibilidad de nombres y formato de hora
- Reproducibilidad del modelo desde cero

