import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Cifra Repartidora")

# Crear un campo de entrada para ingresar la cantidad de votos de cada partido A-J
st.subheader("Ingresar Votos por Partido")
partidos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
votos_partidos = {}
for partido in partidos:
    votos_partidos[partido] = st.number_input(f'Votos para el Partido {partido}', value=0)

# Calcular la sumatoria de los votos de los partidos
sumatoria = sum(votos_partidos.values())

# Crear un campo para ingresar los votos en blanco
votos_blanco = st.number_input("Votos en Blanco", value=0)

# Calcular el cociente
validos = (sumatoria + votos_blanco) # // 100

# Crear un campo para ingresar el número de curules
curules = st.number_input("Número de Curules", min_value=1, value=1)

cociente = validos / curules
# Calcular el umbral
umbral = cociente / 2

# Crear una tabla para mostrar los resultados
st.subheader("Distribución de Curules")
resultados = []
for partido in partidos:
    fila = []
    for i in range(1, curules + 1):
        fila.append(votos_partidos[partido] // i)
    resultados.append(fila)
resultados_df = pd.DataFrame(resultados, columns=[f"Curul {i}" for i in range(1, curules + 1)], index=partidos)


# Mostrar la tabla de resultados
st.dataframe(resultados_df)

# Mostrar el umbral calculado
st.subheader(f"Umbral: {umbral}")

# Obtener una lista de los números ordenados de mayor a menor
valores_ordenados = sorted(resultados_df.values.ravel(), reverse=True)

# Mostrar la lista de números ordenados
st.write("Números ordenados de mayor a menor: (Por ejemplo: si son 10 curules, el ultimo corresponde a la posicion 9 y ese ultimo seria la cifra repartidora)", valores_ordenados)