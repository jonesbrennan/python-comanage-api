# examples/identifiers_example.py
# Identifier API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import identifiers_add, identifiers_assign, identifiers_delete, identifiers_edit, \
    identifiers_view_all, identifiers_view_per_entity, identifiers_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603

# identifiers_add() -> json
print('### identifiers_add')
try:
    new_identifier = identifiers_add()
    print(json.dumps(json.loads(new_identifier), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_assign() -> bool
print('### identifiers_assign')
try:
    assign_identifier = identifiers_assign()
    print(json.dumps(json.loads(assign_identifier), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_delete() -> bool
print('### identifiers_delete')
try:
    delete_identifier = identifiers_delete()
    print(json.dumps(json.loads(delete_identifier), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_edit() -> bool
print('### identifiers_edit')
try:
    edit_identifier = identifiers_edit()
    print(json.dumps(json.loads(edit_identifier), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_all() -> json
print('### identifiers_view_all')
try:
    all_identifiers = identifiers_view_all()
    print(json.dumps(json.loads(all_identifiers), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_per_entity(entity_type: str, entity_id: int) -> json:
print('### identifiers_view_per_entity')
try:
    entity_identifiers = identifiers_view_per_entity(
        entity_type='copersonid',
        entity_id=CO_PERSON_ID
    )
    print(json.dumps(json.loads(entity_identifiers), indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_one(identifier_id: int) -> json
print('### identifiers_view_one')
try:
    # get first Identifiers['Id'] from entity_identifiers response
    identifier_id = int(json.loads(entity_identifiers)['Identifiers'][0]['Id'])
    one_identifier = identifiers_view_one(identifier_id=identifier_id)
    print(json.dumps(json.loads(one_identifier), indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
