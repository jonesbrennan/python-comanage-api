import json

from .config import *

"""
Name API - https://spaces.at.internet2.edu/display/COmanage/Name+API
"""


def names_add() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})


def names_delete() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})


def names_edit() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})


def names_view_all() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})


def names_view_per_coperson() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})


def names_one() -> json:
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})
