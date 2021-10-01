# examples/names_example.py
# Name API examples

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

api = ComanageApi(co_api_url=COMANAGE_API_URL,
                  co_api_user=COMANAGE_API_USER,
                  co_api_pass=COMANAGE_API_PASS,
                  co_api_org_id=COMANAGE_API_CO_ID,
                  co_api_org_name=COMANAGE_API_CO_NAME,
                  co_ssh_key_authenticator_id=COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID
                  )

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# names_add() -> json
print('### names_add')
try:
    new_name = api.names_add()
    print(json.dumps(new_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_delete() -> bool
print('### names_delete')
try:
    delete_name = api.names_delete()
    print(json.dumps(delete_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_edit() -> bool
print('### names_edit')
try:
    edit_name = api.names_edit()
    print(json.dumps(edit_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_all() -> json
print('### names_view_all')
try:
    all_names = api.names_view_all()
    print(json.dumps(all_names, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_per_person(person_type: str, person_id: int) -> json
print('### names_view_per_person')
try:
    person_names = api.names_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(person_names, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_one(name_id: int) -> json
print('### names_view_one')
try:
    name_id = int(person_names['Names'][0]['Id'])
    one_name = api.names_view_one(name_id=name_id)
    print(json.dumps(one_name, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
