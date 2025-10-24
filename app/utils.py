from pathlib import Path
import pandas as pd
import json

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]


def get_processed_path(filename="tripadata_sample.csv"):
    """
    Devuelve la ruta completa al archivo dentro de data/processed.
    """
    return BASE_DIR / "data" / "processed" / filename


def load_data(filename="tripdata_sample.csv"):
    """
    Carga el CSV limpio desde data/processed como DataFrame. 
    """
    path = get_processed_path(filename)
    df = pd.read_csv(path)
    return df


def preprocess_data(df):
    df['tpep_pickup_datetime'] = pd.to_datetime(
        df['tpep_pickup_datetime'], errors='coerce')
    df['tpep_dropoff_datetime'] = pd.to_datetime(
        df['tpep_dropoff_datetime'], errors='coerce')

    # Columna con el dia de la semana (lunes=0, domingo=6)
    df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()
    return df


def trips_per_hour(df):
    df['hour'] = df['tpep_pickup_datetime'].dt.hour
    return df.groupby('hour').size().reset_index(name='num_viajes')


def categorize_distance(df):
    conditions = [
        (df['trip_distance'] < 2),
        (2 <= df['trip_distance']) & (df['trip_distance'] < 10),
        (df['trip_distance'] > 10)
    ]
    labels = ['Corto', 'Medio', 'Largo']
    df['distance_category'] = pd.cut(
        df['trip_distance'], bins=[-1, 2, 10, 10000], labels=labels)
    return df


def avg_trip_duration_per_hour(df):
    """
    Calcula la duracion promedio (en minutos) de los viajes por hora del dia. 
    """
    # Aseguramos que la fecha este en formato datetime
    if not pd.api.types.is_datetime64_any_dtype(df['tpep_pickup_datetime']):
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    # Extraemos la hora
    df['hour'] = df['tpep_pickup_datetime'].dt.hour

    # Calculamos duracion promedio
    duracion_hora = (
        df.groupby('hour')['trip_duration_min']
        .mean()
        .reset_index()
        .rename(columns={'trip_duration_min': 'duracion_promedio_min'})
    )
    return duracion_hora


def trip_distance_distribution(df):
    """
    Devuelve una version filtrada del DataFrame para analizar la distribucion de las distancias de los viajes, elminando valores extremos.
    """
    # Eliminamos valores extremos
    df_filtered = df[df['trip_distance'] <= 150]
    return df_filtered


def payment_distribution(df):
    """
    Calcula la distribucion de los metodos de pago.
    """
    mapping = {
        1: 'Tarjeta de crédito',
        2: 'Efectivo',
        3: 'Sin cargo',
        4: 'Reclamado',
        5: 'Desconocido',
        6: 'Anulado'
    }
    df["payment_type"] = df["payment_type"].map(mapping)
    pagos = df["payment_type"].value_counts().reset_index()
    pagos.columns = ["Método de pago", "Cantidad de viajes"]
    pagos["Porcentaje"] = pagos["Cantidad de viajes"] / \
        pagos["Cantidad de viajes"].sum() * 100
    return pagos


def fare_tip_relation(df):
    """
    Devuelve las columnas necesarias para analizar la relacion entre tarifa total y propina.
    Elimina valores atipicos y viajes con propina total cero.
    """
    df_filtered = df[(df['total_amount'] > 0) & (df['tip_amount'] >= 0)]
    df_filtered = df_filtered[df_filtered['tip_amount'] <= 100]
    df_filtered = df_filtered[df_filtered['total_amount'] <= 500]
    return df_filtered[['total_amount', 'tip_amount']]


def trips_per_zone(df, filename_geojson="taxi_zones.geojson"):
    """
    Calcula el total de viajes por zona de recogida y devuelve un DataFrame combinado con el GeoJson.
    """
    # Contar viajes por zona
    zonas = df.groupby("pulocationid").size().reset_index(name="Total_viajes")

    # Leer el lookup para obtener nombre y borough
    lookup_path = BASE_DIR / "data" / "taxi_zone_lookup.csv"
    lookup = pd.read_csv(lookup_path)
    zonas = zonas.merge(lookup, left_on="pulocationid",
                        right_on="LocationID", how="left")

    # Cargar el GeoJSON
    geojson_path = BASE_DIR / "data" / filename_geojson
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson = json.load(f)

    zonas.rename(columns={"pulocationid": "location_id"}, inplace=True)
    return zonas, geojson


def trips_per_dropoff_zone(df, filename_geojson="taxi_zones.geojson"):
    """
    Calcula el total de viajes por zona de llegada (dropoff) y devuelve un DataFrame combinado con el Geojson.
    """
    # Contar viajes por zona de llegada
    zonas = df.groupby("dolocationid").size().reset_index(name="Total_viajes")

    # Leer el lookup para obtener nombre y borough
    lookup_path = BASE_DIR / "data" / "taxi_zone_lookup.csv"
    lookup = pd.read_csv(lookup_path)
    zonas = zonas.merge(lookup, left_on="dolocationid",
                        right_on="LocationID", how="left")

    # Cargar el Geojson
    geojson_path = BASE_DIR / "data" / filename_geojson
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson = json.load(f)

    zonas.rename(columns={"dolocationid": "location_id"}, inplace=True)
    return zonas, geojson
