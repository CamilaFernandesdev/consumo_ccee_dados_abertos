
from pathlib import Path
import pandas as pd




class ConsumoCCEE():
    def __init__(self, _filepath: Path) -> None:
        self.codigo_perfil = None
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
        
        
        for i, chunk in enumerate(pd.read_csv(_filepath,
                                              chunksize=100000,
                                              sep=';',
                                              decimal=',')):
                                         
            pass
    
    
    def informacoes(self, chunk):
        self.old_names_columns = list(chunk.columns)
        
    
    def empresas(chunk: pd.DataFrame) -> pd.DataFrame:
        set_empresas = set()
        
        
    def unidades_carga(chunk: pd.DataFrame) -> pd.DataFrame:
        set_unidades_carga = set()
        
        
            
        pass    


class Empresas():
    def __init__(self):
        self.codigo_perfil = None
        self.classe_perfil_do_agente = None
        self.sigla = None
        self.nome_empresarial = None
        self.ramo_atividade = None
    pass


class Datas():
    pass

class UnidadeEmpresas():
    pass
