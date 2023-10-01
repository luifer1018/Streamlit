import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Cual es el número a escoger?',
     df['first column'])

'Usted a selecionado la opción: ', option