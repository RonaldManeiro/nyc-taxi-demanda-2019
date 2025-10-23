## Proyecto Taxi NYC 2019
Este documento describe las fórmulas DAX utilizadas en el modelo Power BI para construir la sección ## Resumen General ##  del dashboard. Las expresiones permiten calcular métricas clave, extraer componentes de fecha y hora, y facilitar la segmentación por variables categóricas.

## 1. Extracción de hora de inicio
DAX
HoraInicio = HOUR('tripdata_clean'[hora de inicio del viaje])
Extrae la hora (0 a 23) del campo hora de inicio del viaje.

Se usa para agrupar viajes por hora en el gráfico de barras de demanda horaria.

## 2. Formato legible de hora
DAX
HoraInicioTexto = FORMAT('tripdata_clean'[hora de inicio del viaje], "hh:mm AM/PM")
Convierte la hora en formato legible para el usuario.

Se utiliza como eje X en visualizaciones por hora.

## 3. Día de la semana
DAX
DiaSemana = FORMAT('tripdata_clean'[Fecha de inicio del viaje], "dddd")
Extrae el nombre del día (ej. lunes, martes).

Se usa para segmentar viajes por día en gráficos circulares o de barras.

## 4. Total de viajes
DAX
TotalViajes = COUNT('tripdata_clean'[IdViajes])
Cuenta el número total de viajes en la tabla.

Se muestra como tarjeta resumen en el dashboard.

## 5. Total por método de pago
DAX
TotalTarjeta = CALCULATE(COUNT('tripdata_clean'[IdViajes]), 'tripdata_clean'[Método de pago] = "Tarjeta de Crédito")
TotalEfectivo = CALCULATE(COUNT('tripdata_clean'[IdViajes]), 'tripdata_clean'[Método de pago] = "Efectivo")
Segmenta los viajes según el método de pago.

Se usa en el gráfico de barras de métodos más usados.

## 6. Promedios monetarios
DAX
PromedioPropina = AVERAGE('tripdata_clean'[Propina registrada $ (solo tarjeta)])
PromedioTarifaBase = AVERAGE('tripdata_clean'[Tarifa base del viaje $])
PromedioDistancia = AVERAGE('tripdata_clean'[Distancia recorrida en millas])
Calcula promedios clave para tarjetas resumen.

Se muestran en la parte superior del dashboard.

## 7. Total por día de la semana
DAX
ViajesPorDia = COUNTROWS(FILTER('tripdata_clean', 'tripdata_clean'[DiaSemana] = "domingo"))
Cuenta los viajes realizados en domingo.

Se usa para destacar días con mayor demanda.

## Notas Importantes
Todas las medidas están creadas como medidas DAX en el modelo.

Las expresiones están optimizadas para rendimiento con 1,000,000 registros.

Este documento forma parte de la carpeta dax/ del repositorio GitHub del proyecto Taxi NYC 2019.