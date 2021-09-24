# examples/copeople_example.py
# CoPerson API examples

import json
import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import identifiers_add, identifiers_assign, identifiers_delete, identifiers_edit, \
    identifiers_view_all, identifiers_view_per_entity, identifiers_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# identifiers_add() -> json
print('### identifiers_add')
new_identifier = json.loads(identifiers_add())
print(json.dumps(new_identifier, indent=4))

# identifiers_assign() -> json
print('### identifiers_assign')
assign_identifier = json.loads(identifiers_assign())
print(json.dumps(assign_identifier, indent=4))

# identifiers_delete() -> json
print('### identifiers_delete')
delete_identifier = json.loads(identifiers_delete())
print(json.dumps(delete_identifier, indent=4))

# identifiers_edit() -> json
print('### identifiers_edit')
edit_identifer = json.loads(identifiers_edit())
print(json.dumps(edit_identifer, indent=4))

# identifiers_view_all() -> json
print('### identifiers_view_all')
all_identifiers = json.loads(identifiers_view_all())
print(json.dumps(all_identifiers, indent=4))

# identifiers_view_per_entity(entity_type: str, entity_id: int) -> json:
print('### identifiers_view_per_entity')
entity_identifiers = json.loads(identifiers_view_per_entity(
    entity_type='copersonid',
    entity_id=CO_PERSON_ID
))
print(json.dumps(entity_identifiers, indent=4))

# identifiers_view_one(identifier_id: int) -> json
print('### identifiers_view_one')
# get first Identifiers['Id'] from entity_identifiers response
if entity_identifiers['Identifiers']:
    identifier_id = int(entity_identifiers['Identifiers'][0]['Id'])
    one_identifier = json.loads(identifiers_view_one(identifier_id=identifier_id))
    print(json.dumps(one_identifier, indent=4))
else:
    print('No Identifiers Found...')
