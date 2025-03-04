import streamlit as st
import joblib
import numpy as np

pipeline = joblib.load('pipeline_clasificacion.joblib')

st.title("Predicción de Cut de Diamante")

# FORMULARIO PARA INGRESAR CARACTERÍSTICAS.
carat = st.number_input('Carat', min_value=0.1, max_value=10.0, value=1.0)
depth = st.number_input('Depth', min_value=55.0, max_value=70.0, value=60.0)
table = st.number_input('Table', min_value=50.0, max_value=70.0, value=57.0)
x = st.number_input('X', min_value=0.0, max_value=10.0, value=5.0)
y = st.number_input('Y', min_value=0.0, max_value=10.0, value=5.0)
z = st.number_input('Z', min_value=0.0, max_value=10.0, value=5.0)

# HACER PREDICCIONES CUANDO SE ENVÍE EL FORMULARIO.
if st.button('Predecir Cut'):
    pred_input = np.array([[carat, depth, table, x, y, z]])
    pred = pipeline.predict(pred_input)
    st.metric(label="Cut Predicho", value=pred[0])
