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

# # coperson_roles_add(coperson_id: int, cou_id: int, status: str = None, affiliation: str = None) -> dict
print('### coperson_roles_add')
try:
    coperson_id = CO_PERSON_ID
    cou_id = COU_ID
    status = 'PendingApproval'
    affiliation = 'student'
    roles_add = api.coperson_roles_add(
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(json.dumps(roles_add, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one')
try:
    coperson_role_id = roles_add.get('Id')
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_edit(coperson_role_id: int, coperson_id: int = None, cou_id: int = None, status: str = None,
#                    affiliation: str = None) -> bool
print('### coperson_roles_edit')
try:
    status = 'Active'
    affiliation = 'member'
    roles_edit = api.coperson_roles_edit(
        coperson_role_id=coperson_role_id,
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(roles_edit)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one')
try:
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_all() -> dict
print('### coperson_roles_view_all')
try:
    roles_all = api.coperson_roles_view_all()
    print(json.dumps(roles_all, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_per_coperson(coperson_id: int) -> dict
print('### coperson_roles_view_per_coperson')
try:
    roles_view_per_coperson = api.coperson_roles_view_per_coperson(coperson_id=coperson_id)
    print(json.dumps(roles_view_per_coperson, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_per_cou(cou_id: int) -> dict
print('### coperson_roles_view_per_cou')
try:
    roles_view_per_cou = api.coperson_roles_view_per_cou(cou_id=cou_id)
    print(json.dumps(roles_view_per_cou, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_delete(coperson_role_id: int) -> bool
print('### coperson_roles_delete')
try:
    roles_delete = api.coperson_roles_delete(coperson_role_id=coperson_role_id)
    print(roles_delete)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one (previously deleted co person role)')
try:
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
