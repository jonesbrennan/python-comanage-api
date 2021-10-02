# examples/copersone_roles_example.py
# CoPersonRoles API examples

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
COU_ID = 39

# # copersonroles_add(coperson_id: int, cou_id: int, status: str = None, affiliation: str = None) -> dict
print('### copersonroles_add')
try:
    coperson_id = CO_PERSON_ID
    cou_id = COU_ID
    status = 'PendingApproval'
    affiliation = 'student'
    roles_add = api.copersonroles_add(
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(json.dumps(roles_add, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_one(copersonrole_id: int) -> dict
print('### copersonroles_view_one')
try:
    copersonrole_id = roles_add.get('Id')
    roles_view_one = api.copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_edit(copersonrole_id: int, coperson_id: int = None, cou_id: int = None, status: str = None,
#                    affiliation: str = None) -> bool
print('### copersonroles_edit')
try:
    status = 'Active'
    affiliation = 'member'
    roles_edit = api.copersonroles_edit(
        copersonrole_id=copersonrole_id,
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(roles_edit)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_one(copersonrole_id: int) -> dict
print('### copersonroles_view_one')
try:
    roles_view_one = api.copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_all() -> dict
print('### copersonroles_view_all')
try:
    roles_all = api.copersonroles_view_all()
    print(json.dumps(roles_all, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_per_coperson(coperson_id: int) -> dict
print('### copersonroles_view_per_coperson')
try:
    roles_view_per_coperson = api.copersonroles_view_per_coperson(coperson_id=coperson_id)
    print(json.dumps(roles_view_per_coperson, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_per_cou(cou_id: int) -> dict
print('### copersonroles_view_per_cou')
try:
    roles_view_per_cou = api.copersonroles_view_per_cou(cou_id=cou_id)
    print(json.dumps(roles_view_per_cou, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_delete(copersonrole_id: int) -> bool
print('### copersonroles_delete')
try:
    roles_delete = api.copersonroles_delete(copersonrole_id=copersonrole_id)
    print(roles_delete)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_one(copersonrole_id: int) -> dict
print('### copersonroles_view_one (previously deleted co person role)')
try:
    roles_view_one = api.copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
