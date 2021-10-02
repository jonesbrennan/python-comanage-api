# examples/ssh_keys_example.py
# SshKey API examples

import json
import os
import sys

from dotenv import load_dotenv
from requests.exceptions import HTTPError

load_dotenv()

COMANAGE_API_USER = os.getenv('COMANAGE_API_USER')
COMANAGE_API_PASS = os.getenv('COMANAGE_API_PASS')
COMANAGE_API_CO_NAME = os.getenv('COMANAGE_API_CO_NAME')
COMANAGE_API_CO_ID = int(os.getenv('COMANAGE_API_CO_ID'))
COMANAGE_API_URL = os.getenv('COMANAGE_API_URL')
COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID = int(os.getenv('COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID'))

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from comanage_api import ComanageApi

api = ComanageApi(
    co_api_url=COMANAGE_API_URL,
    co_api_user=COMANAGE_API_USER,
    co_api_pass=COMANAGE_API_PASS,
    co_api_org_id=COMANAGE_API_CO_ID,
    co_api_org_name=COMANAGE_API_CO_NAME,
    co_ssh_key_authenticator_id=COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID
)

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

# ssh_keys_add(coperson_id: int, ssh_key: str, key_type: str, comment: str,
#              ssh_key_authenticator_id: int = None) -> dict
print('### ssh_keys_add')
try:
    coperson_id = CO_PERSON_ID
    ssh_key = EX_SSH_KEY
    key_type = EX_KEY_TYPE
    comment = EX_COMMENT
    new_key = api.ssh_keys_add(
        coperson_id=coperson_id,
        ssh_key=ssh_key,
        key_type=key_type,
        comment=comment
    )
    print(json.dumps(new_key, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_all() -> dict
print('### ssh_keys_view_all')
try:
    all_keys = api.ssh_keys_view_all()
    print(json.dumps(all_keys, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_per_coperson(coperson_id: int) -> dict
print('### ssh_keys_view_per_coperson')
try:
    person_keys = api.ssh_keys_view_per_coperson(
        coperson_id=CO_PERSON_ID
    )
    print(json.dumps(person_keys, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> dict
print('### ssh_keys_view_one')
try:
    # get first SshKeys['Id'] from person_keys response if it exists
    if person_keys.get('SshKeys'):
        ssh_key_id = int(json.loads(person_keys).get('SshKeys')[0].get('Id'))
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
        ssh_key_id = -1
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_edit(ssh_key_id: int, coperson_id: int = None, ssh_key: str = None, key_type: str = None,
#               comment: str = None, ssh_key_authenticator_id: int = None) -> bool
print('### ssh_keys_edit')
try:
    if ssh_key_id != -1:
        new_comment = 'NEW COMMENT'
        edit_key = api.ssh_keys_edit(
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

# ssh_keys_view_one(ssh_key_id: int) -> dict
try:
    print('### ssh_keys_view_one')
    if ssh_key_id != -1:
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_delete() -> bool
print('### ssh_keys_delete')
try:
    # prevent key from being deleted at this time (demo purposes only)
    # ssh_key_id = -1
    if ssh_key_id != -1:
        delete_key = api.ssh_keys_delete(
            ssh_key_id=ssh_key_id
        )
        print(delete_key)
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> dict
print('### ssh_keys_view_one (previously deleted ssh key)')
try:
    # use known previously deleted key (demo purposes only)
    ssh_key_id = PREV_DELETED_KEY_ID
    if ssh_key_id != -1:
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
