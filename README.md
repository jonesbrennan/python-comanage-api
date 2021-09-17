# python-comanage-api

Provide a limited Python 3 implementation of COmanage REST API v1: [https://spaces.at.internet2.edu/display/COmanage/REST+API+v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1)

All responses are in [JSON (ECMA-404)](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/) format

### API endpoints

- [COU API](https://spaces.at.internet2.edu/display/COmanage/COU+API)
    - add: `cous_add(name: str, description: str, parent_id=None) -> json`
    - delete: `cous_delete(cou_id: int) -> json`
    - edit: `cous_edit(cou_id: int, name: str, description: str, parent_id=None) -> json`
    - view all (per co): `cous_view_all() -> json`
    - view one: `cous_view_one(cou_id: int) -> json`

- [CoPerson API](https://spaces.at.internet2.edu/display/COmanage/CoPerson+API)
    - add (not implemented): `copeople_add() -> json`
    - delete (not implemented): `copeople_delete() -> json`
    - edit (not implemented): `copeople_edit() -> json`
    - find (not implemented): `copeople_find() -> json`
    - match: `copeople_match(given=None, family=None, mail=None, distinct_by_id=True) -> json`
    - view all (per co): `copeople_view_all() -> json`
    - view all (per identifier): `copeople_view_per_identifier(identifier: str, distinct_by_id=True) -> json`
    - view one: `copeople_view_one(coperson_id: int) -> json`

- [CoPersonRole API](https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API)
    - add: `copersonroles_add(coperson_id: int, cou_id: int, status=None, affiliation=None) -> json`
    - delete: `copersonroles_delete(copersonrole_id: int) -> json`
    - edit: `copersonroles_edit(copersonrole_id: int, coperson_id: int, cou_id: int, status=None, affiliation=None) -> json`
    - view all (not implemented): `copersonroles_view_all() -> json`
    - view all (per co_person): `copersonroles_view_per_coperson(coperson_id: int) -> json`
    - view all (per cou): `copersonroles_view_per_cou(cou_id: int) -> json`
    - view one: `copersonroles_view_one(copersonrole_id: int) -> json`
    
    **NOTE**: when provided, valid values for `status` and `affiliation` as follows:

    ```python
    STATUS_OPTIONS = ['Active', 'Approved', 'Confirmed', 'Declined', 'Deleted', 'Denied', 'Duplicate', 
    'Expired', 'GracePeriod', 'Invited', 'Pending', 'PendingApproval', 'PendingConfirmation', 'Suspended']
    AFFILIATION_OPTIONS = ['affiliate', 'alum', 'employee', 'faculty', 'member', 'staff', 'student']
    ```

- [Identifier API](https://spaces.at.internet2.edu/display/COmanage/Identifier+API)
    - add:
    - assign:
    - delete:
    - edit:
    - view all:
    - view per entity:
    - view one:

- [Name API](https://spaces.at.internet2.edu/display/COmanage/Name+API)
    - add:
    - delete:
    - edit:
    - view all:
    - view per person:
    - view one:

- [SshKey API](https://spaces.at.internet2.edu/display/COmanage/SshKey+API)
    - add:
    - delete:
    - edit:
    - view all:
    - view all (per co_person):
    - view one:

    
**DISCLAIMER: The code herein may not be up to date nor compliant with the most recent package and/or security notices. The frequency at which this code is reviewed and updated is based solely on the lifecycle of the project for which it was written to support, and is not actively maintained outside of that scope. Use at your own risk.**



## Usage

### From PyPi

TODO

See code in [examples](examples/) directory for usage

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
# COmanage CO Information
COMANAGE_CO_NAME=RegistryName
COMANAGE_CO_ID=123
# COmanage registry URL
COMANAGE_URL=https://FQDN_OF_REGISTRY
```

See code in [examples](examples/) directory for usage

## References

- COmanage REST API v1: [https://spaces.at.internet2.edu/display/COmanage/REST+API+v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1)
- COU API: [https://spaces.at.internet2.edu/display/COmanage/COU+API](https://spaces.at.internet2.edu/display/COmanage/COU+API)
- CoPerson API: [https://spaces.at.internet2.edu/display/COmanage/CoPerson+API](https://spaces.at.internet2.edu/display/COmanage/CoPerson+API)
- CoPersonRole API: [https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API](https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API)
- Identifier API: [https://spaces.at.internet2.edu/display/COmanage/Identifier+API](https://spaces.at.internet2.edu/display/COmanage/Identifier+API)
- Name API: [https://spaces.at.internet2.edu/display/COmanage/Name+API](https://spaces.at.internet2.edu/display/COmanage/Name+API)
- SsHKey API: [https://spaces.at.internet2.edu/display/COmanage/SshKey+API](https://spaces.at.internet2.edu/display/COmanage/SshKey+API)
- PyPi: [https://pypi.org](https://pypi.org)
