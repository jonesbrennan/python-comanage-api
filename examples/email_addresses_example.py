# examples/email_addresses_example.py
# EmailAddress API examples

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

# email_addresses_add() -> dict
print('### email_addresses_add')
try:
    new_email_address = api.email_addresses_add()
    print(json.dumps(new_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_delete() -> bool
print('### email_addresses_delete')
try:
    delete_email_address = api.email_addresses_delete()
    print(json.dumps(delete_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_edit() -> bool
print('### email_addresses_edit')
try:
    edit_email_address = api.email_addresses_edit()
    print(json.dumps(edit_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_all() -> dict
print('### email_addresses_view_all')
try:
    all_email_addresses = api.email_addresses_view_all()
    print(json.dumps(all_email_addresses, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_per_person(person_type: str, person_id: int) -> dict:
print('### email_addresses_view_per_person')
try:
    per_person_email_addresses = api.email_addresses_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(per_person_email_addresses, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_one(email_address_id: int) -> dict
print('### email_addresses_view_one')
try:
    # get first EmailAddresses['Id'] from per_person_email_addresses response
    email_address_id = int(per_person_email_addresses['EmailAddresses'][0]['Id'])
    one_email_address = api.email_addresses_view_one(email_address_id=email_address_id)
    print(json.dumps(one_email_address, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
