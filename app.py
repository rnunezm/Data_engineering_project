import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

# Configuración de la página
st.set_page_config(
    page_title="Data Profiling App",
    layout="wide"
)

# Título de la app
st.title("Government Open Data Quality Assessment via Automated Profilers")

# Instrucciones
st.write("Upload a CSV file to generate an interactive profiling report.")

# Subir archivo CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Leer CSV en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Mostrar preview de los primeros registros
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Crear perfil del dataset
    profile = ProfileReport(
        df,
        title="Data Profiling Report",
        explorative=True,
        minimal=False  # Cambia a True si quieres que sea más rápido y ligero
    )

    # Mostrar reporte en Streamlit
    st_profile_report(profile)
else:
    st.info("Please upload a CSV file to generate the report.")