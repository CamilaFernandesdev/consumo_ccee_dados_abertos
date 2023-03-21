"""."""
import pandas as pd


df = pd.read_csv('C:/Users/E805511/Downloads/Detalhamento - Dados (1).csv', encoding='UTF-16', sep='\t')


df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
df['Consumo (MWm)'] = df['Consumo (MWm)'].str.replace('.','').str.replace(',','.')
df['Consumo (MWm)'] = pd.to_numeric(df['Consumo (MWm)'])


df_resultado = df.groupby([df['Data'].dt.year, 
                           df['Data'].dt.month, 
                           df['Classe'], 
                           df['Ambiente'], 
                           df['Submercado'],
                           df['Estado'],
                           df['Ramo de atividade']]) \
                           .agg({'Consumo (MWm)' : 'mean'})

data = [0, 2, 3, 4, 5, 6]

# convert index columns to datetime format
df_resultado['Datas'] = pd.to_datetime(df_resultado.index.map(lambda x: '{}/{}'.format(x[0], x[1])), format='%Y/%m')
df_resultado = df_resultado.reset_index(level=data)
df_resultado = df_resultado.drop(columns='Data')

# df_resultado['Consumo (MWm)'] = df_resultado['Consumo (MWm)'].round(2)
df_resultado['Consumo (MWm)'] = df_resultado['Consumo (MWm)'].apply(lambda x: '{:.4f}'.format(float(x)).replace('.',','))


df_resultado.to_csv('C:/Users/E805511/Downloads/novo_dataframe.csv',
                    sep=';',
                    index=False, )
