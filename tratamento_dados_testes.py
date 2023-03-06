
_filepath = "C:/Users/E805511/Downloads/Consumo_horario_2022_12/Consumo_horario_2022_12.csv"
print(_filepath)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:10:03 2023

@author: E805511
"""

"""
ARQUITETURA DE DADOS
"""

#importações
from pathlib import Path
import pandas as pd

# Caminho
_filepath = 'C:/Users/SALA 24H/Downloads/Consumo_horario_2023_01'


# Constantes
DROPED_COLUMNS = ['Cód. Perfil Distribuidora',
                  'Sigla Perfil Distribuidora', 
                  'CNAE']

list_processed_chunk = list()
for i, chunk in enumerate(pd.read_csv(_filepath,
                                      sep = ';',
                                      chunksize=10**5,
                                      low_memory=False,
                                      decimal = ',')):
                                        
    chunk.drop(columns=DROPED_COLUMNS)
    list_processed_chunk.append(chunk)
    
    if i == 2:
        break
    
df = pd.concat(list_processed_chunk)

# Dados relacionados ao consumo
# Modificação das infotmações
# Modificação dos nomes
# Condicionais

# DICT 1

dict_consumo_dados = dict()
dict_consumo_dados2 = dict()
for index, rows in df.iterrows():
    df = df.rename({'Data': 'mes'})
    rows.drop(columns=DROPED_COLUMNS)
    dict_consumo_dados.update(rows.to_dict())
    # Funcionando
    #----------------------------------------
    
    data = rows['Data']
    sigla = rows['Sigla'].strip()
    submercado = rows['Submercado'].strip()
    
    dict_consumo_dados2[index] = rows['Data']
    dict_consumo_dados3 = {
        
        'mes': data,
        'sigla': sigla,
        'submercado': submercado}
    
    if index == 1:
        break
    
