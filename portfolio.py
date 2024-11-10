import streamlit as st
from converter_pdf_para_excel import converter_pdf_para_excel

# Título do portfólio
#st.title("Portfólio de Scripts Python - José Carlos")

# Título do portfólio na barra lateral
st.sidebar.title("Portfólio - Bora Analisar")
# Menu lateral
menu = st.sidebar.selectbox("Escolha a categoria:", ["Pdf para Excel"])

# Categoria: PDF para Excel
if menu == "Pdf para Excel":
    st.header("Converte TIPI em PDF para Excel")

    # Upload do arquivo PDF
    uploaded_file = st.file_uploader("Envie o arquivo TIPI em PDF", type="pdf")
    
    if uploaded_file is not None:
        try:
            # Converter PDF para Excel
            excel_data = converter_pdf_para_excel(uploaded_file)
            
            # Download do Excel
            st.download_button(
                label="Baixar arquivo Excel",
                data=excel_data,
                file_name="TIPI_Dados.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("Arquivo processado e pronto para download!")
        
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
