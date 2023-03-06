# Consumo CCEE Dados Abertos

link: https://www.ccee.org.br/dados-e-analises/consumo

```
info_row = {
 'Data': '2023-01-01',
 'HH': 1.0,
 'Cód. Perfil': 3,
 'Sigla': 'RGE SUL',
 'Classe do perfil do agente': 'Distribuidor',
 'Nome Empresarial': 'RGE SUL DISTRIBUIDORA DE ENERGIA S.A.',
 'Cód. Carga': 28,
 'Carga': 'AES-SUL',
 'CNPJ da Carga': 2016440000162.0,
 'Cidade': 'PORTO ALEGRE',
 'Estado': 'RS      ',
 'Submercado': 'SUL',
 'Data de Migração': '2022-12-01 00:00:00-03:00',
 'Cód. Perfil Distribuidora': nan,
 'Sigla Perfil Distribuidora': nan,
 'Capacidade da Carga (MW)': 1540.25,
 'Consumo no Ambiente Livre da parcela de carga - MWh (RC_AL c,j)': 1015.656113,
 'Consumo de energia ajustado da parcela cativa da carga parcialmente livre - MWh (RC_CAT c,j)': 0.0,
 'Consumo de energia ajustado de uma parcela de carga - MWh (RC c,j)': 1015.656113,
 'Consumo de energia no ponto de conexão da parcela de carga - MWh (MED_C c,j)': 985.166441,
 'Ramo de Atividade': 'ACR',
 'CNAE': nan
}
```python


## Novos nomes
De acordo com os padrão do historico_oficial
- Excluir dados do tipo Nan
- 

```
info_row = {
 'Data': 'mes',
 'HH': 'horario',
 'Cód. Perfil': 'codigo_perfil',
 'Sigla': 'sigla',
 'Classe do perfil do agente': 'classe_perfil_do_agente',
 'Nome Empresarial': 'nome_empresarial',
 'Cód. Carga': 'codigo_carga',
 'Carga': 'carga',
 'CNPJ da Carga': 'cnpj_carga',
 'Cidade': 'cidade',
 'Estado': 'unidade_federativa',
 'Submercado': 'submercado',
 'Data de Migração': 'data_de_migracao',
 'Capacidade da Carga (MW)': 'capacidade_da_carga(MW),
 'Consumo no Ambiente Livre da parcela de carga - MWh (RC_AL c,j)': 'RC_AL c,j(MWh)',
 'Consumo de energia ajustado da parcela cativa da carga parcialmente livre - MWh (RC_CAT c,j)': 'RC_CAT_c_j(MWh)',
 'Consumo de energia ajustado de uma parcela de carga - MWh (RC c,j)': 'RC_c_j(MWh)),
 'Consumo de energia no ponto de conexão da parcela de carga - MWh (MED_C c,j)': 'MED_C_c_j(MWh)',
 'Ramo de Atividade': 'ramo_de_atividade',
}
```python
