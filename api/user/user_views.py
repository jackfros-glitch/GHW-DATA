from flask import (
    Blueprint,
    request,
    jsonify,
    abort
)

from api.user.user_service import (
    get_public_user_details,
    get_protected_user_details,
    get_admin_user_details
)
from api.security.guards import authorization_guard
from api.models.models import User

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


@bp.route("/signUp", methods=['POST'])
def register_user():
    data = request.get_json()
    password = data['password']  
    user = User(**data)     
    user.set_password(password)   
    try: 
        user.insert() 
        return jsonify({
            "success": "True",
            "user": user.format()
        })   
    except Exception as e:
        print(e)
        abort(400)