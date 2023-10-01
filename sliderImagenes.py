import streamlit as st
import time

# Lista de URLs de las imágenes que deseas mostrar en el slider
image_urls = [
    "imagenes WiroLimo/SUV1.png",
    "imagenes WiroLimo/SUV2.png",
    "imagenes WiroLimo/sedan1.png",
    "imagenes WiroLimo/Limo.png",
]

# Índice de la imagen actual
current_image = 0

# Función para actualizar la imagen
def update_image():
    global current_image
    st.image(image_urls[current_image], use_column_width=True)
    current_image = (current_image + 1) % len(image_urls)

# Configuración de la página
st.title("Slider de Imágenes")
st.markdown("Cambia automáticamente cada 30 segundos")

# Contenedor para la imagen
image_container = st.empty()

# Bucle para actualizar las imágenes cada 30 segundos
while True:
    update_image()
    time.sleep(30)
    image_container.empty()  # Borrar la imagen actual para mostrar la siguiente
