# examples/coperson_example.py
# CoPerson API examples

import json
import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import coperson_add, coperson_delete, coperson_edit, coperson_find, coperson_match, \
    coperson_view_all, coperson_view_per_identifier, coperson_view_one

# coperson_add() -> json
print('### coperson_add')
new_coperson = json.loads(coperson_add())
print(json.dumps(new_coperson, indent=4))

# coperson_delete() -> json
print('### coperson_delete')
delete_coperson = json.loads(coperson_delete())
print(json.dumps(delete_coperson, indent=4))

# coperson_edit() -> json
print('### coperson_edit')
edit_coperson = json.loads(coperson_edit())
print(json.dumps(edit_coperson, indent=4))

# coperson_find() -> json
print('### coperson_find')
find_coperson = json.loads(coperson_find())
print(json.dumps(find_coperson, indent=4))

# coperson_match(given=None, family=None, mail=None, distinct_by_id=True) -> json
print('### coperson_match')
given = 'michael'
family = None
mail = None
distinct_by_id = True
match_coperson = json.loads(coperson_match(
    given=given,
    family=family,
    mail=mail,
    distinct_by_id=distinct_by_id
))
print(json.dumps(match_coperson, indent=4))

# coperson_view_all() -> json
print('### coperson_view_all')
all_coperson = json.loads(coperson_view_all())
print(json.dumps(all_coperson, indent=4))

# coperson_view_per_identifier(identifier: str, distinct_by_id=True) -> json
print('### coperson_view_per_identifier')
identifier = 'ImPACT1000002'
distinct_by_id = True
identifier_coperson = json.loads(coperson_view_per_identifier(
    identifier=identifier,
    distinct_by_id=True
))
print(json.dumps(identifier_coperson, indent=4))

# coperson_view_one(coperson_id: int) -> json
print('### coperson_view_one')
# get first CoPeople['Id'] from all_coperson response
if all_coperson['CoPeople']:
    coperson_id = int(all_coperson['CoPeople'][0]['Id'])
    one_coperson = json.loads(coperson_view_one(coperson_id=coperson_id))
    print(json.dumps(one_coperson, indent=4))
else:
    print('No CoPeople Found...')
