# examples/cous_example.py
# COU API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import cous_add, cous_view_all, cous_edit, cous_view_one, cous_delete

# cous_add(name: str, description: str, parent_id = None) -> json
print('### cous_add')
try:
    name = 'cou test'
    description = 'cou test description'
    parent_id = None
    new_cou = cous_add(
        name=name,
        description=description,
        parent_id=parent_id
    )
    new_cou_id = json.loads(new_cou).get('Id')
    print(json.dumps(json.loads(new_cou), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_all() -> json
print('### cous_view_all')
try:
    cous_all = cous_view_all()
    print(json.dumps(json.loads(cous_all), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_edit(cou_id: int, name=None, description=None, parent_id=None) -> bool
print('### cous_edit')
try:
    name = 'cou test - edited'
    description = 'cou test description - edited'
    parent_id = 0
    cou_id = new_cou_id
    edit_cou = cous_edit(
        cou_id=cou_id,
        name=name,
        description=description,
        parent_id=parent_id
    )
    print(edit_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_one(cou_id: int) -> json
print('### cous_view_one')
try:
    one_cou = cous_view_one(cou_id=new_cou_id)
    print(json.dumps(json.loads(one_cou), indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_delete(cou_id: int) -> bool
print('### cous_delete')
try:
    delete_cou = cous_delete(cou_id=new_cou_id)
    print(delete_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
