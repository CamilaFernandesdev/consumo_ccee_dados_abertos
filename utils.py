# UTILS ----------------------------------------------------------------
import pandas as pd
from pathlib import Path

def seach_filepath_consumo_tableau_data() -> str:
    # Como procurar as informações?
    # Usar pathlib?
    # Retorar as informações como string?
    # Será parametro para a função leitor consumo tableau
    # return (paste)
    # Tem que limpar a pasta?
    pass

def reader_consumo_tableau_data(filepath):
    path = Path(filepath)

    # Não alterar o método de leitura apenas assim que funciona
    df = pd.read_csv(path, encoding='UTF-16', sep='\t')
    # Date
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    # Tratando os dados de consumo
    df['Consumo (MWm)'] = df['Consumo (MWm)'].str.replace('.','').str.replace(',','.')
    df['Consumo (MWm)'] = pd.to_numeric(df['Consumo (MWm)']).round(5)
    return df

def clear_paste():
    pass
