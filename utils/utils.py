def get_file_temp_folder(re_name: str) -> str:
     
    temp_dir = Path(tempfile.gettempdir())
    file_name_pattern = re.compile(re_name)
    filepath = next((temp_file for temp_file in temp_dir.glob('*.csv') if file_name_pattern.match(temp_file.name)), None)
    
    # Converter para string porque filepath retorna um objeto WindowsPath
    return str(filepath)



def reader_consumo_tableau_data(filepath: str) -> pd.DataFrame:
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
    path = Path(filepath)
    # Não alterar o método de leitura apenas assim que funciona
    df = pd.read_csv(path, encoding='UTF-16', sep='\t')
    # Date
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    # Tratando os dados de consumo
    df['Consumo (MWm)'] = df['Consumo (MWm)'].str.replace('.','').str.replace(',','.')
    df['Consumo (MWm)'] = pd.to_numeric(df['Consumo (MWm)']).round(5)
    
    return df
