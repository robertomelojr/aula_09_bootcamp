## soma 
from loguru import logger
from sys import stderr
from functools import wraps

# Removendo os handlers existentes para evitar duplicação
logger.remove()

##logger.debug("Aviso para o Dev (ou eu mesmo) no futuro")
## logger.info("Informação importante do processo")
## logger.warning("Algo vai parar de funcionar no futuro!")
## logger.error("Aconteceu uma falha")
## logger.critical("Aconteceu uma falha que aborta a aplicação")

# Configuração do logger para stderr

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# Configuração do logger para arquivo de log
logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )
def soma (x,y):
    
    try:
        soma = x + y
        logger.info(f"Os valores foram válidos, o resultado foi {soma}")
        return soma
    except:
        logger.critical("Você tem que inserir valores válidos na aplicação!")

soma(2,"3")

soma(2,3)

soma("a","b")