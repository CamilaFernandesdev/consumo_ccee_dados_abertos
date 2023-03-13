# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:41:21 2023

@author: E805511
"""



import pandas as pd
from pathlib import Path
from datetime import datetime

_filepath = Path("C:/Users/E805511/Downloads/Consumo_horario_2022_12/Consumo_horario_2022_12.csv")

# lê o arquivo csv em chunks de 1000 linhas
chunk_size = 1000

# informações

self_codigo_perfil = set()
self_codigo_carga = set()
empresas = list()
infomercado_ccee_empresa = list()
infomercado_ccee_consumo_unidade = list()
dict_empresa_unidade = dict()




# Estrutura 
for i, chunk in enumerate(pd.read_csv(_filepath,
                                      sep = ';',
                                      chunksize=chunk_size,
                                      low_memory=False,
                                      decimal = ',')):
    
    if (i == 1):
        break
    # Informações
    
    
    last_hour = chunk.iloc[-1]["HH"]
    old_names_columns = list(chunk.columns)
    dict_empresa_unidade.update(chunk.groupby('Cód. Perfil').agg({'Cód. Carga':lambda x: list(set(x))}).to_dict(orient='index'))
    empresas
    
    # Estrutura
    for index, rows in chunk.iterrows(): 

        #==========================================================================
        # DADOS EMPRESA
        #==========================================================================
        codigo_perfil = rows[old_names_columns[2]]
        codigo_carga = rows[old_names_columns[6]]
        # Informações para o Mongo na Colletion Empresa
        if codigo_perfil not in self_codigo_perfil:
            infomercado_ccee_empresa.append({
            
            'codigo_perfil':           rows[old_names_columns[2]],
            'sigla':                   rows[old_names_columns[3]],
            'classe_perfil_do_agente': rows[old_names_columns[4]],
            'nome_empresarial':        rows[old_names_columns[5]],
            'ramo_de_atividade':       rows[old_names_columns[20]],
            'unidade':                 list()
            })
            
            # Retirando as redundâncias
            self_codigo_perfil.add(codigo_perfil)
            
            
            if codigo_carga not in self_codigo_carga: 
            
            # Constração do dict e tratamento dos dados
                infomercado_ccee_consumo_unidade.append({
                    
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
                
                })
                
                self_codigo_carga.add(codigo_carga)
        
        
                # Adicionando as unidades à lista de unidades da empresa correspondente
        for empresa in infomercado_ccee_empresa:
            perfil = empresa['codigo_perfil']
            unidades = dict_empresa_unidade[codigo_perfil]['Cód. Carga']
            for unidade in unidades:
                
                if codigo_carga not in self_codigo_carga:
                    empresa['unidade'].append({
                        
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
                    
                    })
                    
                    self_codigo_carga.add(codigo_carga)
                    break

        #==========================================================================
        # DADOS UNIDADES (CARGA)
        #==========================================================================
        # for dicionarios_empresas in infomercado_ccee_empresa: 

        #     if codigo_carga not in self_codigo_carga: 
            
        #     # Constração do dict e tratamento dos dados
        #         infomercado_ccee_consumo_unidade.append({
                    
        #             'codigo_unidade_carga':        rows[old_names_columns[6]],
        #             'nome_unidade_carga':          rows[old_names_columns[7]],
        #             'cnpj_carga':                  str(rows[old_names_columns[8]]).replace('.',''),
        #             'cidade':                      rows[old_names_columns[9]],
        #             'unidade_federativa':          rows[old_names_columns[10]].strip(),
        #             'submercado':                  rows[old_names_columns[11]].strip(),
        #             'data_de_migracao':            rows[old_names_columns[12]],
        #             'cogigo_perfil_distribuidora': rows[old_names_columns[13]],
        #             'sigla_perfil_distribuidora':  rows[old_names_columns[14]],
        #             'capacidade_da_carga(MW)':     rows[old_names_columns[15]],
                
        #         })
        
        
        
        # # Adicionando as unidades à lista de unidades da empresa correspondente
        # for empresa in infomercado_ccee_empresa:
        #     codigo_perfil = empresa['codigo_perfil']
        #     unidades = dict_empresa_unidade[codigo_perfil]['Cód. Carga']
        #     for unidade in unidades:
        #         for unidade_dict in infomercado_ccee_consumo_unidade:
        #             if unidade_dict['codigo_unidade_carga'] == unidade:
        #                 empresa['unidade'].append(unidade_dict)
        #                 break

        # Retirando as redundâncias
        self_codigo_carga.add(codigo_carga)
        
        
        
        
        #==============
        # DADOOS
        
        # dados = {
            
        #     'mes': ,
        #     'horario': ,
        #     'data_de_migracao': ,
        # 'unidade'
        # '
            
            
            
        #     }
