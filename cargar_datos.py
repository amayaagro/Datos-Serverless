import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 1. Inicializar la conexión con Firebase usando la clave privada descargada
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. Cargar el dataset utilizando Pandas
# REEMPLAZA 'tu_archivo.csv' por el nombre exacto de tu archivo CSV
# on_bad_lines='skip' evita que el script falle si alguna línea del CSV tiene errores de formato
df = pd.read_csv('UTP_Computer_and_Systems.csv', on_bad_lines='skip')

# Limpiar valores nulos para evitar errores de compatibilidad en Firestore
df = df.where(pd.notnull(df), None)

# 3. Iterar sobre las filas y subir el 100% de los datos a una colección
nombre_coleccion = "registros_dataset"

for index, row in df.iterrows():
    # Convertir cada fila del DataFrame en un diccionario
    data = row.to_dict()
    
    # Subir documento a la colección en Firestore
    db.collection(nombre_coleccion).add(data)
    print(f"Registro {index + 1} subido exitosamente.")

print("¡Carga del dataset completada al 100%!")