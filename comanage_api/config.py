import os

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

s = Session()
s.auth = (CO_API_USER, CO_API_PASS)
