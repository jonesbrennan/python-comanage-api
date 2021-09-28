# examples/names_example.py
# Name API examples

import json
import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import names_add, names_delete, names_edit, names_view_all, names_view_per_person, names_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# names_add() -> json
print('### names_add')
new_name = json.loads(names_add())
print(json.dumps(new_name, indent=4))

# names_delete() -> json
print('### names_delete')
delete_name = json.loads(names_delete())
print(json.dumps(delete_name, indent=4))

# names_edit() -> json
print('### names_edit')
edit_name = json.loads(names_edit())
print(json.dumps(edit_name, indent=4))

# names_view_all() -> json
print('### names_view_all')
all_names = json.loads(names_view_all())
print(json.dumps(all_names, indent=4))

# names_view_per_person(person_type: str, person_id: int) -> json
print('### names_view_per_person')
person_names = json.loads(names_view_per_person(
    person_type='copersonid',
    person_id=CO_PERSON_ID
))
print(json.dumps(person_names, indent=4))

# names_view_one(name_id: int) -> json
print('### names_view_one')
# get first Names['Id'] from person_names response
if person_names['Names']:
    name_id = int(person_names['Names'][0]['Id'])
    one_name = json.loads(names_view_one(name_id=name_id))
    print(json.dumps(one_name, indent=4))
else:
    print('No Identifiers Found...')
