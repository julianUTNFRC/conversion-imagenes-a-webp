import os
from PIL import Image

# Rutas de las carpetas
carpeta_origen = 'imagenes'
carpeta_destino = 'convertidas'

# Crea la carpeta de destino si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Recorre todas las imágenes en la carpeta origen
for archivo in os.listdir(carpeta_origen):
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_origen, archivo)

    # Verifica si es un archivo de imagen
    if os.path.isfile(ruta_archivo):
        # Abre la imagen
        with Image.open(ruta_archivo) as img:
            # Define el nombre del archivo de salida
            nombre_salida = os.path.splitext(archivo)[0] + '.webp'
            ruta_salida = os.path.join(carpeta_destino, nombre_salida)

            # Convierte la imagen a webp y la guarda
            img.save(ruta_salida, 'webp')

print("Conversión completada.")
