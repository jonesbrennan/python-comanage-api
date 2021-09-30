import os

import requests_mock
from dotenv import load_dotenv
from requests import Session

load_dotenv()

CO_API_USER = os.getenv('COMANAGE_API_USER')
CO_API_PASS = os.getenv('COMANAGE_API_PASS')
CO_API_ORG_NAME = os.getenv('COMANAGE_CO_NAME')
CO_API_ORG_ID = os.getenv('COMANAGE_CO_ID')
CO_API_URL = os.getenv('COMANAGE_URL')
if CO_API_URL.endswith('/'):
    CO_API_URL = CO_API_URL[:-1]
CO_SSH_KEY_AUTHENTICATOR_ID = os.getenv('COMANAGE_SSH_KEY_AUTHENTICATOR_ID')

STATUS_OPTIONS = ['Active', 'Approved', 'Confirmed', 'Declined', 'Deleted', 'Denied', 'Duplicate', 'Expired',
                  'GracePeriod', 'Invited', 'Pending', 'PendingApproval', 'PendingConfirmation', 'Suspended']

AFFILIATION_OPTIONS = ['affiliate', 'alum', 'employee', 'faculty', 'member', 'staff', 'student']

ENTITY_OPTIONS = ['codeptid', 'cogroupid', 'copersonid', 'organizationid', 'orgidentityid']

PERSON_OPTIONS = ['copersonid', 'orgidentityid']

SSH_KEY_OPTIONS = ['ssh-dss', 'ecdsa-sha2-nistp256', 'ecdsa-sha2-nistp384', 'ecdsa-sha2-nistp521',
                   'ssh-ed25519', 'ssh-rsa', 'ssh-rsa1']

# create comanage_api session
s = Session()
s.auth = (CO_API_USER, CO_API_PASS)

# create mock response session
mock_session = Session()
adapter = requests_mock.Adapter()
mock_session.mount('mock://', adapter)

# add mock adapters
MOCK_501_URL = 'mock://not_implemented_501.local'
adapter.register_uri('GET', MOCK_501_URL, reason='Not Implemented', status_code=501)
