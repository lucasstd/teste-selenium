import json
import logging
# from jsonschema import validate
from jsonschema import Draft7Validator
import jsonschema
from os.path import dirname

schema_path = f'{dirname(__file__)}/base_schema.json'

with open(schema_path, 'r') as file:
    schema = json.load(file)


def validate_json(json_to_compare: 'Json', log=None):
    """ retorna a lista de erros do json passado """
    try:
        log = log if log else logging
        v = Draft7Validator(schema)
        errors = sorted(v.iter_errors(json_to_compare), key=lambda e: e.path)
        if errors:
            msg = list()
            msg.append('Erro validando')
            for error in errors:
                msg.append(error.message.replace('\\', ''))
            raise ValueError(' | '.join(msg))
        log.debug(f'[JSON-Schema] JSON valido: [{json_to_compare}] para {schema}')
    except Exception as e:
        log.error(f'[JSONSchema] Error - {e}', extra=json_to_compare)
        return e
