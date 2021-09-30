# examples/copersone_roles_example.py
# CoPersonRoles API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import copersonroles_add, copersonroles_delete, copersonroles_edit, copersonroles_view_all, \
    copersonroles_view_per_coperson, copersonroles_view_per_cou, copersonroles_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603
COU_ID = 39

# # copersonroles_add(coperson_id: int, cou_id: int, status=None, affiliation=None) -> json
print('### copersonroles_add')
try:
    coperson_id = CO_PERSON_ID
    cou_id = COU_ID
    status = 'PendingApproval'
    affiliation = 'student'
    roles_add = copersonroles_add(
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(json.dumps(json.loads(roles_add), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
try:
    copersonrole_id = json.loads(roles_add).get('Id')
    roles_view_one = copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(json.loads(roles_view_one), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_edit(copersonrole_id: int, coperson_id=None, cou_id=None, status=None, affiliation=None) -> bool
print('### copersonroles_edit')
try:
    status = 'Active'
    affiliation = 'member'
    roles_edit = copersonroles_edit(
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

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
try:
    roles_view_one = copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(json.loads(roles_view_one), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_all() -> json
print('### copersonroles_view_all')
try:
    roles_all = copersonroles_view_all()
    print(json.dumps(json.loads(roles_all), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_per_coperson(coperson_id: int) -> json
print('### copersonroles_view_per_coperson')
try:
    roles_view_per_coperson = copersonroles_view_per_coperson(coperson_id=coperson_id)
    print(json.dumps(json.loads(roles_view_per_coperson), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_per_cou(cou_id: int) -> json
print('### copersonroles_view_per_cou')
try:
    roles_view_per_cou = copersonroles_view_per_cou(cou_id=cou_id)
    print(json.dumps(json.loads(roles_view_per_cou), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_delete(copersonrole_id: int) -> bool
print('### copersonroles_delete')
try:
    roles_delete = copersonroles_delete(copersonrole_id=copersonrole_id)
    print(roles_delete)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
try:
    roles_view_one = copersonroles_view_one(copersonrole_id=copersonrole_id)
    print(json.dumps(json.loads(roles_view_one), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
