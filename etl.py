# Função de extract que le e consolida os json 
import pandas as pd 
import os
import glob
from utils_log import log_decorator

@log_decorator
def extrair_dados_e_consolidar (path_da_pasta : str) -> pd.DataFrame:
    """Função que realiza a extração e concatenação dos dados .json e retorna um pd.Dataframe
    """    
    arquivos_json = glob.glob(os.path.join(path_da_pasta,'*.json'))

    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    df_concatenado = pd.concat(df_list, ignore_index= True)
    return df_concatenado

# um função que transforma
@log_decorator
def calcula_kpi_de_total_de_vendas (df : pd.DataFrame) -> pd.DataFrame:
    """Função que calculo o kpi do total de vendas 
    """  
    df["Total"] = df["Quantidade"]*df["Venda"]
    return df


# uma função que da load em csv ou parquet

@log_decorator
def carregar_dados(df :pd.DataFrame, formato_de_saida : list) :
    """Função que vai definir se o formato de saída será CSV ou Parquet
    """
    for formato in formato_de_saida:
        if formato  == 'csv':
            df.to_csv("dados.csv" , index= False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet")
        
    return

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado (pasta : str, formato_de_saida : list):
    """Função que chama a pipeline do pipeline de vendas consolidado
    """
    
    df_concatenado = extrair_dados_e_consolidar(pasta)
    df_kpi = calcula_kpi_de_total_de_vendas(df=df_concatenado)
    carregar_dados(df=df_kpi,formato_de_saida = formato_de_saida)



## teste : 


if __name__ == "__main__":
    pasta_argumento : str = 'data'
    df_concatenado = extrair_dados_e_consolidar(path_da_pasta= pasta_argumento)
    df_kpi = calcula_kpi_de_total_de_vendas(df=df_concatenado)
    formato_de_saida : list = ["csv","parquet"]
    carregar_dados(df=df_kpi,formato_de_saida = formato_de_saida)