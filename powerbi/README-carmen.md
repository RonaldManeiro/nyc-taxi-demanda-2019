# 📊 Resumen General — Proyecto Taxi NYC 2019 (1,000,000 registros)

Este módulo presenta una visión general del comportamiento de los viajes en taxi en Nueva York durante 2019, utilizando una muestra de **1,000,000 de registros**. Se construyó en Power BI y se documenta aquí como parte del repositorio técnico.

---

##  Métricas clave

| Métrica                                        | Valor estimado |
|------------------------------------------------|----------------|
| Promedio de distancia recorrida (millas)       | 202.99 millones|
| Promedio de tarifa base por viaje ($)          | 138.03         |
| Promedio de propina registrada (solo tarjeta)  | 191.83         |
| Suma de cantidad de pasajeros                  | 2.000.000      |
| Total de viajes analizados                     | 1,000,000      |


##  Visualizaciones principales

### 1. **Gráfico de dispersión: Total cobrado vs Distancia**
- **Eje X**: Distancia recorrida en millas
- **Eje Y**: Total cobrado al pasajero ($)
- **Detalles**: ID del viaje
- **Propósito**: Identificar relación entre distancia y monto cobrado, y detectar outliers.

### 2. **Gráfico de barras: Horas más demandadas**
- **Eje X**: Hora del día (formato AM/PM)
- **Eje Y**: Conteo de viajes
- **Propósito**: Visualizar picos de demanda por hora. Se observa alta actividad entre 7:00 AM y 9:00 AM, y entre 5:00 PM y 7:00 PM.

### 3. **Gráfico de barras: Método de pago más usado**
- **Categorías**: Tarjeta vs Efectivo
- **Valores**: Número de viajes
- **Resultado**: Tarjeta representa más del 90% de los pagos.

### 4. **Gráfico circular: Recuento por día de la semana**
- **Categorías**: Lunes a domingo
- **Valores**: Número de viajes
- **Hallazgo**: Domingo concentra una proporción significativa de viajes, lo que sugiere alta demanda en fines de semana.

---

##  Archivos relacionados

- `taxi_transformacion_2019-10-19.pbix`: versión principal del modelo Power BI con 1 millón de registros
- `screenshots/`: capturas del dashboard
- `powerquery/`: transformaciones aplicadas en Power Query
- `dax/`: fórmulas DAX utilizadas para columnas calculadas (ej. `HoraInicio`, `HoraInicioTexto`)
- `tareas-carmen.md`: tareas realizadas durante el desarrollo

---

##  Notas técnicas

- Se utilizó `Table.FirstN` para limitar la muestra a 1,000,000 registros desde el archivo CSV.
- Se creó la columna `HoraInicioTexto` con `FORMAT(..., "hh:mm AM/PM")` para mejorar la legibilidad en gráficos.
- Se validó que los campos en los gráficos de dispersión estén en modo **no agregado** para evitar agrupaciones erróneas.
- Se aplicaron filtros mínimos para mantener la representatividad de la muestra.
- Se optimizó el modelo para evitar congelamientos al manejar grandes volúmenes de datos.


##  Estado del módulo

 Finalizado  
 Última modificación: 22/10/2025  


##  Estructura del repositorio

Este repositorio contiene el desarrollo completo del dashboard “Resumen General” para el análisis de viajes en taxi en Nueva York durante 2019, utilizando una muestra de **1,000,000 registros**.


- `powerquery/`: Transformaciones aplicadas en Power Query
- `dax/`: Medidas DAX utilizadas en el modelo
- `screenshots/`: Capturas del dashboard
- `tareas-carmen.md`: Registro de tareas realizadas
- `notes.md`: Notas técnicas y decisiones tomadas
- `taxi_transformacion_2019-10-19.pbix`: Archivo principal del modelo Power BI
- `taxi_transformacion_v1.pbix`: Versión inicial de prueba


##  Visualizaciones principales

- Gráfico de dispersión: Total cobrado vs Distancia
- Gráfico de barras: Horas más demandadas
- Gráfico de barras: Método de pago más usado
- Gráfico circular: Viajes por día de la semana
- Tarjetas resumen con métricas clave


## Documentación técnica

- Transformaciones: [`powerquery-transformaciones.md`](powerquery/)
- Medidas DAX: [`dax-resumen-general.md`](dax/)
- Registro de tareas: [`tareas-carmen.md`](tareas-carmen.md)
- Notas técnicas: [`notes.md`](notes.md)

---

##  Estado del módulo

 Finalizado 
 Última modificación: 22/10/2025

