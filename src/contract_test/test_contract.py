import pytest
import logging
import json
import urllib.request
# Local libraries
from ..settings import configs
from .json_schema.jsonschema_validator import validate_json


""" Describe: Testar JSON da API """
def test_contract():
    # Abrir o link nas variaveis de ambiente "API_URL"
    with urllib.request.urlopen(configs['API_URL']) as url:
        data = json.loads(url.read().decode())
    # Garantir que a validação não volte nenhum erro
    assert not validate_json(data)
