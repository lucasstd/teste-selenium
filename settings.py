import os
from os.path import join, dirname
# Third-party
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def config():
    """ 
        Mantem todos as variaveis necessarias para executar a apicação
        Caso alguma não esteja aqui, irá dar erro antes de executar a aplicação
    """ 
    WAIT_FOR_RSC_ON_PAGE_LOADS = os.environ.get("WAIT_FOR_RSC_ON_PAGE_LOADS")
    TIMEOUT = os.environ.get("TIMEOUT")
    
# Isso é como um Export default do Javascript
# para não precisar "instanciar" sempre o config
configs = config()
