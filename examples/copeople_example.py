# examples/copeople_example.py
# CoPerson API examples

import json
import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import copeople_add, copeople_delete, copeople_edit, copeople_find, copeople_match, \
    copeople_view_all, copeople_view_per_identifier, copeople_view_one

# copeople_add() -> json
print('### copeople_add')
new_copeople = json.loads(copeople_add())
print(json.dumps(new_copeople, indent=4))

# copeople_delete() -> json
print('### copeople_delete')
delete_copeople = json.loads(copeople_delete())
print(json.dumps(delete_copeople, indent=4))

# copeople_edit() -> json
print('### copeople_edit')
edit_copeople = json.loads(copeople_edit())
print(json.dumps(edit_copeople, indent=4))

# copeople_find() -> json
print('### copeople_find')
find_copeople = json.loads(copeople_find())
print(json.dumps(find_copeople, indent=4))

# copeople_match(given=None, family=None, mail=None, distinct_by_id=True) -> json
print('### copeople_match')
given = 'michael'
family = None
mail = None
distinct_by_id = True
match_copeople = json.loads(copeople_match(
    given=given,
    family=family,
    mail=mail,
    distinct_by_id=distinct_by_id
))
print(json.dumps(match_copeople, indent=4))

# copeople_view_all() -> json
print('### copeople_view_all')
all_copeople = json.loads(copeople_view_all())
print(json.dumps(all_copeople, indent=4))

# copeople_view_per_identifier(identifier: str, distinct_by_id=True) -> json
print('### copeople_view_per_identifier')
identifier = 'ImPACT1000002'
distinct_by_id = True
identifier_copeople = json.loads(copeople_view_per_identifier(
    identifier=identifier,
    distinct_by_id=True
))
print(json.dumps(identifier_copeople, indent=4))

# copeople_view_one(copeople_id: int) -> json
print('### copeople_view_one')
# get first CoPeople['Id'] from all_copeople response
if all_copeople['CoPeople']:
    copeople_id = int(all_copeople['CoPeople'][0]['Id'])
    one_copeople = json.loads(copeople_view_one(copeople_id=copeople_id))
    print(json.dumps(one_copeople, indent=4))
else:
    print('No CoPeople Found...')
