#"Encabezados promovidos" = Table.PromoteHeaders(...)
#"Tipo cambiado" = Table.TransformColumnTypes(...)
Se convierten los nombres de columna.

Se asignan tipos adecuados (datetime, int64, number) para análisis.

 ## Extracción de fecha y hora
m
#"Columna duplicada" = Table.DuplicateColumn(...)
#"Fecha extraída" = Table.TransformColumns(...)
#"Hora extraída" = Table.TransformColumns(...)
Se duplican columnas de fecha para extraer la hora por separado.

Se renombran como Fecha de inicio del viaje, hora de inicio del viaje, etc.

## Renombrado de columnas técnicas
m
#"Columnas con nombre cambiado" = Table.RenameColumns(...)
Se renombran columnas como:

trip_distance → Distancia recorrida en millas

fare_amount → Tarifa base del viaje

tip_amount → Propina registrada (solo tarjeta)

total_amount → Total cobrado al pasajero

pulocationid → ID de zona de recogida

dolocationid → ID de zona de destino

ratecodeid → Código de tarifa aplicada

payment_type → Método de pago

## Conversión de tipos numéricos
m
Table.TransformColumnTypes(..., type number)
Se convierten columnas monetarias y de distancia a tipo number.

## Cálculos adicionales
m
Table.AddColumn(..., "Distancia recorrida Km", each [Distancia recorrida en millas]*1.60934)
Table.AddIndexColumn(..., "Índice", 1, 1, Int64.Type)
Se calcula la distancia en kilómetros.

Se agrega un índice para ordenar los viajes.

## Limpieza y codificación de valores
m
Table.ReplaceValue(..., "10", "Tarjeta de Crédito", ...)
Se reemplazan códigos numéricos por texto legible:

"10" → "Tarjeta de Crédito"

"20" → "Efectivo"

"30" → "Sin cargo"

"40" → "Disputa"

Se renombran columnas monetarias para incluir el símbolo $.

## Cálculo de hora redondeada
m
Time.StartOfHour(...)
Time.EndOfHour(...)
Se calcula la hora de inicio y fin redondeada a la hora completa.

Se eliminan columnas auxiliares.

## Renombrado final y filtrado
m
Table.RenameColumns(..., {"Total Viajes", "IdViajes"})
Table.RenameColumns(..., {"Total cobrado al pasajero $", "Total cobrado pasajeros $"})
Se renombra el índice como IdViajes.

Se renombra el monto total como Total cobrado pasajeros $.

Se aplica un filtro general para mantener estructura.

## Resultado final
La tabla final contiene:

Fechas y horas limpias

Variables monetarias y categóricas listas para visualización

Campos renombrados y ordenados

1,000,000 registros listos para análisis en Power BI