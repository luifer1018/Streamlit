import streamlit as st
import numpy as np
import pandas as pd

st.write("Aqui esta nuestra primera tabla:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("---")
st.write("Aqui esta la tabla con Numpy y numeros ramdomicos en rango de 20 Columnas y 10 filas:")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))