import streamlit as st
import pandas as pd

# Título do portfólio
st.title("Portfólio de Scripts Python - José Carlos")

# Menu lateral
menu = st.sidebar.selectbox("Escolha a categoria:", ["Pdf para Excel"])

# Categoria: Calculadoras
if menu == "Pdf para Excel":
    st.header("Converte TIPI em PDF para Excel")
    


# Categoria: Análises de Dados
'''elif menu == "Análises de Dados":
    st.header("Análise de Dados de Vendas")
    st.write("Aqui você pode carregar um arquivo CSV de vendas e visualizar uma análise.")

    # Upload do arquivo
    file = st.file_uploader("Carregue o arquivo CSV", type=["csv"])
    
    if file is not None:
        import pandas as pd
        df = pd.read_csv(file)
        st.write("Visualização dos dados:")
        st.write(df)
        st.write("Resumo estatístico:")
        st.write(df.describe())

# Categoria: Automação
elif menu == "Automação":
    st.header("Automação de Tarefas")
    st.write("Aqui você encontrará scripts para automatizar tarefas repetitivas.")

    # Exemplos de automação (personalize conforme seus scripts)
    from st_aggrid import AgGrid

    data = {
        'Produto': ['Produto A', 'Produto B', 'Produto C'],
        'Quantidade': [10, 20, 15]
    }
    df = pd.DataFrame(data)
    AgGrid(df)

    st.write("- Enviar e-mails automaticamente")
    st.write("- Processar arquivos em lote")

# Categoria: Visualizações
elif menu == "Visualizações":
    st.header("Visualizações de Dados")
    st.write("Visualize gráficos interativos baseados em seus dados.")

    # Exemplo de gráfico
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    st.pyplot(fig)'''

