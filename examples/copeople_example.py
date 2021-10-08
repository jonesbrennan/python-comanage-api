# examples/copeople_example.py
# CoPerson API examples

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

# copeople_add() -> dict
print('### copeople_add')
try:
    new_copeople = api.copeople_add()
    print(json.dumps(new_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_delete() -> bool
print('### copeople_delete')
try:
    delete_copeople = api.copeople_delete()
    print(json.dumps(delete_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_edit() -> bool
print('### copeople_edit')
try:
    edit_copeople = api.copeople_edit()
    print(json.dumps(edit_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_find() -> dict
print('### copeople_find')
try:
    find_copeople = api.copeople_find()
    print(json.dumps(find_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_match(given: str = None, family: str = None, mail: str = None, distinct_by_id: bool = True) -> dict
print('### copeople_match')
try:
    given = 'michael'
    family = None
    mail = None
    distinct_by_id = True
    match_copeople = api.copeople_match(
        given=given,
        family=family,
        mail=mail,
        distinct_by_id=distinct_by_id
    )
    print(json.dumps(match_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_all() -> dict
print('### copeople_view_all')
try:
    all_copeople = api.copeople_view_all()
    print(json.dumps(all_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_per_co() -> dict
print('### copeople_view_per_co')
try:
    per_co_copeople = api.copeople_view_per_co()
    print(json.dumps(per_co_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_per_identifier(identifier: str, distinct_by_id: bool = True) -> dict
print('### copeople_view_per_identifier')
try:
    identifier = 'ImPACT1000002'
    distinct_by_id = True
    identifier_copeople = api.copeople_view_per_identifier(
        identifier=identifier,
        distinct_by_id=True
    )
    print(json.dumps(identifier_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_one(coperson_id: int) -> dict
print('### copeople_view_one')
try:
    # get first CoPeople['Id'] from all_copeople response
    if per_co_copeople['CoPeople']:
        coperson_id = int(per_co_copeople['CoPeople'][0]['Id'])
        one_copeople = api.copeople_view_one(coperson_id=coperson_id)
        print(json.dumps(one_copeople, indent=4))
    else:
        print('No CoPeople Found...')
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
