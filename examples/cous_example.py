# examples/cous_example.py
# COU API examples

import json
import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import cous_add, cous_view_all, cous_edit, cous_view_one, cous_delete

# cous_add(name: str, description: str, parent_id = None) -> json
print('### cous_add')
name = 'cou test'
description = 'cou test description'
parent_id = None
new_cou = json.loads(cous_add(
    name=name,
    description=description,
    parent_id=parent_id)
)
print(json.dumps(new_cou, indent=4))

# cous_view_all() -> json
print('### cous_view_all')
cous_all = json.loads(cous_view_all())
print(json.dumps(cous_all, indent=4))

# cous_edit(cou_id: int, name: str, description: str, parent_id: str) -> json
print('### cous_edit')
name = 'cou test - edit'
description = 'cou test description - edit'
parent_id = None
cou_id = new_cou.get('Id')
edit_cou = json.loads(cous_edit(
    cou_id=cou_id,
    name=name,
    description=description,
    parent_id=parent_id)
)
print(json.dumps(edit_cou, indent=4))

# cous_view_one(cou_id: int) -> json
print('### cous_view_one')
one_cou = json.loads(cous_view_one(cou_id=cou_id))
print(json.dumps(one_cou, indent=4))

# cous_delete(cou_id: int) -> json
print('### cous_delete')
delete_cou = json.loads(cous_delete(cou_id=cou_id))
print(json.dumps(delete_cou, indent=4))
