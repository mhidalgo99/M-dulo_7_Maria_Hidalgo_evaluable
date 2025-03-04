import streamlit as st

st.set_page_config(page_title="Diamonds Analysis", layout="wide")

st.title("Bienvenido/a a la App de 'Análisis de Diamonds'")
st.write("Selecciona una opción en la barra lateral para explorar los datos, hacer predicciones de precio o clasificar la calidad del corte.")

import streamlit as st
import seaborn as sns
import plotly.express as px

PAGES = {
    "EDA": "1_EDA.py",
    "Regresión": "2_Regresión.py",
    "Clasificación": "3_Clasificación.py"
}
st.sidebar.title("Navegación")
page = st.sidebar.radio("Selecciona una página", options=PAGES.keys())

exec(open(PAGES[page]).read())
