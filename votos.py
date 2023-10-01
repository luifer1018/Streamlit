import streamlit as st
import pandas as pd

# Crear una función para la aplicación
def main():
    st.title("Aplicación de Testigos Electorales")

    # Recopilar información del puesto de votación, el coordinador y otros datos
    numero_puesto = st.text_input("Número de Puesto de Votación:")
    numero_mesa = st.text_input("Número de Mesa:")
    numero_comuna = st.text_input("Número de Comuna:")
    coordinador = st.text_input("Nombre del Coordinador del Puesto:")

    # Crear una tabla para registrar los votos por partido
    partidos = ['Partido A', 'Partido B', 'Partido C', 'Partido D', 'Partido E', 'Partido F', 'Partido G', 'Partido H', 'Partido I', 'Partido J']
    votos = [st.number_input(f'Votos para {partido}', min_value=0) for partido in partidos]

    # Calcular el total de votos
    total_votos = sum(votos)

    # Mostrar la información ingresada
    st.write(f"Número de Puesto de Votación: {numero_puesto}")
    st.write(f"Número de Mesa: {numero_mesa}")
    st.write(f"Número de Comuna: {numero_comuna}")
    st.write(f"Coordinador del Puesto: {coordinador}")

    # Mostrar la tabla de resultados y el total de votos
    resultados = pd.DataFrame({
        'Partido': partidos,
        'Votos': votos
    })

    st.write(resultados)
    st.write(f"Total de Votos: {total_votos}")

if __name__ == "__main__":
    main()
