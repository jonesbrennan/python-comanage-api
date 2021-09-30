# examples/names_example.py
# Name API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import names_add, names_delete, names_edit, names_view_all, names_view_per_person, names_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# names_add() -> json
print('### names_add')
try:
    new_name = names_add()
    print(json.dumps(json.loads(new_name), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_delete() -> json
print('### names_delete')
try:
    delete_name = names_delete()
    print(json.dumps(json.loads(delete_name), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_edit() -> json
print('### names_edit')
try:
    edit_name = names_edit()
    print(json.dumps(json.loads(edit_name), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_all() -> json
print('### names_view_all')
try:
    all_names = names_view_all()
    print(json.dumps(json.loads(all_names), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_per_person(person_type: str, person_id: int) -> json
print('### names_view_per_person')
try:
    person_names = names_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(json.loads(person_names), indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_one(name_id: int) -> json
print('### names_view_one')
try:
    name_id = int(json.loads(person_names)['Names'][0]['Id'])
    one_name = json.loads(names_view_one(name_id=name_id))
    print(json.dumps(one_name, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
