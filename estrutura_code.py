import pandas as pd
from pathlib import Path

_filepath = Path("C:/Users/E805511/Downloads/Consumo_horario_2022_12/Consumo_horario_2022_12.csv")

# lê o arquivo csv em chunks de 1000 linhas
chunk_size = 10000

# informações

self_codigo_perfil = set()
empresas = list()
infomercado_ccee_empresa = list()






# Estrutura 
for i, chunk in enumerate(pd.read_csv(_filepath,
                                      sep = ';',
                                      chunksize=chunk_size,
                                      low_memory=False,
                                      decimal = ',')):
    
    if (i == 4):
        break
    # Informações
    
    
    last_hour = chunk.iloc[-1]["HH"]
    old_names_columns = list(chunk.columns)
    dict_empresa_unidade = chunk.groupby('Cód. Perfil').agg({'Cód. Carga':lambda x: list(set(x))}).to_dict(orient='index')
    
    
    # Estrutura
    for index, rows in chunk.iterrows(): 

        #==========================================================================
        # DADOS EMPRESA
        #==========================================================================
        codigo_perfil = rows[old_names_columns[2]]

        # Informações para o Mongo na Colletion Empresa
        if codigo_perfil not in self_codigo_perfil:
            infomercado_ccee_empresa.append({
            
            'codigo_perfil':           rows[old_names_columns[2]],
            'sigla':                   rows[old_names_columns[3]],
            'classe_perfil_do_agente': rows[old_names_columns[4]],
            'nome_empresarial':        rows[old_names_columns[5]],
            'ramo_de_atividade':       rows[old_names_columns[20]],
        
            })
            
        # Retirando as redundâncias
        self_codigo_perfil.add(codigo_perfil)
        
        
        #==========================================================================
        # DADOS UNIDADES (CARGA)
        #==========================================================================
        # Constração do dict e tratamento dos dados
        # consumo_unidade_carga.append({
            
        #     'codigo_unidade_carga': rows[OLD_NAMES[6]],
        #     'nome_unidade_carga': rows[OLD_NAMES[7]],
        #     'cnpj_carga': str(rows[OLD_NAMES[8]]).replace('.',''),
        #     'cidade': rows[OLD_NAMES[9]],
        #     'unidade_federativa': rows[OLD_NAMES[10]],
        #     'submercado': rows[OLD_NAMES[11]].strip(),
        #     'data_de_migracao': rows[OLD_NAMES[12]],
        #     'cogigo_perfil_distribuidora': rows[OLD_NAMES[13]],
        #     'sigla_perfil_distribuidora': rows[OLD_NAMES[14]],
        #     'capacidade_da_carga(MW)': rows[OLD_NAMES[15]],
        
        # }
