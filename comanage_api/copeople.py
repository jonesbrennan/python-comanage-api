import json

from .config import *

"""
CoPerson API - https://spaces.at.internet2.edu/display/COmanage/CoPerson+API
"""


def copeople_add() -> json:
    """
    ### NOT IMPLEMENTED ###
    Add a new CO Person. A person must have an OrgIdentity before they can be added to a CO.
    Note that linking to an OrgIdentity and invitations are separate operations.

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


def copeople_delete() -> json:
    """
    ### NOT IMPLEMENTED ###
    Remove a CO Person. This method will also delete related data, such as CoPersonRoles, EmailAddresses,
    and Identifiers. A person must be removed from any COs (CoPerson records must be deleted)
    before the OrgIdentity record can be removed.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def copeople_edit() -> json:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CO Person.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def copeople_find() -> json:
    """
    ### NOT IMPLEMENTED ###
    Search for existing CO Person records.
    When too many records are found, a message may be returned rather than specific records.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = MOCK_501_URL
    resp = mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def copeople_match(given=None, family=None, mail=None, distinct_by_id=True) -> json:
    """
    Attempt to match existing CO Person records.
    Note that matching is not performed on search criteria of less than 3 characters,
    or for email addresses that are not syntactically valid.

    :param given:
    :param family:
    :param mail:
    :param distinct_by_id:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoPerson Response       CoPerson returned (zero or more matches may be returned)
        401 Unauthorized                                Authentication required
        404 CO Unknown                                  id not found - Not currently implemented
                                                            -- unknown CO will return an empty set
        500 Other Error                                 Unknown error
    """
    url = CO_API_URL + '/co_people.json'
    params = {'coid': CO_API_ORG_ID}
    if given:
        params.update({'given': given})
    if family:
        params.update({'family': family})
    if mail:
        params.update({'mail': mail})
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        if distinct_by_id:
            resp_dict = json.loads(resp.text)
            distinct_copeople = list({v['Id']: v for v in resp_dict.get('CoPeople')}.values())
            resp_dict['CoPeople'] = distinct_copeople
            return json.dumps(resp_dict)
        else:
            return resp.text
    else:
        resp.raise_for_status()


def copeople_view_all() -> json:
    """
    Retrieve all existing CO People for the specified CO.

    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoPerson Response       CoPerson returned (zero or more matches may be returned)
        401 Unauthorized                                Authentication required
        404 CO Unknown                                  id not found - Not currently implemented
                                                            -- unknown CO will return an empty set
        500 Other Error                                 Unknown error
    """
    url = CO_API_URL + '/co_people.json'
    params = {'coid': CO_API_ORG_ID}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()


def copeople_view_per_identifier(identifier: str, distinct_by_id=True) -> json:
    """
    Retrieve all existing CO People attached to the specified identifier.
    Note the specified identifier must be attached to a CO Person, not an Org Identity.

    :param identifier:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      CoPerson Response       CoPerson returned
        401 Unauthorized                                    Authentication required
        404 CO Unknown                                      id not found
        500 Other Error                                     Unknown error
    """
    url = CO_API_URL + '/co_people.json'
    params = {'coid': CO_API_ORG_ID, 'search.identifier': identifier}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        if distinct_by_id:
            resp_dict = json.loads(resp.text)
            distinct_copeople = list({v['Id']: v for v in resp_dict.get('CoPeople')}.values())
            resp_dict['CoPeople'] = distinct_copeople
            return json.dumps(resp_dict)
        else:
            return resp.text
    else:
        resp.raise_for_status()


def copeople_view_one(coperson_id: int) -> json:
    """
    Retrieve an existing CO Person.

    :param coperson_id:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      CoPerson Response       CoPerson returned
        401 Unauthorized                                    Authentication required
        404 copeople Unknown                                id not found
        500 Other Error                                     Unknown error
    """
    url = CO_API_URL + '/co_people/' + str(coperson_id) + '.json'
    params = {'coid': CO_API_ORG_ID}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        resp.raise_for_status()
