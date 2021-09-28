import json

from .config import *

"""
SshKey API - https://spaces.at.internet2.edu/display/COmanage/SshKey+API

Experimental
- The SshKey API is implemented via the SSH Key Authenticator Plugin. 
  REST APIs provided by plugins are currently considered Experimental, and as such this interface may change 
  without notice between minor releases.

Implementation Notes
- Only JSON format is supported. XML format is not supported.
- Note the URLs for this API use plugin syntax. (There is an extra component to the path.)
- As defined in the SshKey Schema, an SSH Key Authenticator ID is required as part of the request. 
  This refers to the Authenticator instantiated for the CO.
- Authenticators that are locked cannot be managed by the API.
"""


def ssh_keys_add(coperson_id: int, ssh_key: str, key_type: str, comment: str, ssh_key_authenticator_id=None) -> json:
    """
    Add a new SSH Key.

    :post_body
    :return
        {
            "ResponseType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    ,
                    "Comment":"<Comment>",
                    "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                            "ssh-ed25519'"|"ssh-rsa"|"ssh-rsa1"),
                    "Skey":"<SshKey>",
                    "SshKeyAuthenticatorId":"<Id>"
                },
                {...}
            ]
        }:

    Request Format
        {
            "RequestType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                    "Version":"1.0",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    "Comment":"<Comment>",
                    "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                            "ssh-ed25519'"|"ssh-rsa"|"ssh-rsa1"),
                    "Skey":"<SshKey>",
                    "SshKeyAuthenticatorId":"<Id>"
                }
            ]
        }:

    Response Format
        HTTP Status             Response Body                       Description
        201 Added               NewObjectResponse with              SSH Key created
                                ObjectType of SshKey
        400 Bad Request                                             SSH Key Request not provided in POST body
        400 Invalid Fields      ErrorResponse with details in       An error in one or more provided fields
                                InvalidFields element
        401 Unauthorized                                            Authentication required
        500 Other Error                                             Unknown error
    """
    if not ssh_key_authenticator_id:
        ssh_key_authenticator_id = CO_SSH_KEY_AUTHENTICATOR_ID
    if not key_type:
        key_type = 'ssh-rsa'
    else:
        key_type = str(key_type).lower()
    if key_type not in SSH_KEY_OPTIONS:
        return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: key_type'})
    post_body = json.dumps({
        'RequestType': 'SshKeys',
        'Version': '1.0',
        'SshKeys':
            [
                {
                    'Version': '1.0',
                    'Person':
                        {
                            'Type': 'CO',
                            'Id': str(coperson_id)
                        },
                    'Comment': str(comment),
                    'Type': str(key_type),
                    'Skey': str(ssh_key),
                    'SshKeyAuthenticatorId': str(ssh_key_authenticator_id)
                }
            ]
    })
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys.json'
    resp = s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def ssh_keys_delete(ssh_key_id: int) -> json:
    """
    Remove an SSH Key.

    :param ssh_key_id:
    :return::

    Response Format
        HTTP Status             Response Body       Description
        200 OK                                      SSH Key updated
        400 Invalid Fields                          An error in one or more provided fields
        401 Unauthorized                            Authentication required
        404 SshKey Unknown                          id not found
        500 Other Error                             Unknown error
    """
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys/' + str(ssh_key_id) + '.json'
    resp = s.delete(
        url=url
    )
    return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def ssh_keys_edit(ssh_key_id: int, coperson_id: int, ssh_key=None, key_type=None, comment=None,
                  ssh_key_authenticator_id=None) -> json:
    """
    Edit an exiting SSH Key.

    :post_body
    :return:

    Request Format
        {
            "RequestType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                    "Version":"1.0",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    "Comment":"<Comment>",
                    "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                            "ssh-ed25519'"|"ssh-rsa"|"ssh-rsa1"),
                    "Skey":"<SshKey>",
                    "SshKeyAuthenticatorId":"<Id>"
                }
            ]
        }:

    Response Format
        HTTP Status             Response Body                       Description
        200 OK                                                      SSH Key updated
        400 Bad Request                                             SSH Key Request not provided in POST body
        400 Invalid Fields      ErrorResponse with details in       An error in one or more provided fields
                                InvalidFields element
        401 Unauthorized                                            Authentication required
        404 SshKey Unknown                                          id not found
        500 Other Error                                             Unknown error
    """
    orig_key = json.loads(ssh_keys_view_one(ssh_key_id=ssh_key_id))
    if not ssh_key_authenticator_id:
        ssh_key_authenticator_id = CO_SSH_KEY_AUTHENTICATOR_ID
    post_body = {
        'RequestType': 'SshKeys',
        'Version': '1.0',
        'SshKeys':
            [
                {
                    'Version': '1.0',
                    'Person':
                        {
                            'Type': 'CO',
                            'Id': str(coperson_id)
                        },
                    'SshKeyAuthenticatorId': str(ssh_key_authenticator_id)
                }
            ]
    }
    if comment:
        post_body['SshKeys'][0]['Comment'] = str(comment)
    else:
        post_body['SshKeys'][0]['Comment'] = orig_key['SshKeys'][0]['Comment']
    if key_type:
        post_body['SshKeys'][0]['Type'] = str(key_type).lower()
        if key_type not in SSH_KEY_OPTIONS:
            return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: key_type'})
    else:
        post_body['SshKeys'][0]['Type'] = orig_key['SshKeys'][0]['Type']
    if ssh_key:
        post_body['SshKeys'][0]['Skey'] = str(ssh_key)
    else:
        post_body['SshKeys'][0]['Skey'] = orig_key['SshKeys'][0]['Skey']
    post_body = json.dumps(post_body)
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys/' + str(ssh_key_id) + '.json'
    resp = s.put(
        url=url,
        data=post_body
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def ssh_keys_view_all() -> json:
    """
    Retrieve all existing SSH Keys.

    :return
        {
            "ResponseType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                "Version":"1.0",
                "Id":"<Id>",
                "Person":
                {
                    "Type":"CO",
                    "Id":"<ID>"
                },
                ,
                "Comment":"<Comment>",
                "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                        "ssh-ed25519"|"ssh-rsa"|"ssh-rsa1"),
                "Skey":"<SshKey>",
                "SshKeyAuthenticatorId":"<Id>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body       Description
        200 OK              SshKey Response     SSH Keys returned
        401 Unauthorized                        Authentication required
        500 Other Error                         Unknown error
    """
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys.json'
    resp = s.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def ssh_keys_view_per_coperson(coperson_id: int) -> json:
    """
    Retrieve all existing SSH Keys for the specified CO Person.

    :return
        {
            "ResponseType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                "Version":"1.0",
                "Id":"<Id>",
                "Person":
                {
                    "Type":"CO",
                    "Id":"<ID>"
                },
                ,
                "Comment":"<Comment>",
                "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                        "ssh-ed25519"|"ssh-rsa"|"ssh-rsa1"),
                "Skey":"<SshKey>",
                "SshKeyAuthenticatorId":"<Id>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status             Response Body       Description
        200 OK                  SshKey Response     SSH Keys returned
        401 Unauthorized                            Authentication required
        404 SSH Key Unknown                         id not found
        500 Other Error                             Unknown error
    """
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys.json'
    params = {'copersonid': str(coperson_id)}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def ssh_keys_view_one(ssh_key_id: int) -> json:
    """
    Retrieve an existing SSH Key.

    :return
        {
            "ResponseType":"SshKeys",
            "Version":"1.0",
            "SshKeys":
            [
                {
                "Version":"1.0",
                "Id":"<Id>",
                "Person":
                {
                    "Type":"CO",
                    "Id":"<ID>"
                },
                ,
                "Comment":"<Comment>",
                "Type":("ssh-dss"|"ecdsa-sha2-nistp256"|"ecdsa-sha2-nistp384"|"ecdsa-sha2-nistp521"|
                        "ssh-ed25519"|"ssh-rsa"|"ssh-rsa1"),
                "Skey":"<SshKey>",
                "SshKeyAuthenticatorId":"<Id>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status             Response Body       Description
        200 OK                  SshKey Response     SSH Keys returned
        401 Unauthorized                            Authentication required
        404 SSH Key Unknown                         id not found
        500 Other Error                             Unknown error
    """
    url = CO_API_URL + '/ssh_key_authenticator/ssh_keys/' + str(ssh_key_id) + '.json'
    resp = s.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})
