#  Notas técnicas — Proyecto Taxi NYC 2019

Este archivo contiene observaciones técnicas, decisiones tomadas y oportunidades de mejora durante el desarrollo del dashboard "Resumen General".

---

##  Decisiones técnicas

- Se utilizó una muestra de **1,000,000 registros** para garantizar representatividad sin comprometer el rendimiento.
- Se aplicó `Table.FirstN(...)` en Power Query para limitar la carga inicial.
- Se separaron fecha y hora en columnas distintas para facilitar segmentaciones temporales.
- Se renombraron todas las columnas en español para mejorar la legibilidad del modelo.

##  Pruebas realizadas

- Se probó el rendimiento del modelo con 50K, 500K y 1M de registros.
- Se validó que los gráficos de dispersión no agregaran valores por defecto.
- Se verificó que las medidas DAX funcionaran correctamente con filtros por hora, día y método de pago.


##  Problemas resueltos

- Visualizaciones que no mostraban puntos por agregación automática → solucionado usando campos sin agregación.
- Columnas con nombres ambiguos → renombradas para claridad.
- Códigos numéricos en `Método de pago` → reemplazados por texto legible.

##  Mejoras futuras

- Agregar análisis por zonas geográficas (`pulocationid`, `dolocationid`).
- Incorporar mapas interactivos en la pestaña “Análisis geográfico”.
- Documentar transformaciones específicas por pestaña (económico, segmentación).
- Automatizar la carga de datos desde una fuente externa.

