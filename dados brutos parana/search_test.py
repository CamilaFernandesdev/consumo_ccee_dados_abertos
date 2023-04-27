# ============================= Leitura dos dados ========================================
# Jupyter notebook
# Início 2019 -1 com informações incompletas e Término 2023 - 2

_filepath = '/content/drive/MyDrive/COPEL/Consumo energia CCEE/Consumo_horario_2023_01.csv'


list_processed_chunk = list()
for i, chunk in enumerate(pd.read_csv(_filepath,
                                      sep = ';',
                                      chunksize=10**5,
                                      low_memory=False,
                                      decimal = ',')):
                                        
    list_processed_chunk.append(chunk)
    
    # Processar todos os dados depois
    # 24 milhôes de linhas
    # aprox. 17 min por arquivo
    if i == 3:
        break

df_dados_brutos = list_processed_chunk[2]
len(list_processed_chunk)

# ============================= Verificação ========================================
df_dados_brutos

# ============================= Filtro por estado ========================================
df_pr_brutos = df_dados_brutos[df_dados_brutos['Estado'] == 'BA']
df_estados = df_dados_brutos['Estado']
df_estados.unique()

# ============================= Paraná ========================================

list_parana_dados_brutos = list()
for dataframe in list_processed_chunk:
  # search State ]Paraná
  # Corrigir para não adicionar df vazios na lista
  df = dataframe[dataframe['Estado'] == 'PR      ']
  if df.empty:
      continue

  else:
      list_parana_dados_brutos.append(df)

# ============================= Verificação ========================================
list_parana_dados_brutos[2]
