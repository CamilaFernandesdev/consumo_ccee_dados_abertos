from pathlib import Path
import pandas as pd




class ConsumoCCEE():
    def __init__(self, _filepath: Path) -> None:
        
        # Informações da base de dados
        self.codigo_perfil = set()
        self.classe_perfil_do_agente = None
        self.sigla = None
        self.nome_empresarial = None
        self.ramo_atividade = None

        self.codigo_unidade_carga = None
        self.nome_unidade_carga = None
        self.cnpj_carga = None
        self.cidade = None 
        self.unidade_federativa = None
        self.submercado = None
        self.data_migracao = None
        self.codigo_perfil_distribuidora = None
        self.sigla_perfil_distribuidora = None
        self.capacidade_da_carga = None
        
        self.data = None
        self.horario = None
        self.consumo_1 = None
        self.consumo_2 = None
        self.consumo_3 = None
        self.consumo_4 = None
        
        # Documentos para o Mongo
        self.infomercado_ccee_empresa = list()
        self.infomercado_ccee_consumo_carga = list() #lista?
        self.infomercado_ccee_empresa_unidades = list()

        # Apenas constantes
        CHUNK_SIZE = 10**5
        for i, chunk in enumerate(pd.read_csv(_filepath,
                                              chunksize=CHUNK_SIZE,
                                              sep=';',
                                              decimal=',')):
          
          
          for index, rows in chunk:
              self.empresas(row)


                                         
            pass
    
    
    def informacoes_chunks(self, i:int, chunk:pd.DataFrame):
        self.old_names_columns = list(chunk.columns)
        
    
    def empresas(rows: pd.Series) -> list[dict]:
        # Definindo cada empresa de acordo com o código do perfil
        codigo_perfil = rows[self.old_names_columns[2]]

        # Retirando as redundâncias
        self.codigo_perfil.add(codigo_perfil)

        # Informações para o Mongo na Colletion Empresa
        if codigo_perfil not in self.codigo_perfil:
            self.infomercado_ccee_empresa.append({
            
            'codigo_perfil': rows[self.old_names_columns[2]],
            'sigla': rows[self.old_names_columns[3]],
            'classe_perfil_do_agente': rows[self.old_names_columns[4]],
            'nome_empresarial': rows[self.old_names_columns[5]],
            'ramo_de_atividade': rows[self.old_names_columns[20]],
        
            })
        
    def unidades_carga(rows: pd.Series) -> list[list[dict]]:
        set_unidades_carga = set()
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

        
    def carregar_mongo():     
        pass   
