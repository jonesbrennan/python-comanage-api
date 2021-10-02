# examples/identifiers_example.py
# Identifier API examples

import json
import os
import sys

from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

COMANAGE_API_USER = os.getenv('COMANAGE_API_USER')
COMANAGE_API_PASS = os.getenv('COMANAGE_API_PASS')
COMANAGE_API_CO_NAME = os.getenv('COMANAGE_API_CO_NAME')
COMANAGE_API_CO_ID = int(os.getenv('COMANAGE_API_CO_ID'))
COMANAGE_API_URL = os.getenv('COMANAGE_API_URL')
COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID = int(os.getenv('COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID'))

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import ComanageApi

api = ComanageApi(
    co_api_url=COMANAGE_API_URL,
    co_api_user=COMANAGE_API_USER,
    co_api_pass=COMANAGE_API_PASS,
    co_api_org_id=COMANAGE_API_CO_ID,
    co_api_org_name=COMANAGE_API_CO_NAME,
    co_ssh_key_authenticator_id=COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID
)

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# identifiers_add() -> dict
print('### identifiers_add')
try:
    new_identifier = api.identifiers_add()
    print(json.dumps(new_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_assign() -> bool
print('### identifiers_assign')
try:
    assign_identifier = api.identifiers_assign()
    print(json.dumps(assign_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_delete() -> bool
print('### identifiers_delete')
try:
    delete_identifier = api.identifiers_delete()
    print(json.dumps(delete_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_edit() -> bool
print('### identifiers_edit')
try:
    edit_identifier = api.identifiers_edit()
    print(json.dumps(edit_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_all() -> json
print('### identifiers_view_all')
try:
    all_identifiers = api.identifiers_view_all()
    print(json.dumps(all_identifiers, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_per_entity(entity_type: str, entity_id: int) -> dict:
print('### identifiers_view_per_entity')
try:
    entity_identifiers = api.identifiers_view_per_entity(
        entity_type='copersonid',
        entity_id=CO_PERSON_ID
    )
    print(json.dumps(entity_identifiers, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_one(identifier_id: int) -> dict
print('### identifiers_view_one')
try:
    # get first Identifiers['Id'] from entity_identifiers response
    identifier_id = int(entity_identifiers['Identifiers'][0]['Id'])
    one_identifier = api.identifiers_view_one(identifier_id=identifier_id)
    print(json.dumps(one_identifier, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
