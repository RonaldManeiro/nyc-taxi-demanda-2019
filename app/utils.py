from pathlib import Path
import pandas as pd

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
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
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
