import json

from .config import *

"""
CoPersonRole API - https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API
"""


def copersonroles_add(coperson_id: int, cou_id: int, status=None, affiliation=None) -> json:
    """
    Add a new CO Person Role.

    :param affiliation:
    :param coperson_id:
    :param cou_id:
    :param status:

    :return
        {
            "ResponseType":"NewObject",
            "Version":"1.0",
            "ObjectType":"CoPersonRole",
            "Id":"<ID>"
        }:

    Request Format
        {
          "RequestType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Person":
              {
                "Type":"CO",
                "Id":"<coperson_id>"
              },
              "CouId":"<cou_id>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            }
          ]
        }

    Response Format
        HTTP Status             Response Body                       Description
        201 Added               NewObjectResponse with ObjectType   CoPersonRole created
        400 Bad Request                                             CoPersonRole Request not provided in POST body
        400 Invalid Fields      ErrorResponse with details in       An error in one or more provided fields
                                InvalidFields element
        401 Unauthorized                                            Authentication required
        403 COU Does Not Exist                                      The specified COU does not exist
        500 Other Error                                             Unknown error
    """
    if not status:
        status = 'Active'
    if not affiliation:
        affiliation = 'member'
    else:
        affiliation = str(affiliation).lower()
    if status not in STATUS_OPTIONS:
        return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: Status'})
    if affiliation not in AFFILIATION_OPTIONS:
        return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: Affiliation'})
    post_body = json.dumps({
        'RequestType': 'CoPersonRoles',
        'Version': '1.0',
        'CoPersonRoles': [
            {
                'Version': '1.0',
                'Person':
                    {
                        'Type': 'CO',
                        'Id': str(coperson_id)
                    },
                'CouId': str(cou_id),
                'Affiliation': str(affiliation),
                'O': str(CO_API_ORG_NAME),
                'Status': str(status)
            }
        ]
    })
    url = CO_API_URL + '/co_person_roles.json'
    resp = s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})
    pass


