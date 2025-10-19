from pathlib import Path
import pandas as pd

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]


def get_processed_path(filename="tripdata_clean.csv"):
    """
    Devuelve la ruta completa al archivo dentro de data/processed.
    """
    return BASE_DIR / "data" / "processed" / filename


def load_data(filename="tripdata_clean.csv"):
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
    return df.groupby('hour').size()


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
