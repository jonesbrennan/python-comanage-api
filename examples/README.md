# Examples

Examples demonstrating basic usage for each wrapped endpoint. Some of the values used herein are specific to the ImPACT project registry and thus would not work for other registries, but the concept would be the same for any registry.

## COU API

Example: `cous_example.py` 

```console
$ python examples/cous_example.py
### cous_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "Cou",
    "Id": "105"
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
            "Lft": "66",
            "Rght": "67",
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
            "Lft": "68",
            "Rght": "69",
            "Created": "2021-09-10 14:44:09",
            "Modified": "2021-09-10 14:44:09",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "105",
            "CoId": "3",
            "Name": "cou test",
            "Description": "cou test description",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:33",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### cous_edit
True
### cous_view_one
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "105",
            "CoId": "3",
            "Name": "cou test - edited",
            "Description": "cou test description - edited",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:34",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### cous_delete
True
### cous_view_one (previously deleted cou)
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "105",
            "CoId": "3",
            "Name": "cou test - edited",
            "Description": "cou test description - edited",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:34",
            "Revision": "1",
            "Deleted": true,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
```

## CoPerson API

Example: `copeople_example.py`

```console
$ python examples/copeople_example.py
### copeople_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_find
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
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
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/co_people.json
### copeople_view_per_co
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
    "Id": "1727"
}
### copersonroles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "student",
            "O": "Impact",
            "Status": "PendingApproval",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:44",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_edit
True
### copersonroles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/co_person_roles.json
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
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
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
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### copersonroles_delete
True
### copersonroles_view_one (previously deleted co person role)
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:46",
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
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_assign
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/identifiers.json
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
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/names.json
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

**NOTE**: waiting to resolve whether `add` and `edit` functions should be available to priviledged API users (currenlty they are not)

Example: `ssh_keys_example.py `

```console
$ python examples/ssh_keys_example.py
### ssh_keys_add
[ERROR] Exception caught
-->  HTTPError - 500 Server Error: Internal Server Error for url: https://registry.cilogon.org/registry/ssh_key_authenticator/ssh_keys/add
### ssh_keys_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/ssh_key_authenticator/ssh_keys.json
### ssh_keys_view_per_coperson
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "39",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Comment": "michael.j.stealey@gmail.com",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-09-27 01:11:57",
            "Modified": "2021-09-27 01:11:57",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181",
            "SshKeyAuthenticatorId": "3"
        }
    ]
}
### ssh_keys_view_one
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "39",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Comment": "michael.j.stealey@gmail.com",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-09-27 01:11:57",
            "Modified": "2021-09-27 01:11:57",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181",
            "SshKeyAuthenticatorId": "3"
        }
    ]
}
### ssh_keys_edit
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/ssh_key_authenticator/ssh_keys/39.json
### ssh_keys_view_one
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "39",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Comment": "michael.j.stealey@gmail.com",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-09-27 01:11:57",
            "Modified": "2021-09-27 01:11:57",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181",
            "SshKeyAuthenticatorId": "3"
        }
    ]
}
### ssh_keys_delete
True
### ssh_keys_view_one (previously deleted ssh key)
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "38",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Comment": "michael.j.stealey@gmail.com",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-09-25 16:41:57",
            "Modified": "2021-09-26 20:42:17",
            "Revision": "0",
            "Deleted": true,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181",
            "SshKeyAuthenticatorId": "3"
        }
    ]
}
```
