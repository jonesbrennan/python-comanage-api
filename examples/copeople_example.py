# examples/copeople_example.py
# CoPerson API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import copeople_add, copeople_delete, copeople_edit, copeople_find, copeople_match, \
    copeople_view_all, copeople_view_per_identifier, copeople_view_one

# copeople_add() -> json
print('### copeople_add')
try:
    new_copeople = copeople_add()
    print(json.dumps(json.loads(new_copeople), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_delete() -> json
print('### copeople_delete')
try:
    delete_copeople = copeople_delete()
    print(json.dumps(json.loads(delete_copeople), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_edit() -> json
print('### copeople_edit')
try:
    edit_copeople = copeople_edit()
    print(json.dumps(json.loads(edit_copeople), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_find() -> json
print('### copeople_find')
try:
    find_copeople = copeople_find()
    print(json.dumps(json.loads(find_copeople), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_match(given=None, family=None, mail=None, distinct_by_id=True) -> json
print('### copeople_match')
try:
    given = 'michael'
    family = None
    mail = None
    distinct_by_id = True
    match_copeople = copeople_match(
        given=given,
        family=family,
        mail=mail,
        distinct_by_id=distinct_by_id
    )
    print(json.dumps(json.loads(match_copeople), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_all() -> json
print('### copeople_view_all')
try:
    all_copeople = json.loads(copeople_view_all())
    print(json.dumps(all_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_per_identifier(identifier: str, distinct_by_id=True) -> json
print('### copeople_view_per_identifier')
try:
    identifier = 'ImPACT1000002'
    distinct_by_id = True
    identifier_copeople = json.loads(copeople_view_per_identifier(
        identifier=identifier,
        distinct_by_id=True
    ))
    print(json.dumps(identifier_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_one(coperson_id: int) -> json
print('### copeople_view_one')
try:
    # get first CoPeople['Id'] from all_copeople response
    if all_copeople['CoPeople']:
        coperson_id = int(all_copeople['CoPeople'][0]['Id'])
        one_copeople = json.loads(copeople_view_one(coperson_id=coperson_id))
        print(json.dumps(one_copeople, indent=4))
    else:
        print('No CoPeople Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
