# examples/org_identities_example.py
# OrgIdentity API examples

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
ORG_IDENDIFIER_ID = 1234

# org_identities_add() -> dict
print('### org_identities_add')
try:
    new_org_identity = api.org_identities_add()
    print(json.dumps(new_org_identity, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_delete() -> bool
print('### org_identities_delete')
try:
    delete_org_identity = api.org_identities_delete()
    print(json.dumps(delete_org_identity, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_edit() -> bool
print('### org_identities_edit')
try:
    edit_org_identity = api.org_identities_edit()
    print(json.dumps(edit_org_identity, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_view_all() -> dict
print('### org_identities_view_all')
try:
    all_org_identities = api.org_identities_view_all()
    print(json.dumps(all_org_identities, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_view_per_co() -> dict
print('### org_identities_view_per_co')
try:
    per_co_org_identities = api.org_identities_view_per_co()
    print(json.dumps(per_co_org_identities, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_view_per_identitifer(identifier_id: int) -> dict:
print('### org_identities_view_per_identifier')
try:
    per_identifier_org_identities = api.org_identities_view_per_identifier(
        identifier_id=ORG_IDENDIFIER_ID
    )
    print(json.dumps(per_identifier_org_identities, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# org_identities_view_one(org_identity_id: int) -> dict
print('### org_identities_view_one')
try:
    # get first EmailAddresses['Id'] from per_person_email_addresses response
    org_identity_id = int(per_co_org_identities['OrgIdentities'][0]['Id'])
    one_email_address = api.org_identities_view_one(org_identity_id=org_identity_id)
    print(json.dumps(one_email_address, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
