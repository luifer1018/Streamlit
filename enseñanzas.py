import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conexión a la base de datos SQLite
conn = sqlite3.connect('enseñanzas.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enseñanzas (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        numero_enseñanza TEXT,  -- Cambiar a TEXT
        fecha DATE,
        predicador TEXT,
        nota TEXT
    )
''')

conn.commit()

# Función para agregar un registro
def agregar_enseñanza(nombre, numero_enseñanza, fecha, predicador, nota):
    cursor.execute('INSERT INTO enseñanzas (nombre, numero_enseñanza, fecha, predicador, nota) VALUES (?, ?, ?, ?, ?)',
                   (nombre, numero_enseñanza, fecha, predicador, nota))
    conn.commit()

# Función para actualizar un registro
def actualizar_enseñanza(id, nombre, numero_enseñanza, fecha, predicador, nota):
    cursor.execute('UPDATE enseñanzas SET nombre=?, numero_enseñanza=?, fecha=?, predicador=?, nota=? WHERE id=?',
                   (nombre, numero_enseñanza, fecha, predicador, nota, id))
    conn.commit()

# Función para eliminar un registro
def eliminar_enseñanza(id):
    cursor.execute('DELETE FROM enseñanzas WHERE id=?', (id,))
    conn.commit()

# Función para obtener todas las enseñanzas
def obtener_enseñanzas():
    cursor.execute('SELECT * FROM enseñanzas')
    enseñanzas = cursor.fetchall()
    return enseñanzas

# Función para contar las veces que se ha dado un número de enseñanza
def contar_numero_enseñanza():
    cursor.execute('SELECT numero_enseñanza, COUNT(*) FROM enseñanzas GROUP BY numero_enseñanza')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Número de Enseñanza', 'Cantidad'])
    return df

# Configuración de la aplicación Streamlit
st.title('Gestión de Enseñanzas')

# Menú de selección de acción
accion = st.selectbox('Seleccione una acción', ['Crear', 'Actualizar', 'Eliminar', 'Ver Enseñanzas', 'Ver Gráfico','Buscar por Nombre o Número de Enseñanza'])
# Buscar enseñanzas por nombre o número de enseñanza
if accion == 'Buscar por Nombre o Número de Enseñanza':
    st.subheader('Buscar enseñanzas por Nombre o Número de Enseñanza')
    consulta = st.text_input('Ingrese el nombre o número de enseñanza a buscar:')
    if st.button('Buscar'):
        cursor.execute('SELECT * FROM enseñanzas WHERE nombre LIKE ? OR numero_enseñanza LIKE ?', ('%' + consulta + '%', '%' + consulta + '%'))
        resultados = cursor.fetchall()
        if not resultados:
            st.warning('No se encontraron enseñanzas que coincidan con la consulta.')
        else:
            df = pd.DataFrame(resultados, columns=['ID', 'Nombre', 'Número de Enseñanza', 'Fecha', 'Predicador', 'Nota'])
            st.write(df)

# Realizar la acción seleccionada
if accion == 'Crear':
    st.subheader('Crear una nueva enseñanza')
    nombre = st.text_input('Nombre')
    numero_enseñanza = st.text_input('Número de Enseñanza')
    fecha = st.date_input('Fecha')
    predicador = st.text_input('Predicador')
    nota = st.text_area('Nota')
    if st.button('Guardar'):
        agregar_enseñanza(nombre, numero_enseñanza, fecha, predicador, nota)
        st.success('Enseñanza creada con éxito!')

elif accion == 'Actualizar':
    st.subheader('Actualizar una enseñanza existente')
    enseñanzas = obtener_enseñanzas()
    enseñanza_ids = [str(enseñanza[0]) for enseñanza in enseñanzas]
    selected_id = st.selectbox('Seleccione una enseñanza para actualizar', enseñanza_ids)
    enseñanza = [enseñanza for enseñanza in enseñanzas if str(enseñanza[0]) == selected_id][0]
    nombre = st.text_input('Nombre', enseñanza[1])
    numero_enseñanza = st.text_input('Número de Enseñanza', enseñanza[2])
    fecha = st.text_input('Fecha', enseñanza[3])
    predicador = st.text_input('Predicador', enseñanza[4])
    nota = st.text_area('Nota', enseñanza[5])
    if st.button('Actualizar'):
        actualizar_enseñanza(int(selected_id), nombre, numero_enseñanza, fecha, predicador, nota)
        st.success('Enseñanza actualizada con éxito!')

elif accion == 'Eliminar':
    st.subheader('Eliminar una enseñanza existente')
    enseñanzas = obtener_enseñanzas()
    enseñanza_ids = [str(enseñanza[0]) for enseñanza in enseñanzas]
    selected_id = st.selectbox('Seleccione una enseñanza para eliminar', enseñanza_ids)
    if st.button('Eliminar'):
        eliminar_enseñanza(int(selected_id))
        st.success('Enseñanza eliminada con éxito!')

elif accion == 'Ver Enseñanzas':
    st.subheader('Enseñanzas existentes')
    enseñanzas = obtener_enseñanzas()
    df = pd.DataFrame(enseñanzas, columns=['ID', 'Nombre', 'Número de Enseñanza', 'Fecha', 'Predicador', 'Nota'])
    st.write(df)

elif accion == 'Ver Gráfico':
    st.subheader('Gráfico de frecuencia de Números de Enseñanza')
    df = contar_numero_enseñanza()
    st.bar_chart(df.set_index('Número de Enseñanza'))

# Cerrar la conexión a la base de datos
conn.close()
