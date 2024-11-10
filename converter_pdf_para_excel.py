import pdfplumber
import pandas as pd
from io import BytesIO

def converter_pdf_para_excel(pdf_file):
    try:
        # Processar o PDF
        with pdfplumber.open(pdf_file) as pdf:
            all_text = ''
            for page in pdf.pages:
                all_text += page.extract_text()

        # Processar o texto extraído e convertê-lo em linhas
        lines = all_text.split("\n")

        # Criar listas para armazenar os dados processados
        ncm = []
        descricao = []
        aliquota = []

        # Iterar sobre as linhas para encontrar padrões de NCM, descrição e alíquota
        for line in lines:
            line_parts = line.split()
            if len(line_parts) > 2:
                try:
                    possible_ncm = line_parts[0].replace(".", "")
                    possible_aliquota = line_parts[-1].replace(",", ".").replace("%", "")
                    
                    # Verificar se a primeira parte da linha é um NCM e a última uma alíquota válida
                    if possible_ncm.isdigit() and possible_aliquota.replace('.', '', 1).isdigit():
                        ncm.append(possible_ncm)
                        aliquota.append(float(possible_aliquota))
                        descricao.append(" ".join(line_parts[1:-1]))
                except ValueError:
                    continue

        # Criar um DataFrame com os dados
        df_tipi = pd.DataFrame({
            'NCM': ncm,
            'Descrição': descricao,
            'Alíquota (%)': aliquota
        })

        # Renomear colunas conforme necessário
        df_tipi.rename(columns={'NCM': 'prod_NCM', 'Alíquota (%)': 'Aliquota_TIPI'}, inplace=True)

        # Converter DataFrame em arquivo Excel para download
        buffer = BytesIO()
        df_tipi.to_excel(buffer, index=False)
        buffer.seek(0)
        
        return buffer
    
    except Exception as e:
        raise ValueError(f"Erro ao processar o arquivo PDF: {e}")
