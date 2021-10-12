# examples/cous_example.py
# COU API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# cous_add(name: str, description: str, parent_id: int = None) -> dict
print('### cous_add')
try:
    name = 'cou test'
    description = 'cou test description'
    parent_id = None
    new_cou = api.cous_add(
        name=name,
        description=description,
        parent_id=parent_id
    )
    new_cou_id = new_cou.get('Id')
    print(json.dumps(new_cou, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_all() -> dict
print('### cous_view_all')
try:
    cous_all = api.cous_view_all()
    print(json.dumps(cous_all, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_per_co() -> dict
print('### cous_view_per_co')
try:
    cous_per_co = api.cous_view_per_co()
    print(json.dumps(cous_per_co, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_edit(cou_id: int, name: str = None, description: str = None, parent_id: int = None) -> bool
print('### cous_edit')
try:
    name = 'cou test - edited'
    description = 'cou test description - edited'
    parent_id = 0
    cou_id = new_cou_id
    edit_cou = api.cous_edit(
        cou_id=cou_id,
        name=name,
        description=description,
        parent_id=parent_id
    )
    print(edit_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_one(cou_id: int) -> dict
print('### cous_view_one')
try:
    one_cou = api.cous_view_one(cou_id=new_cou_id)
    print(json.dumps(one_cou, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_delete(cou_id: int) -> bool
print('### cous_delete')
try:
    delete_cou = api.cous_delete(cou_id=new_cou_id)
    print(delete_cou)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cous_view_one(cou_id: int) -> dict
print('### cous_view_one (previously deleted cou)')
try:
    one_cou = api.cous_view_one(cou_id=new_cou_id)
    print(json.dumps(one_cou, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
