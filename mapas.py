import streamlit as st
import numpy as np
import pandas as pd


# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Mapa de las coordenadas al rededor de Cali")
        map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [3.43722, -76.5225],
    columns=['lat', 'lon'])
        
    st.map(map_data)        

        
    with right_column:
       st.header("Tabla con direcciones randomicas")
       st.table(map_data)