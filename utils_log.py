from loguru import logger
from sys import stderr
from functools import wraps

# Removendo os handlers existentes para evitar duplicação
logger.remove()

# Configuração do logger para stderr

### Cuidados -  1: Rodar apenas o necessário, um "log full" vai gerar informação que não serve de nada, gera custos e ineficiência
        ## 2:Saber o que é preciso para acompanhar no projeto, quais logs, por que e o que fazer, processos e etapas bem definidas 

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO" ## AQUI EDITA O QUE SE QUER, SE É WARNING, CRITIAL, INFO E ETC
            )

# Configuração do logger para arquivo de log
logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)  ## O result é o retorno da função onde ela está sendo "chamada", por isso os *args, **kwargs, para n perder nada da função original
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper