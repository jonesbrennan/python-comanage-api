# python-comanage-api

Provide a limited Python 3 implementation of COmanage REST API v1: [https://spaces.at.internet2.edu/display/COmanage/REST+API+v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1)

### API endpoints

- [COU API](https://spaces.at.internet2.edu/display/COmanage/COU+API)
    - add: `cous_add(name: str, description: str, parent_id=None) -> json`
    - delete: `cous_delete(cou_id: int) -> json`
    - edit: `cous_edit(cou_id: int, name: str, description: str, parent_id=None) -> json`
    - view all (per co): `cous_view_all() -> json`
    - view one: `cous_view_one(cou_id: int) -> json`

- [CoPerson API](https://spaces.at.internet2.edu/display/COmanage/CoPerson+API)
    - add (not implemented)
    - delete (not implemented)
    - edit (not implemented)
    - find:
    - view all (per co):
    - view all (per identifier):
    - view one:

- [CoPersonRole API](https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API)
    - add:
    - delete:
    - edit:
    - view all (per co):
    - view all (per co_person):
    - view all (per cou):
    - view one:

**DISCLAIMER: The code herein may not be up to date nor compliant with the most recent package and/or security notices. The frequency at which this code is reviewed and updated is based solely on the lifecycle of the project for which it was written to support, and is not actively maintained outside of that scope. Use at your own risk.**



## Usage

### From PyPi

TODO

See code in examples directory for usage

### From Source

Install supporting packages

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install -r comanage_api/requirements.txt
```

Create and configure the .env file

```console
cp template.env .env
```

```env
# COmanage API user and pass
COMANAGE_API_USER=co_123.api-user-name
COMANAGE_API_PASS=xxxx-xxxx-xxxx-xxxx
# COmanage CO ID
COMANAGE_CO_ID=123
# COmanage registry URL
COMANAGE_URL=https://FQDN_OF_REGISTRY
```

See code in examples directory for usage

## COUs

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

## References

- COmanage REST API v1: [https://spaces.at.internet2.edu/display/COmanage/REST+API+v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1)
- COU API: [https://spaces.at.internet2.edu/display/COmanage/COU+API](https://spaces.at.internet2.edu/display/COmanage/COU+API)
- CoPerson API: [https://spaces.at.internet2.edu/display/COmanage/CoPerson+API](https://spaces.at.internet2.edu/display/COmanage/CoPerson+API)
- CoPersonRole API: [https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API](https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API)
- PyPi: [https://pypi.org](https://pypi.org)
