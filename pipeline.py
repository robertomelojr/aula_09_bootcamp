from etl import pipeline_calcular_kpi_de_vendas_consolidado as pipeline
 
pasta_argumento : str = 'data'
formato_de_saida : list = ["csv"]
 
pipeline(pasta = pasta_argumento ,formato_de_saida = formato_de_saida)  
   
