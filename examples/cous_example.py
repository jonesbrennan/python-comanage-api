# examples/cous_example.py
# COU API examples

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

# cous_add(name: str, description: str, parent_id: int = None) -> dict
print('### cous_add')
try:
    name = 'cou test'
    description = 'cou test description'
    parent_id = None
    new_cou = api.cous_add(
        name=name,
        description=description,
        parent_id=parent_id
    )
    new_cou_id = new_cou.get('Id')
    print(json.dumps(new_cou, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_all() -> json
print('### cous_view_all')
try:
    cous_all = api.cous_view_all()
    print(json.dumps(cous_all, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_edit(cou_id: int, name: str = None, description: str = None, parent_id: int = None) -> bool
print('### cous_edit')
try:
    name = 'cou test - edited'
    description = 'cou test description - edited'
    parent_id = 0
    cou_id = new_cou_id
    edit_cou = api.cous_edit(
        cou_id=cou_id,
        name=name,
        description=description,
        parent_id=parent_id
    )
    print(edit_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_one(cou_id: int) -> dict
print('### cous_view_one')
try:
    one_cou = api.cous_view_one(cou_id=new_cou_id)
    print(json.dumps(one_cou, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_delete(cou_id: int) -> bool
print('### cous_delete')
try:
    delete_cou = api.cous_delete(cou_id=new_cou_id)
    print(delete_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_one(cou_id: int) -> dict
print('### cous_view_one (previously deleted cou)')
try:
    one_cou = api.cous_view_one(cou_id=new_cou_id)
    print(json.dumps(one_cou, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
