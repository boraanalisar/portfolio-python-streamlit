import streamlit as st
import pandas as pd

# Título do portfólio
st.title("Portfólio de Scripts Python - José Carlos")

# Menu lateral
menu = st.sidebar.selectbox("Escolha a categoria:", ["Pdf para Excel"])

# Categoria: Calculadoras
if menu == "Pdf para Excel":
    st.header("Converte TIPI em PDF para Excel")
    




