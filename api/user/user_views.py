from flask import (
    Blueprint
)

from api.user.user_service import (
    get_public_user_details
)
from api.security.guards import authorization_guard

bp_name = 'api-users'
bp_url_prefix = '/api/users'
bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix)


@bp.route("/public")
def public():
    return vars(get_public_user_details())


@bp.route("/protected")
@authorization_guard
def protected():
    return vars(get_protected_user_details())


@bp.route("/admin")
@authorization_guard
def admin():
    return vars(get_admin_user_details())
