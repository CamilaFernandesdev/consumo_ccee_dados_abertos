# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:14:03 2023

@author: E805511
"""
import pymongo
import pandas as pd
from pathlib import Path
from datetime import datetime


def mongodb():
    pass

def insert_documentos():
    pass

def processing():
    pass


# Configurar a conexão com o MongoDB
CONNECT_MONGO_NWAUTOMHML = 'mongodb://user_rw:us3r_rw@nwautomhml/'
client = pymongo.MongoClient(CONNECT_MONGO_NWAUTOMHML)
db = client['historico_oficial']
collection = db['test3_consumo_ccee']
print(collection)


# 
_filepath = Path("C:/Users/E805511/Downloads/Consumo_horario_2022_12/Consumo_horario_2022_12.csv")


CHUNKSIZE = 10**5
infomercado_ccee_consumo = list()


def to_datetime(x):
    """lalal."""
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')


# Estrutura 
for i, chunk in enumerate(pd.read_csv(_filepath,
                                      sep = ';',
                                      chunksize=CHUNKSIZE,
                                      low_memory=False,
                                      decimal = ',')):
    
    if (i == 1):
        break
    # Lista com o nome das colunas
    old_names_columns = list(chunk.columns)
    
    # Campo mes_horario    
    

    # Nas informações cada linha representa um documento do Mongo
    for index, rows in chunk.iterrows():
        
        chunk['dataHora'] = chunk.apply(lambda row: to_datetime(rows[old_names_columns[0]] + ' ' + rows[old_names_columns[1]]), axis=1)
        infomercado_ccee_consumo.append({
         
             'mes_horario':                 rows[old_names_columns[1]],
             'codigo_perfil':               rows[old_names_columns[2]],
             'sigla':                       rows[old_names_columns[3]],
             'classe_perfil_do_agente':     rows[old_names_columns[4]],
             'nome_empresarial':            rows[old_names_columns[5]],
             'codigo_unidade_carga':        rows[old_names_columns[6]],
             'nome_unidade_carga':          rows[old_names_columns[7]],
             'cnpj_carga':                  str(rows[old_names_columns[8]]).replace('.',''),
             'cidade':                      rows[old_names_columns[9]],
             'unidade_federativa':          rows[old_names_columns[10]].strip(),
             'submercado':                  rows[old_names_columns[11]].strip(),
             'data_de_migracao':            rows[old_names_columns[12]],
             'cogigo_perfil_distribuidora': rows[old_names_columns[13]],
             'sigla_perfil_distribuidora':  rows[old_names_columns[14]],
             'capacidade_da_carga(MW)':     rows[old_names_columns[15]],
             'RC_AL_C_J(MWh)':              rows[old_names_columns[16]],
             'RC_CAT_C_J(MWh)':             rows[old_names_columns[17]],
             'RC_C_J(MWh)':                 rows[old_names_columns[18]],
             'MED_C_C_J(MWh)':              rows[old_names_columns[19]],
             'ramo_de_atividade':           rows[old_names_columns[20]],
         })
        
        #collection.insertMany(infomercado_ccee_consumo)
