"""
ARQUITETURA DE DADOS
"""

#importações
from pathlib import Path
import pandas as pd
from datetime import datetime as dt

# Caminho
_filepath = Path("C:/Users/E805511/Downloads/Consumo_horario_2022_12/Consumo_horario_2022_12.csv")


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
    
    if i == 1:
        break
    
df = pd.concat(list_processed_chunk)

# Dados relacionados ao consumo
# Modificação das infotmações
# Modificação dos nomes
# Condicionais

# DICT 1

# dict_consumo_dados = dict()
# dict_consumo_dados2 = dict()
# for index, rows in df.iterrows():
#     df = df.rename({'Data': 'mes'})
#     rows.drop(columns=DROPED_COLUMNS)
#     dict_consumo_dados.update(rows.to_dict())
#     # Funcionando
#     #----------------------------------------
    
#     data = rows['Data']
#     sigla = rows['Sigla'].strip()
#     submercado = rows['Submercado'].strip()
    
#     dict_consumo_dados2[index] = rows['Data']
#     dict_consumo_dados3 = {
        
#         'mes': data,
#         'sigla': sigla,
#         'submercado': submercado}
    
#     if index == 1:
#         break
    
INFO_ROWS = { 
    
    'Data': 'mes',
    'HH': 'horario',
    'Cód. Perfil': 'codigo_perfil',
    'Sigla': 'sigla',
    'Classe do perfil do agente': 'classe_perfil_do_agente', 
    'Nome Empresarial': 'nome_empresarial', 
    'Cód. Carga': 'codigo_carga', 
    'Carga': 'nome_unidade', 
    'CNPJ da Carga': 'cnpj_carga', 
    'Cidade': 'cidade', 
    'Estado': 'unidade_federativa', 
    'Submercado': 'submercado', 
    'Data de Migração': 'data_de_migracao', 
    'Cód. Perfil Distribuidora ': 'cogigo_perfil_distribuidora', 
    'Sigla Perfil Distribuidora': 'sigla_perfil_distribuidora',
    'Capacidade da Carga (MW)': 'capacidade_da_carga(MW)', 
    'Consumo no Ambiente Livre da parcela de carga - MWh (RC_AL c,j)': 'RC_AL c,j(MWh)', 
    'Consumo de energia ajustado da parcela cativa da carga parcialmente livre - MWh (RC_CAT c,j)': 'RC_CAT_c_j(MWh)', 
    'Consumo de energia ajustado de uma parcela de carga - MWh (RC c,j)': 'RC_c_j(MWh)', 
    'Consumo de energia no ponto de conexão da parcela de carga - MWh (MED_C c,j)': 'MED_C_c_j(MWh)', 
    'Ramo de Atividade': 'ramo_de_atividade'
    
    }
    
OLD_NAMES = list(df.columns)

# -------------------------------------    
consumo_dados = list()
consumo_empresa = list()
consumo_unidade_carga = list()

# -------------------------------------
# Removing duplicates
set_codigo_perfil = set()
set_codigo_carga = set()


for index, rows in df.iterrows():
    
    #==========================================================================
    # DADOS EMPRESA
    #==========================================================================
    
    
    codigo_perfil = rows[OLD_NAMES[2]]
    if codigo_perfil not in set_codigo_perfil:
        # Constração do dict e tratamento dos dados
        consumo_empresa.append({
            
            'codigo_perfil': rows[OLD_NAMES[2]],
            'sigla': rows[OLD_NAMES[3]],
            'classe_perfil_do_agente': rows[OLD_NAMES[4]],
            'nome_empresarial': rows[OLD_NAMES[5]],
            'ramo_de_atividade': rows[OLD_NAMES[20]],
            'list': list()
        })
    
    set_codigo_perfil.add(rows[OLD_NAMES[2]])
    
    
    #==========================================================================
    # DADOS UNIDADES (CARGA)
    #==========================================================================
    # Constração do dict e tratamento dos dados
    
    
    
    codigo_carga = rows[OLD_NAMES[6]]
    if codigo_carga not in set_codigo_carga:
        consumo_unidade_carga.append({
            
            'codigo_unidade_carga': rows[OLD_NAMES[6]],
            'nome_unidade_carga': rows[OLD_NAMES[7]],
            'cnpj_carga': rows[OLD_NAMES[8]],
            'cidade': rows[OLD_NAMES[9]],
            'unidade_federativa': rows[OLD_NAMES[10]],
            'submercado': rows[OLD_NAMES[11]].strip(),
            'data_de_migracao': rows[OLD_NAMES[12]],
            'cogigo_perfil_distribuidora': rows[OLD_NAMES[13]],
            'sigla_perfil_distribuidora': rows[OLD_NAMES[14]],
            'capacidade_da_carga(MW)': rows[OLD_NAMES[15]],
        
        })
    
    set_codigo_carga.add(rows[OLD_NAMES[6]])
    
    data = rows[OLD_NAMES[0]]
    set_data = set(rows[OLD_NAMES[0]])
    set_data.add(data)
    horario = rows[OLD_NAMES[1]]
    list_horario = list()
    
    
    consumo_1 = list()
    consumo_2 = list()
    consumo_3 = list()
    consumo_4 = list()
   
    #==========================================================================
    # DADOS CONSUMO MWH
    #==========================================================================
    # Constração do dict e tratamento dos dados
    
    
    # if data in set_data:
    list_horario.append(horario)
        
        
    consumo_1.append(rows[OLD_NAMES[16]])
    consumo_2.append(rows[OLD_NAMES[17]])
    consumo_3.append(rows[OLD_NAMES[18]])
    consumo_4.append(rows[OLD_NAMES[19]])
        
    
    consumo_dados.append({
        
        'mes': data,
        'horario': list_horario,
        'RC_AL_C_J(MWh)':  consumo_1,
        'RC_CAT_C_J(MWh)': consumo_2,
        'RC_C_J(MWh)': consumo_3,
        'MED_C_C_J(MWh)': consumo_4,
        
        })
    
    if index == 97:
        break
