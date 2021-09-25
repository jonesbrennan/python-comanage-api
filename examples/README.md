# Examples

Examples demonstrating basic usage for each wrapped endpoint. Some of the values used herein are specific to the ImPACT CO and thus would not work for other registries, but the concept would be the same for any registry.

## COU API

Example: `cous_example.py` 

```console
$ python examples/cous_example.py
### cous_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "Cou",
    "Id": "53"
}
### cous_view_all
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "38",
            "CoId": "3",
            "Name": "enrollment-approval",
            "Description": "Enrollment Approval Personnel - can approve or deny new registry members",
            "Lft": "60",
            "Rght": "61",
            "Created": "2021-09-10 14:33:11",
            "Modified": "2021-09-10 14:33:11",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "39",
            "CoId": "3",
            "Name": "impact-users",
            "Description": "ImPACT Users - Registering with the ImPACT site will add new user's to this group",
            "Lft": "62",
            "Rght": "63",
            "Created": "2021-09-10 14:44:09",
            "Modified": "2021-09-10 14:44:09",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "53",
            "CoId": "3",
            "Name": "cou test",
            "Description": "cou test description",
            "Lft": "70",
            "Rght": "71",
            "Created": "2021-09-14 20:31:21",
            "Modified": "2021-09-14 20:31:21",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### cous_edit
{
    "status_code": 200,
    "reason": "OK"
}
### cous_view_one
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "53",
            "CoId": "3",
            "Name": "cou test - edit",
            "Description": "cou test description - edit",
            "Lft": "70",
            "Rght": "71",
            "Created": "2021-09-14 20:31:21",
            "Modified": "2021-09-14 20:31:21",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### cous_delete
{
    "status_code": 200,
    "reason": "OK"
}
```

## CoPerson API

Example: `copeople_example.py`

```console
$ python examples/copeople_example.py
### copeople_add
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### copeople_delete
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### copeople_edit
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### copeople_find
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### copeople_match
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### copeople_view_all
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "29",
            "CoId": "3",
            "Status": "Active",
            "Created": "2018-11-05 20:48:55",
            "Modified": "2018-11-06 03:23:00",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/241998"
        },
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "1558",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-10 18:32:32",
            "Modified": "2021-09-10 18:33:46",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/227641"
        },
        {
            "Version": "1.0",
            "Id": "1573",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-14 11:06:03",
            "Modified": "2021-09-14 11:06:57",
            "Revision": "7",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/2604273"
        },
        {
            "Version": "1.0",
            "Id": "1603",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:36:02",
            "Revision": "7",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
### copeople_view_per_identifier
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### copeople_view_one
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "29",
            "CoId": "3",
            "Status": "Active",
            "Created": "2018-11-05 20:48:55",
            "Modified": "2018-11-06 03:23:00",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/241998"
        }
    ]
}
```

## CoPersonRole API

Example: `copersonroles_example.py`

```console
$ python examples/copersonroles_example.py
### copersonroles_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "CoPersonRole",
    "Id": "1677"
}
### copersonroles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1677",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "student",
            "O": "Impact",
            "Status": "PendingApproval",
            "Created": "2021-09-17 18:11:49",
            "Modified": "2021-09-17 18:11:49",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_edit
Active member
{
    "status_code": 200,
    "reason": "OK"
}
### copersonroles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1677",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-17 18:11:49",
            "Modified": "2021-09-17 18:11:50",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_view_all
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### copersonroles_view_per_coperson
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1648",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:36:02",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1677",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-17 18:11:49",
            "Modified": "2021-09-17 18:11:50",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_view_per_cou
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1622",
            "Person": {
                "Type": "CO",
                "Id": "1558"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-10 18:32:32",
            "Modified": "2021-09-10 18:33:46",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/227641"
        },
        {
            "Version": "1.0",
            "Id": "1628",
            "Person": {
                "Type": "CO",
                "Id": "1573"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-14 11:06:09",
            "Modified": "2021-09-14 11:06:57",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/2604273"
        },
        {
            "Version": "1.0",
            "Id": "1677",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-17 18:11:49",
            "Modified": "2021-09-17 18:11:50",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_delete
{
    "status_code": 200,
    "reason": "OK"
}
### copersonroles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1677",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-17 18:11:49",
            "Modified": "2021-09-17 18:11:51",
            "Revision": "1",
            "Deleted": true,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
```

## Identifiers API

Example: `identifiers_example.py`

```console
$ python examples/identifiers_example.py
### identifiers_add
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### identifiers_assign
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### identifiers_delete
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### identifiers_edit
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### identifiers_view_all
{
    "status_code": 401,
    "reason": "Unauthorized"
}
### identifiers_view_per_entity
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "1552",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1550",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1553",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "sorid",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1551",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1554",
            "Identifier": "ImPACT1000006",
            "Type": "impactid",
            "Login": false,
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Created": "2021-09-15 12:36:01",
            "Modified": "2021-09-15 12:36:01",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### identifiers_view_one
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "1552",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1550",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
```

## Names API

Example: `names_example.py`

```console
$ python examples/names_example.py
### names_add
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### names_delete
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### names_edit
{
    "status_code": 501,
    "reason": "Not Implemented"
}
### names_view_all
{
    "status_code": 401,
    "reason": "Unauthorized"
}
### names_view_per_person
{
    "ResponseType": "Names",
    "Version": "1.0",
    "Names": [
        {
            "Version": "1.0",
            "Id": "923",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": false,
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "924",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceNameId": "922",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "926",
            "Honorific": "",
            "Given": "mj",
            "Middle": "",
            "Family": "stealey",
            "Suffix": "",
            "Type": "official",
            "Language": "",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": true,
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
### names_view_one
{
    "ResponseType": "Names",
    "Version": "1.0",
    "Names": [
        {
            "Version": "1.0",
            "Id": "923",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": false,
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
```

## SshKey API


