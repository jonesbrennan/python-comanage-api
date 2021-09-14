import os

from dotenv import load_dotenv
from requests import Session

load_dotenv()

CO_API_USER = os.getenv('COMANAGE_API_USER')
CO_API_PASS = os.getenv('COMANAGE_API_PASS')
CO_API_ID = os.getenv('COMANAGE_CO_ID')
CO_API_URL = os.getenv('COMANAGE_URL')
if CO_API_URL.endswith('/'):
    CO_API_URL = CO_API_URL[:-1]

s = Session()
s.auth = (CO_API_USER, CO_API_PASS)
