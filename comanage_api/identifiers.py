import json

from .config import *

"""
Identifier API - https://spaces.at.internet2.edu/display/COmanage/Identifier+API
"""


def identifiers_add() -> json:
    """
    ### NOT IMPLEMENTED ###
    Add a new Identifier.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 201:
        return resp.text
    else:
        resp.raise_for_status()


def identifiers_assign() -> bool:
    """
    ### NOT IMPLEMENTED ###
    Assign Identifiers for a CO Person.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def identifiers_delete() -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove an Identifier.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def identifiers_edit() -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing Identifier.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def identifiers_view_all() -> json:
    """
    Retrieve all existing Identifiers.

    :return
        {
          "ResponseType":"Identifiers",
          "Version":"1.0",
          "Identifiers":
          [
            {
              "Version":"1.0",
              "Id":"<ID>",
              "Type":"<Type>",
              "Identifier":"<Identifier>",
              "Login":true|false,
              "Person":{"Type":("CO"|"Dept"|"Group"|"Org"|"Organization"),"ID":"<ID>"},
              "CoProvisioningTargetId":"<CoProvisioningTargetId>",
              "Status":"Active"|"Deleted",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>"
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status         Response Body           Description
        200 OK              Identifier Response     Identifiers returned
        401 Unauthorized                            Authentication required
        500 Other Error                             Unknown error
    """
    url = CO_API_URL + '/identifiers.json'
    resp = s.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def identifiers_view_per_entity(entity_type: str, entity_id: int) -> json:
    """
    Retrieve Identifiers attached to a CO Department, Co Group, CO Person, or Org Identity.

    :param entity_type:
    :param entity_id:
    :return
        {
          "ResponseType":"Identifiers",
          "Version":"1.0",
          "Identifiers":
          [
            {
              "Version":"1.0",
              "Id":"<ID>",
              "Type":"<Type>",
              "Identifier":"<Identifier>",
              "Login":true|false,
              "Person":{"Type":("CO"|"Dept"|"Group"|"Org"|"Organization"),"ID":"<ID>"},
              "CoProvisioningTargetId":"<CoProvisioningTargetId>",
              "Status":"Active"|"Deleted",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>"
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      Identifier Response     Identifier returned
        204 CO Department                                   The requested CO Department was found,
            Has No Identifier                                   but has no identifiers attached
        204 CO Group                                        The requested CO Group was found,
            Has No Identifier                                   but has no identifiers attached
        204 CO Person                                       The requested CO Person was found,
            Has No Identifier                                   but has no identifiers attached
        204 Organization                                    The requested Organization was found,
            Has No Identifier                                   but has no identifiers attached
        204 Org Identity                                    The requested Org Identity was found,
            Has No Identifier                                   but has no identifiers attached
        401 Unauthorized                                    Authentication required
        404 CO Department Unknown                           id not found for CO Department
        404 CO Group Unknown                                id not found for CO Group
        404 CO Person Unknown                               id not found for CO Person
        404 Organization Unknown                            id not found for Organization
        404 Org Identity Unknown                            id not found for Org Identity
        500 Other Error                                     Unknown error
    """
    if not entity_type:
        entity_type = 'copersonid'
    else:
        entity_type = str(entity_type).lower()
    if entity_type not in ENTITY_OPTIONS:
        raise TypeError("Invalid Fields 'entity_type'")
    url = CO_API_URL + '/identifiers.json'
    params = {str(entity_type): str(entity_id)}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def identifiers_view_one(identifier_id: int) -> json:
    """
    Retrieve all existing Identifiers.

    :param identifier_id:
    :return
        {
          "ResponseType":"Identifiers",
          "Version":"1.0",
          "Identifiers":
          [
            {
              "Version":"1.0",
              "Id":"<ID>",
              "Type":"<Type>",
              "Identifier":"<Identifier>",
              "Login":true|false,
              "Person":{"Type":("CO"|"Dept"|"Group"|"Org"|"Organization"),"ID":"<ID>"},
              "CoProvisioningTargetId":"<CoProvisioningTargetId>",
              "Status":"Active"|"Deleted",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>"
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      Identifier Response     Identifiers returned
        401 Unauthorized                                    Authentication required
        404 Identifier Unknown                              id not found
        500 Other Error                                     Unknown error
    """
    url = CO_API_URL + '/identifiers/' + str(identifier_id) + '.json'
    resp = s.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()
