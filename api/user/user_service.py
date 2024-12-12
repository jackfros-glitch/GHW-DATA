from api.user.user import User

def get_public_user_details():
    return User(
        "This is a public user's page."
        )

def get_protected_user_details():
    return User(
        "This is a protected user's page."
    )

def get_admin_user_details():
    return Message(
        "This is an admin user's page."
    )