def copersonroles_delete(copersonrole_id: int) -> json:
    """
    Remove a CO Person Role.

    :param copersonrole_id:
    :return:

    Response Format
        HTTP Status                 Response Body       Description
        200 Deleted                                     CoPersonRole deleted
        400 Invalid Fields                              id not provided
        401 Unauthorized                                Authentication required
        404 CoPersonRole Unknown                        id not found
        500 Other Error                                 Unknown error
    """
    url = CO_API_URL + '/co_person_roles/' + str(copersonrole_id) + '.json'
    resp = s.delete(
        url=url
    )
    return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def copersonroles_edit(copersonrole_id: int, coperson_id: int, cou_id: int, status=None, affiliation=None) -> json:
    """
    Edit an existing CO Person Role.

    :param copersonrole_id:
    :param affiliation:
    :param coperson_id:
    :param cou_id:
    :param status:

    :return:

    Request Format
        {
          "RequestType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Person":
              {
                "Type":"CO",
                "Id":"<coperson_id>"
              },
              "CouId":"<cou_id>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            }
          ]
        }

    Response Format
        HTTP Status                 Response Body                       Description
        200 OK                                                          CoPersonRole updated
        400 Bad Request                                                 CoPersonRole Request not provided in POST body
        400 Invalid Fields          ErrorRespons with details in        An error in one or more provided fields
                                    InvalidFields element
        401 Unauthorized                                                Authentication required
        403 COU Does Not Exist                                          The specified COU does not exist
        404 CoPersonRole Unknown                                        id not found
        500 Other Error                                                 Unknown error
    """
    copersonrole = json.loads(copersonroles_view_one(copersonrole_id))
    print(status, affiliation)
    if copersonrole.get('CoPersonRoles'):
        if not status:
            status = copersonrole['CoPersonRoles'][0]['Status']
        if not affiliation:
            affiliation = copersonrole['CoPersonRoles'][0]['Affiliation']
    else:
        return json.dumps({'status_code': 500, 'reason': 'Unknown error'})
    if status not in STATUS_OPTIONS:
        return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: Status'})
    if affiliation not in AFFILIATION_OPTIONS:
        return json.dumps({'status_code': 400, 'reason': 'Invalid Fields: Affiliation'})

    post_body = json.dumps({
        'RequestType': 'CoPersonRoles',
        'Version': '1.0',
        'CoPersonRoles': [
            {
                'Version': '1.0',
                'Person':
                    {
                        'Type': 'CO',
                        'Id': str(coperson_id)
                    },
                'CouId': str(cou_id),
                'Affiliation': str(affiliation),
                'O': str(CO_API_ORG_NAME),
                'Status': str(status)
            }
        ]
    })
    url = CO_API_URL + '/co_person_roles/' + str(copersonrole_id) + '.json'
    resp = s.put(
        url=url,
        data=post_body
    )
    return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def copersonroles_view_all() -> json:
    """
    Retrieve all existing CO Person Roles.

    :return
        {
          "ResponseType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Id":"<Id>",
              "Person":
              {
                "Type":"CO",
                "Id":"<ID>"
              },
              "CouId":"<CouId>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status             Response Body                       Description
        200 OK                  CoPersonRole Response               CoPersonRoles returned
        401 Unauthorized                                            Authentication required
        500 Other Error                                             Unknown error
    """
    return json.dumps({'status_code': 501, 'reason': 'Not Implemented'})
    # TODO: Does not allow retrieval of all CoPersonRoles per CO even when CoId is defined
    # url = CO_API_URL + '/co_person_roles.json'
    # params = {'coid': CO_API_ORG_ID}
    # resp = s.get(
    #     url=url,
    #     params=params
    # )
    # if resp.status_code == 200:
    #     return resp.text
    # else:
    #     return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def copersonroles_view_per_coperson(coperson_id: int) -> json:
    """
    Retrieve all existing CO Person Roles for the specified CO Person. Available since Registry v2.0.0.

    :param coperson_id:
    :return
        {
          "ResponseType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Id":"<Id>",
              "Person":
              {
                "Type":"CO",
                "Id":"<ID>"
              },
              "CouId":"<CouId>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status             Response Body                       Description
        200 OK                  CoPersonRole Response               CoPersonRoles returned
        401 Unauthorized                                            Authentication required
        404 CO Person Unknown                                       id not found
        500 Other Error                                             Unknown error
    """
    url = CO_API_URL + '/co_person_roles.json'
    params = {'copersonid': int(coperson_id)}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def copersonroles_view_per_cou(cou_id: int) -> json:
    """
    Retrieve all existing CO Person Roles for the specified COU.

    :param cou_id:
    :return
        {
          "ResponseType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Id":"<Id>",
              "Person":
              {
                "Type":"CO",
                "Id":"<ID>"
              },
              "CouId":"<CouId>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status             Response Body                       Description
        200 OK                  CoPersonRole Response               CoPersonRoles returned
        401 Unauthorized                                            Authentication required
        404 COU Unknown                                             id not found
        500 Other Error                                             Unknown error
    """
    url = CO_API_URL + '/co_person_roles.json'
    params = {'couid': int(cou_id)}
    resp = s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})


def copersonroles_view_one(copersonrole_id: int) -> json:
    """
    Retrieve an existing CO Person Role.

    :param copersonrole_id:
    :return
        {
          "ResponseType":"CoPersonRoles",
          "Version":"1.0",
          "CoPersonRoles":
          [
            {
              "Version":"1.0",
              "Id":"<Id>",
              "Person":
              {
                "Type":"CO",
                "Id":"<ID>"
              },
              "CouId":"<CouId>",
              "Affiliation":"<Affiliation>",
              "Title":"<Title>",
              "O":"<O>",
              "Ordr":"<Order>",
              "Ou":"<Ou>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended"),
              "ValidFrom":"<ValidFrom>",
              "ValidThrough":"<ValidThrough>",
              "Created":"<CreateTime>",
              "Modified":"<ModTime>",
              "ExtendedAttributes":
              {
                "<Attribute>":"<Value>",
                {...}
              }
            },
            {...}
          ]
        }:

    Response Format
        HTTP Status                 Response Body                       Description
        200 OK                      CoPersonRole Response               CoPersonRoles returned
        401 Unauthorized                                                Authentication required
        404 CoPersonRole Unknown                                        id not found
        500 Other Error                                                 Unknown error
    """
    url = CO_API_URL + '/co_person_roles/' + str(copersonrole_id) + '.json'
    resp = s.get(
        url=url
    )
    if resp.status_code == 200:
        return resp.text
    else:
        return json.dumps({'status_code': resp.status_code, 'reason': resp.reason})
