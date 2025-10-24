--consulta 1: Calcula la distancia promedio y el tiempo promedio de viaje en minutos para todos los viajes realizados en 2019. 

SELECT 
	round(avg(trip_distance),2) as distancia,
	round(avg(trip_duration_min),2) as minutos
FROM tripdata_clean

-- consulta 2: Determina el método de pago más común y cuántos viajes lo usaron. 

SELECT
    CASE payment_type
        WHEN 1 THEN 'tarjeta de crédito'
        WHEN 2 THEN 'efectivo'
        WHEN 3 THEN 'sin cargo'
        WHEN 4 THEN 'en disputa'
        WHEN 5 THEN 'desconocido'
        WHEN 6 THEN 'viaje cancelado'
    END AS metodo_de_pago,
    COUNT(payment_type) AS cantidad_viajes
FROM
    tripdata_clean
GROUP BY
    payment_type
ORDER BY
    cantidad_viajes DESC
LIMIT 1;

--consulta 3: Calcula la propina promedio según el tipo de pago pero sólo para viajes donde la propina fue mayor que 0. 

SELECT
    CASE payment_type
        WHEN 1 THEN 'tarjeta de crédito'
        WHEN 2 THEN 'efectivo'
        WHEN 3 THEN 'sin cargo'
        WHEN 4 THEN 'en disputa'
        WHEN 5 THEN 'desconocido'
        WHEN 6 THEN 'viaje cancelado'
        ELSE 'Otro/No definido'
    END AS metodo_de_pago,
    ROUND(AVG(tip_amount), 2) AS propina_promedio
FROM
    tripdata_clean
WHERE
    tip_amount > 0
GROUP BY
    metodo_de_pago 
ORDER by 
	metodo_de_pago DESC

--consulta 4: Muestra el porcentaje de viajes correspondientes a cada tipo de tarifa, ordenado de mayor a menor participación. 

SELECT
    CASE ratecodeid
        WHEN 1 THEN 'Tarifa estandar'
        WHEN 2 THEN 'JFK'
        WHEN 3 THEN 'Newark'
        WHEN 4 THEN 'Nassau o Westchester'
        WHEN 5 THEN 'Tarifa negociada'
        WHEN 6 THEN 'Tarifa grupal'
        ELSE 'Desconocido'
    END AS tipo_de_tarifa,
    COUNT(ratecodeid) AS total_viajes,
    ROUND(
        CAST(COUNT(ratecodeid) AS REAL) * 100.0 / (SELECT COUNT(*) FROM tripdata_clean),
        2
    ) AS porcentaje_participacion
FROM
    tripdata_clean
GROUP BY
    tipo_de_tarifa
ORDER BY
    porcentaje_participacion DESC; 
	
--Clasifica los viajes según su distancia (Trip_distance) en tres categorías: 
--Corto: menos de 2 millas 
--Medio: entre 2 y 10 millas 
--Largo: más de 10 millas 
--Muestra cuántos viajes hay en cada categoría. 

SELECT
    CASE
        WHEN trip_distance < 2 THEN 'Corto'                 
        WHEN trip_distance BETWEEN 2 AND 10 THEN 'Medio'     
        WHEN trip_distance > 10 THEN 'Largo'                  
        ELSE 'Distancia Desconocida'                        
    END AS categoria_distancia,
    
    COUNT(*) AS cantidad_viajes
FROM
    tripdata_clean
GROUP BY
    categoria_distancia
ORDER BY
    cantidad_viajes DESC;






