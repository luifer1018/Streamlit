import streamlit as st
from PIL import Image

# Título de la página
st.title("Imágenes a la Izquierda y a la Derecha")

# Cargar las imágenes
image1 = Image.open("imagenes WiroLimo/Camioneta.jpg")

image2 = Image.open("imagenes WiroLimo/Camioneta2.jpg")


# Dividir el diseño en dos columnas
col1, col2 = st.columns(2)

# Mostrar la primera imagen en la columna izquierda
with col1:
    st.image(image1, caption="Imagen 1", use_column_width=True)
    # Comentario para la primera imagen
    st.write("Comentario para la primera imagen:")

# Mostrar la segunda imagen en la columna derecha
with col2:
    st.image(image2, caption="Imagen 2", use_column_width=True)
    # Comentario para la segunda imagen
    st.write("Comentario para la segunda imagen:")
