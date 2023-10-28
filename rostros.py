import streamlit as st
import cv2
import numpy as np
import face_recognition

# Crear una base de datos de características faciales de personas
database = {
    'Luis Fernando Umana': face_recognition.face_encodings(face_recognition.load_image_file('persona1.jpg'))[0],
    'Miguel': face_recognition.face_encodings(face_recognition.load_image_file('persona2.jpg'))[0],
}
try:
    database['Persona1'] = face_recognition.face_encodings(face_recognition.load_image_file('persona1.jpg'))[0]
except FileNotFoundError:
    st.write("Archivo 'persona1.jpg' no encontrado")

# Variables para rastrear la cantidad de fotos tomadas y el límite
fotos_tomadas = 0
limite_fotos = 4

# Función para reconocer rostros en la imagen de la cámara
def reconocer_rostros(frame):
    global fotos_tomadas
    if fotos_tomadas >= limite_fotos:
        return

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        for nombre, encodings in database.items():
            matches = face_recognition.compare_faces([encodings], face_encoding)
            if True in matches:
                st.write(f'Persona reconocida: {nombre}')
                fotos_tomadas += 1
                break  # Detener la búsqueda cuando se encuentra una coincidencia

# Configurar la interfaz de Streamlit
st.title("Reconocimiento Facial")

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while fotos_tomadas < limite_fotos:
    ret, frame = cap.read()
    reconocer_rostros(frame)
    st.image(frame, channels="BGR")

# Mostrar un mensaje después de salir del bucle
if fotos_tomadas > 0:
    st.write(f"Se encontraron {fotos_tomadas} fotos.")
else:
    st.write("No se encontraron fotos.")

# Detener la cámara al cerrar la aplicación
cap.release()
