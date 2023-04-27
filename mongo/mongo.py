# MONGO
import pymongo
import pandas as pd

from infra_copel import MongoHistoricoOficial

# Adicionar método no código original
def sort_values(self) -> None:
    """Ordenar como os dados serão organizados no mongo."""
    return self.df.sort_values(self.df.columns[0], inplace=True, ignore_index=True)



class Mongo:
    """Classe que faz o update das informações do Mongo quando a base de dados sofre alterações."""
    def __init__(self, df: pd.DataFrame, collection: str, dicionario: dict[str: list]):
        """"estrutura - code.py"
        # Key: nomes dos campus do Mongo
        # Value: as possibilidade de alterações no nome das colunas na base de dados
        
        """
        self.df = df
        self.dicionario = dicionario
        self.collection_name = collection
        
        # Variáveis que serão preenchidas após executar os métodos
        self.column_names = list(self.df.columns)
        self.dict_rename = dict()
        self.df_last_document = None
        
        # Conexão com o MongoDB
        self.mdb = MongoHistoricoOficial()
        self.collection = self.mdb[self.collection_name]
        
    def document_information(self, position:str):
        position = str().lowe().strip()            
        if position == "first":
            document = self.collection.find_one(sort=[('_id', pymongo.DESCENDING)])
        elif position == "last":  
            document = self.collection.find_one(sort=[('_id', pymongo.ASCENDING)])
        else:
            print('String invalid.')
        # Informação da últimos dado da collection em series pandas
        self.df_last_document = pd.Series(document)
        self.df_last_document = self.df_last_document.drop(index='_id')
    
    def _create_dict_rename(self):
         # Como os dados CCEE alteram constantemente
         # Cria um dicionário de renomeação utilizando dict comprehension
        for key, list_value in self.DICIONARIO.items():
            for regex in list_value:
                self.dict_rename.update({column: key  for column in self.column_names if re.match(regex, column)})
        
    def _verification_methods(self, columns_number=8):
        
        # Verifica se o tamanho de b é igual a 8
        if len(self.column_names) != columns_number:
            raise Exception('A quantidade de colunas da base de dados foi alterada.')
        else:
            self._create_dict_rename()
            # Verifica se todos os nomes foram renomeados corretamente
            if set(self.dict_rename.keys()) == set(self.column_names) and set(self.dict_rename.values()) == set(self.DICIONARIO.keys()):
                print('Funcionou lindamente!')
            else:
                raise Exception('Houve alteração no nome das colunas da base de dados.')
    
    def _rename_column(self):
        return self.df.rename(columns = self.dict_rename, inplace=True)
    
    def create_list_diff(self) -> list[dict]:    
        try:
            list_diff = list()
            # Itera pelas colunas e verifica se os valores são iguais
            for idx, row in self.df.iterrows():
                # Verifica se os valores da linha são iguais aos valores do segundo dataframe
                list_diff.append(row.to_dict())
                # Compara os dados e gt retorna os valores como boolean
                # Se diferente retorna True
                result_compare = row.gt(self.df_last_document)
                if result_compare.any() == True:
                    continue
                else:
                    print('Linha encontrada:', idx)
                    break
            
            list_diff.pop()
                
        except ValueError as error:
            print('error')
            print ('Normalmente o error acontece porque os nomes do indexes das Series comparadas estão diferentes.')
            
        return list_diff
    
    def update_mongo(self, dict_rename):
        if bool(self.dict_rename) == False:
            raise ValueError("O dicionário está vazio, não foi criado corretamente!")
        else:
            self.rename_column()

        list_diff = self.create_list_diff()
        # Continuar aqui
        pass
    
    # ----------------------------------------------------------------
    # Excluir essa function
    def upload_all_data_mongo(self, batch_size: int) -> None:
        """Iterate over the rows of the DataFrame and insert each batch of documents."""
        for i in range(0, len(self.df), batch_size):
            batch = list(self.df.iloc[i:i+batch_size].to_dict('records'))
            # collection = mongo_connect(COLLECTION)
            self.collection.insert_many(batch)
