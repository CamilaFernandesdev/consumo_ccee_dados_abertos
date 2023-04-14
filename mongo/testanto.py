import re
# Nomes desejados
column_name = ['Submercado', 'DATA', 'Status Migracao', 'Classe', 'Ambiente', 'Ramo de atividade', 'Estado',  'Consumo (MWm)']
new_dict = dict()   

# Como os dados CCEE alteram constantemente
# Key: nomes dos campus do Mongo
# Value: as possibilidade de alterações no nome das colunas na base de dados
DICIONARIO = {
    'dia': ['(?i)^data[s]?$'],
    'classe': ['(?i)^Classe[s]?$'],
    'ambiente': ['(?i)^Ambiente[s]?$'],
    'ramo_de_atividade': ['(?i)^[Rr]amo[s]? *de *[Aa]tividade[s]?$'],
    'submercado': ['(?i)^Submercado[s]?$'],
    'unidade_federativa': ['(?i)^[Uu][Ff]?$', '(?i)^Estado[s]?$'],
    'status_migracao': ['(?i)^Status *[de]? *Migração$', '(?i)^Status *[de]? *Migracao$'],
    'MWm': ['(?i)^Consumo *\\([Mm][Ww][Mm]\\)$']
}

for key, value in DICIONARIO.items():
    for regex in value:
        new_dict.update({column: key  for column in column_name if re.match(regex, column)})
        
new_dict

# ===========================================
dicionario1 = dict()
if bool(dicionario1) == False:
    raise ValueError("O dicionário está vazio, não foi criado corretamente")

# =============================================

