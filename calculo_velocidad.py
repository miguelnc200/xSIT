import pandas as pd
import math
import ast

def calcular_distancia(loc1, loc2):
    """
    Calcula la distancia entre dos puntos en un plano 2D o 3D.
    Los puntos pueden ser en formato [x,y] o [x,y,z].
    """
    try:
        # Convertir strings de listas a listas reales si es necesario
        if isinstance(loc1, str):
            loc1 = ast.literal_eval(loc1)
        if isinstance(loc2, str):
            loc2 = ast.literal_eval(loc2)
        
        # Para puntos 2D (sin coordenada z)
        if len(loc1) == 2 and len(loc2) == 2:
            dx = loc2[0] - loc1[0]
            dy = loc2[1] - loc1[1]
            return math.sqrt(dx**2 + dy**2)
        # Para puntos donde uno es 2D y otro 3D (tomamos solo x,y)
        elif len(loc1) == 2 and len(loc2) == 3:
            dx = loc2[0] - loc1[0]
            dy = loc2[1] - loc1[1]
            return math.sqrt(dx**2 + dy**2)
        # Para puntos 3D
        elif len(loc1) == 3 and len(loc2) == 3:
            dx = loc2[0] - loc1[0]
            dy = loc2[1] - loc1[1]
            dz = loc2[2] - loc1[2]
            return math.sqrt(dx**2 + dy**2 + dz**2)
        else:
            return None
    except:
        return None

def calcular_velocidad(df):
    """
    Añade una columna 'velocidad' al DataFrame calculando la distancia entre
    location y end_location dividida por timeduration.
    """
    velocidades = []
    
    for _, row in df.iterrows():
        loc = row['location']
        end_loc = row['end_location']
        tiempo = row['timeduration']
        
        if tiempo == 0 or pd.isna(tiempo):
            velocidades.append(None)
            continue
            
        distancia = calcular_distancia(loc, end_loc)
        if distancia is None:
            velocidades.append(None)
        else:
            velocidad = (distancia / tiempo) * 3.6
            if velocidad < 210 or velocidad <30:
                velocidades.append(velocidad)
            else: 
                velocidades.append(None)
    
    df['velocidad'] = velocidades
    return df

def procesar_excel(archivo_entrada, archivo_salida=None):
    """
    Procesa el archivo Excel, añadiendo la columna de velocidad.
    Si no se especifica archivo_salida, sobreescribe el original.
    """
    # Leer el archivo Excel
    df = pd.read_excel(archivo_entrada)
    
    # Calcular velocidades
    df = calcular_velocidad(df)
    
    # Guardar el resultado
    if archivo_salida is None:
        archivo_salida = archivo_entrada
    
    df.to_excel(archivo_salida, index=False)
    print(f"Archivo guardado en: {archivo_salida}")

archivo_original = "C:/Users/Usuario/Desktop/Investigacion_blanca/open-data-master/open-data-master/data/events/43/Velocidad.xlsx"
archivo_resultado = "C:/Users/Usuario/Desktop/Investigacion_blanca/open-data-master/open-data-master/data/events/43/velocidad_con_calculo.xlsx"
    
procesar_excel(archivo_original, archivo_resultado)