import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("saber_11.csv")

# Seleccionar categorías específicas de la variable 'ESTU_DEPTO_RESIDE'
categorias_seleccionadas = ['CAUCA', 'AMAZONAS', 'CAQUETA', 'VAUPES', 'VICHADA', 'MAGDALENA', 'CUNDINAMARCA']
df_filtrado = df[df['ESTU_DEPTO_RESIDE'].isin(categorias_seleccionadas)]

# Cambiar el fondo de la página a negro
st.markdown(
    """
    <style>
    .reportview-container {
        background: #000000;
    }
    .sidebar .sidebar-content {
        background: #000000;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
    }
    p {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Crear la figura del boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='ESTU_DEPTO_RESIDE', y='PERCENTIL_GLOBAL', data=df_filtrado)
plt.xticks(rotation=45)
plt.title('¿Hay diferencias entre los percentiles globales dependiendo el departamento de residencia?')
plt.xlabel('Departamento de residencia')
plt.ylabel('Percentil global')

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Texto adicional en la aplicación
st.write("")
