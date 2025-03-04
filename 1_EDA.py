import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Análisis Exploratorio del Dataset Diamonds", layout="wide")
st.title("Análisis Exploratorio de Datos (EDA)")

df = pd.read_csv("ds_diamonds.csv")

df.drop(columns=["Unnamed: 0"], inplace=True)

# APLICANDO LOS FILTROS GLOBALES:
col1, col2 = st.columns(2)
with col1:
    categoria = st.selectbox("Selecciona una categoría:", df.select_dtypes(include=['object']).columns)
with col2:
    numerica = st.selectbox("Selecciona una variable numérica:", df.select_dtypes(include=['int64', 'float64']).columns)

# FILTRAR DATOS:
df_filtrado = df.copy()
df_filtrado = df_filtrado[df_filtrado[categoria].notna()]
df_filtrado = df_filtrado[df_filtrado[numerica].notna()]

# GRÁFICOS UNIVARIANTES: HISTOGRAMA; KDEPLOT; Y BOXPLOT.
st.subheader("Gráficos Univariantes: Histograma, Kdeplot y Boxplot.")
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(df_filtrado[numerica], kde=True, ax=ax[0])
sns.kdeplot(df_filtrado[numerica], ax=ax[1])
sns.boxplot(x=df_filtrado[numerica], ax=ax[2])
st.pyplot(fig)

# GRÁFICOS BIVARIANTES: SCATTER.
st.subheader("Gráficos Bivariantes: Scatter.")
fig = px.scatter(df_filtrado, x=numerica, y="price", color=categoria, title="Relación entre Precio y " + numerica)
st.plotly_chart(fig)

# GRÁFICOS MULTIVARIANTES: HEATMAP; PAIRPLOT; Y SCATTER (HUE).
st.subheader("Gráficos Multivariantes: Heatmap, Pairplot y Scatter.")
col1, col2 = st.columns(2)
with col1:
    st.write("Heatmap de correlación")
    corr_matrix = df_filtrado.select_dtypes(include=['int64', 'float64']).corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
with col2:
    st.write("Pairplot de las variables numéricas")
    st.warning("Este gráfico puede tardar en generarse si hay muchos datos")
    pairplot_fig = sns.pairplot(df_filtrado, hue=categoria, diag_kind='kde')
    st.pyplot(pairplot_fig)

# SCATTER HUE O CON COLOR. 
st.subheader("Scatter con color (hue)")
fig = px.scatter(df_filtrado, x="carat", y="price", color=categoria, title="Scatter de Carat vs Price")
st.plotly_chart(fig)
