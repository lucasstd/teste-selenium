import os
from os.path import join, dirname
# Third-party
import dotenv

dotenv_path = dotenv.find_dotenv('config.dotenv')
dotenv.load_dotenv(dotenv_path)


def config():
    """ 
        Mantem todos as variaveis necessarias para executar a apicação
        Caso alguma não esteja aqui, irá dar erro antes de executar a aplicação
    """
    return {
        "BASE_URL": os.environ.get("BASE_URL"),  # URL base para teste do Sicredi
        "API_URL": os.environ.get("API_URL")  # API_URL para testes na API
    }
    
# Isso é como um Export default do Javascript
# para não precisar "instanciar" sempre o config
configs = config()
