# examples/__init__.py
# Configuration for example code

import json
import os
import sys

from dotenv import load_dotenv
from requests.exceptions import HTTPError

# Use .env file to set environment variables
load_dotenv()

COMANAGE_API_USER = os.getenv('COMANAGE_API_USER')
COMANAGE_API_PASS = os.getenv('COMANAGE_API_PASS')
COMANAGE_API_CO_NAME = os.getenv('COMANAGE_API_CO_NAME')
COMANAGE_API_CO_ID = int(os.getenv('COMANAGE_API_CO_ID'))
COMANAGE_API_URL = os.getenv('COMANAGE_API_URL')
COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID = int(os.getenv('COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID'))

# DEVELOPMEMNT: account for comanage_api directory being one level up for development purposes
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# import fabric-comanage-api package (uses directory for development purposes)
from comanage_api import ComanageApi

# create a new ComanageApi object and set the connection attributes
api = ComanageApi(
    co_api_url=COMANAGE_API_URL,
    co_api_user=COMANAGE_API_USER,
    co_api_pass=COMANAGE_API_PASS,
    co_api_org_id=COMANAGE_API_CO_ID,
    co_api_org_name=COMANAGE_API_CO_NAME,
    co_ssh_key_authenticator_id=COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID
)
