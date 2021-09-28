# examples/copersone_roles_example.py
# CoPersonRoles API examples

import json
import os.path
import sys

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
coperson_id = CO_PERSON_ID
cou_id = COU_ID
status = 'PendingApproval'
affiliation = 'student'
roles_add = json.loads(
    copersonroles_add(coperson_id=coperson_id, cou_id=cou_id, status=status, affiliation=affiliation))
print(json.dumps(roles_add, indent=4))

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
copersonrole_id = roles_add.get('Id')
roles_view_one = json.loads(copersonroles_view_one(copersonrole_id=copersonrole_id))
print(json.dumps(roles_view_one, indent=4))

# copersonroles_edit(copersonrole_id: int, coperson_id: int, cou_id: int, status=None, affiliation=None) -> json
print('### copersonroles_edit')
status = 'Active'
affiliation = 'member'
roles_edit = json.loads(
    copersonroles_edit(copersonrole_id=copersonrole_id, coperson_id=coperson_id, cou_id=cou_id, status=status,
                       affiliation=affiliation))
print(json.dumps(roles_edit, indent=4))

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
roles_view_one = json.loads(copersonroles_view_one(copersonrole_id=copersonrole_id))
print(json.dumps(roles_view_one, indent=4))

# copersonroles_view_all() -> json
print('### copersonroles_view_all')
roles_all = json.loads(copersonroles_view_all())
print(json.dumps(roles_all, indent=4))

# copersonroles_view_per_coperson(coperson_id: int) -> json
print('### copersonroles_view_per_coperson')
roles_view_per_coperson = json.loads(copersonroles_view_per_coperson(coperson_id=coperson_id))
print(json.dumps(roles_view_per_coperson, indent=4))

# copersonroles_view_per_cou(cou_id: int) -> json
print('### copersonroles_view_per_cou')
roles_view_per_cou = json.loads(copersonroles_view_per_cou(cou_id=cou_id))
print(json.dumps(roles_view_per_cou, indent=4))

# copersonroles_delete(copersonrole_id: int) -> json
print('### copersonroles_delete')
roles_delete = json.loads(copersonroles_delete(copersonrole_id=copersonrole_id))
print(json.dumps(roles_delete, indent=4))

# copersonroles_view_one(copersonrole_id: int) -> json
print('### copersonroles_view_one')
roles_view_one = json.loads(copersonroles_view_one(copersonrole_id=copersonrole_id))
print(json.dumps(roles_view_one, indent=4))
