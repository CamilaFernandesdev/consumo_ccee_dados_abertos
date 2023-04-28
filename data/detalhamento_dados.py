import re
import tempfile
import pandas as pd
from pathlib import Path

class DetalhamentoDados:
    def __init__(self):
        """Representa o arquivo baixado no tableau da página Cosumo da CCEE.
        
        filename_pattern: Regular expression
            O padrão de expressão regular que será usado para encontrar o arquivo.
            Atualmente o nome do arquivo baixado é Detalhamento - Dados.csv
            Porém, caso haja mudança modificar esse parâmetro.
            
        filepath: str
            O caminho completo para o arquivo encontrado, ou None se nenhum arquivo
            corresponder ao padrão.
        """
        self.filename_pattern = r'(?i)^Detalhamento *- *Dados.csv$'
        
        # Variáveis quando executar os métodos.
        self.filepath = None
        self.df = None
    
    def get_file_temp_folder(self) -> None:
        """Localiza um arquivo com nome que corresponde a um padrão de expressão regular na pasta temporária."""
        # Caminho da pasta temporária
        temp_dir = Path(tempfile.gettempdir())
        filename = re.compile(self.filename_pattern)
        
        # Procurando o arquivo na pasta temporária por re
        self.filepath = next((temp_file for temp_file in temp_dir.glob('*.csv') if filename.match(temp_file.name)), None)
        self.filepath = str(self.filepath)
    
    def reader(self) -> pd.DataFrame:
        """
        Lê um arquivo Detalhamento dos Dados no formato CSV e retorna um DataFrame.

        Parâmetros
        ----------
        filepath : str
            O caminho completo para o arquivo a ser lido.

        Retorna
        -------
        pd.DataFrame
            Um DataFrame contendo os dados lidos a partir do arquivo.

        """
        path = Path(self.filepath)
        # Não alterar o método de leitura apenas assim que funciona
        df = pd.read_csv(path, encoding='UTF-16', sep='\t')
        # Date
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
        # Tratando os dados de consumo
        df['Consumo (MWm)'] = df['Consumo (MWm)'].str.replace('.','').str.replace(',','.')
        df['Consumo (MWm)'] = pd.to_numeric(df['Consumo (MWm)']).round(5)
        
        return df
    
    def detalhamento_dados(self) -> pd.DataFrame:
        """Executa os outros métodos.
        
        Importe para as DAGs.
        """
        detalhamento_dados_filepath = self.get_file_temp_folder()
        self.df = self.reader()
        
        return self.df
