import streamlit as st

# Establecer el color de fondo de la página
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF; /* Cambia el color de fondo de la página */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Establecer el estilo de la banda verde
st.markdown(
    """
    <style>
    .green-band {
        background-color: #00FF00; /* Cambia el color de la banda a verde */
        padding: 20px; /* Añade relleno para que el texto no esté pegado al borde */
        text-align: center; /* Centra el texto en la banda */
        color: #0000FF; /* Cambia el color del texto a azul */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar el texto en la banda verde
st.markdown('<div class="green-band">Este es un texto en una banda verde y azul.</div>', unsafe_allow_html=True)
