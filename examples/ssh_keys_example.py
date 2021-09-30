# examples/ssh_keys_example.py
# SshKey API examples

import json
import os.path
import sys

from requests.exceptions import HTTPError

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import ssh_keys_add, ssh_keys_delete, ssh_keys_edit, ssh_keys_view_all, \
    ssh_keys_view_per_coperson, ssh_keys_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 1603
PREV_DELETED_KEY_ID = 38
EX_SSH_KEY = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6' \
             'IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJd' \
             'NUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYo' \
             'LNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4F' \
             'O3M4oqg0G+UgFQccXXi1afkJxu7z'
EX_KEY_TYPE = 'ssh-rsa'
EX_COMMENT = 'SshKey API test'

# ssh_keys_add(coperson_id: int, ssh_key: str, key_type: str, comment: str, ssh_key_authenticator_id=None) -> json
print('### ssh_keys_add')
try:
    coperson_id = CO_PERSON_ID
    ssh_key = EX_SSH_KEY
    key_type = EX_KEY_TYPE
    comment = EX_COMMENT
    new_key = ssh_keys_add(
        coperson_id=coperson_id,
        ssh_key=ssh_key,
        key_type=key_type,
        comment=comment
    )
    print(json.dumps(json.loads(new_key), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_all() -> json
print('### ssh_keys_view_all')
try:
    all_keys = ssh_keys_view_all()
    print(json.dumps(json.loads(all_keys), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_per_coperson(coperson_id: int) -> json
print('### ssh_keys_view_per_coperson')
try:
    person_keys = ssh_keys_view_per_coperson(
        coperson_id=CO_PERSON_ID
    )
    print(json.dumps(json.loads(person_keys), indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> json
print('### ssh_keys_view_one')
try:
    # get first SshKeys['Id'] from person_keys response if it exists
    if json.loads(person_keys).get('SshKeys'):
        ssh_key_id = int(json.loads(person_keys).get('SshKeys')[0].get('Id'))
        one_key = ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(json.loads(one_key), indent=4))
    else:
        print('No SSH Keys Found...')
        ssh_key_id = -1
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_edit(ssh_key_id: int, coperson_id: int, ssh_key: str, key_type: str, comment: str,
#               ssh_key_authenticator_id=None) -> json
print('### ssh_keys_edit')
try:
    if ssh_key_id != -1:
        new_comment = 'NEW COMMENT'
        edit_key = ssh_keys_edit(
            ssh_key_id=ssh_key_id,
            coperson_id=CO_PERSON_ID,
            comment=new_comment
        )
        print(edit_key)
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> json
try:
    print('### ssh_keys_view_one')
    if ssh_key_id != -1:
        one_key = ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(json.loads(one_key), indent=4))
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_delete() -> json
print('### ssh_keys_delete')
try:
    # prevent key from being deleted at this time (demo purposes only)
    # ssh_key_id = -1
    if ssh_key_id != -1:
        delete_key = ssh_keys_delete(
            ssh_key_id=ssh_key_id
        )
        print(delete_key)
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> json
print('### ssh_keys_view_one (previously deleted ssh key)')
try:
    # use known previously deleted key (demo purposes only)
    ssh_key_id = PREV_DELETED_KEY_ID
    if ssh_key_id != -1:
        one_key = ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(json.loads(one_key), indent=4))
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
