__VERSION__ = "0.1.0"

# expose functions from modules
from .copeople import copeople_add, copeople_delete, copeople_edit, copeople_find, copeople_match, \
    copeople_view_all, copeople_view_per_identifier, copeople_view_one
from .copersonroles import copersonroles_add, copersonroles_delete, copersonroles_edit, copersonroles_view_all, \
    copersonroles_view_per_coperson, copersonroles_view_per_cou, copersonroles_view_one
from .cous import cous_add, cous_delete, cous_edit, cous_view_all, cous_view_one
from .identifiers import identifiers_add, identifiers_assign, identifiers_delete, identifiers_edit, \
    identifiers_view_all, identifiers_view_per_entity, identifiers_view_one
from .names import names_add, names_delete, names_edit, names_view_all, names_view_per_person, names_view_one
