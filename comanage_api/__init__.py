__VERSION__ = "0.1.0"

# expose functions from copeople module
from .copeople import copeople_add, copeople_delete, copeople_edit, copeople_find, copeople_match, \
    copeople_view_all, copeople_view_per_identifier, copeople_view_one
# expose functions from cous module
from .cous import cous_add, cous_delete, cous_edit, cous_view_all, cous_view_one
