import pandas as pd
from pathlib import Path
import os

# Ruta base
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar dataset completo
db_path = BASE_DIR / "data" / "processed" / "tripdata_clean.csv"
df = pd.read_csv(db_path)

# Tomar muestra aleatoria
df_sample = df.sample(n=500000, random_state=42)

# Guardar muestra
path_sample = BASE_DIR / "data" / "processed" / "tripdata_sample.csv"
df_sample.to_csv(path_sample, index=False)

print(f"Muestra creada correctamente: {path_sample}")
