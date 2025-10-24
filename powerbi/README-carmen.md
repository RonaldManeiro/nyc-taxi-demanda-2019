#  Modulo Resumen General — Proyecto NYC-Taxi-DEMANDA NYC 2019 (1,000,000 registros)

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

# Módulo: Análisis Económico

Este módulo presenta un conjunto de métricas y visualizaciones orientadas al análisis económico de los viajes en taxi, aplicando conceptos estadísticos como promedio, mediana, desviación estándar, composición del ingreso y eficiencia por ruta. El objetivo es identificar patrones de rentabilidad, comportamiento de pago y distribución de ingresos.
Se calcularon medidas de tendencia central (media, mediana) y dispersión (desviación estándar) para variables económicas clave. Estas permiten caracterizar el comportamiento general de los ingresos por viaje.

- Promedio tarifa base (`Promedio Tarifa Base`)
- Mediana tarifa base (`Mediana Tarifa Base`)
- Desviación estándar (`Desviación Tarifa Base`)
- Promedio propina (`Promedio Propina`)
- % de viajes con propina (`Porcentaje Viajes con Propina`)


### Histograma de tarifas base

Se creó una columna calculada `Rango Tarifa Base` que agrupa los valores de `fare_amount` en cinco rangos definidos. Esta clasificación permite visualizar la distribución de tarifas mediante un gráfico de columnas, facilitando la identificación de patrones y valores frecuentes.

## Ganancia económica por ruta

La columna `Ruta` representa el trayecto entre zona de origen y destino (ej. "48 → 48"). Se utilizó como categoría para agrupar los ingresos (`total_amount`) y calcular la ganancia total por trayecto. También se puede calcular la ganancia promedio por pasajero, dividiendo el ingreso total entre la cantidad de pasajeros por ruta.



### Gráfico de Torta: Total cobrado por Día de la Semana

Visualiza la distribución del ingreso total (`total_amount`) por día (`DíaSemana`). Permite identificar qué días concentran mayor actividad económica.

- **Valores destacados**:
  - Viernes: 229,72 mil
  - Jueves: 212,94 mil
  - Martes: 203,72 mil

---

###  Gráfico de Barras: Total de Viajes por Rango de Tarifa Base

Segmenta los viajes según rangos de tarifa base (`fare_amount`) y muestra la cantidad total de viajes en cada rango. Útil para identificar la frecuencia de tarifas bajas, medias y altas.

- **Rangos destacados**:
  - 50–100 mil: 0,40 mil viajes
  - 100–150 mil: 0,38 mil viajes

###  Gráfico de Barras: Ganancia por Ruta

Agrupa el ingreso total por trayecto (`Ruta`), representado como combinación de zona de origen y destino. Permite identificar las rutas más rentables.

 **Ejemplo de rutas destacadas**:
  - “48 → 48”: 150 mil
  - “68 → 68”: 120 mil

  ### Objetivo del modulo
- Evaluar la eficiencia económica por pasajero y por ruta.
- Identificar días y trayectos con mayor rentabilidad.
- Analizar la composición del ingreso total por viaje.
- Visualizar el comportamiento de pago voluntario (propinas).

### Modulo Analis por Zonas 

Relaciones bloqueadas por cardinalidad: se resolvió usando LOOKUPVALUE y CALCULATE + FILTER.
Visualizaciones de mapa deshabilitadas: se activaron en configuración global de Power BI.
Falta de coordenadas geográficas: se utilizó geolocalización automática por nombre de zona.
Carga masiva de datos: se optimizó el modelo para manejar más de 1 millón de registros sin pérdida de rendimiento.

### Recomendaciones futuras
Incorporar coordenadas geográficas para mejorar precisión en mapas.
Agregar análisis por tipo de tarifa o método de pago.
Automatizar la carga mensual de nuevos datos.
Explorar visualizaciones avanzadas como Sankey para rutas.