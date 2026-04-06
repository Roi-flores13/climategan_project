import os
import json

def generate_climategan_json(image_folder, output_json_name="my_images.json"):
    # Lista para almacenar los diccionarios de imágenes
    data_list = []
    
    # Extensiones de imagen soportadas
    valid_extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG')
    
    # Obtener todas las imágenes de la carpeta
    # Es importante usar la ruta completa o relativa correcta desde la raíz del repo
    for filename in os.listdir(image_folder):
        if filename.endswith(valid_extensions):
            # Guardamos la ruta relativa de la imagen
            file_path = os.path.join(image_folder, filename)
            
            # Según el README, el objeto mínimo requiere la llave "x"
            data_list.append({
                "x": file_path
            })
    
    # Guardar el archivo JSON
    with open(output_json_name, 'w') as f:
        json.dump(data_list, f, indent=4)
    
    print(f"✅ Archivo {output_json_name} generado con {len(data_list)} imágenes.")

# Ejecución
# Asumiendo que tus imágenes están en la carpeta que creamos antes
generate_climategan_json("images_ready_640")