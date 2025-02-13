##########################################
# External Modules
##########################################

import os
from flask import Flask  
from flask_cors import CORS
from flask_talisman import Talisman

from api import exception_views
from api.user import user_views
from api.models.models import db, setup_db

from common.utils import safe_get_env_var

def create_app():
    ##########################################
    # Environment Variables
    ##########################################
    client_origin_url = safe_get_env_var("CLIENT_ORIGIN_URL")
   
    ##########################################
    # Flask App Instance
    ##########################################

    app = Flask(__name__, instance_relative_config=True)

    ##########################################
    # Database
    ##########################################

    setup_db(app)
    # db.drop_all()
    # db.create_all()


    ##########################################
    # HTTP Security Headers
    ##########################################

    csp = {
        'default-src': ['\'self\''],
        'frame-ancestors': ['\'none\'']
    }

    Talisman(
        app,
        force_https=False,
        frame_options='DENY',
        content_security_policy=csp,
        referrer_policy='no-referrer',
        x_xss_protection=False,
        x_content_type_options=True
    )


    @app.after_request
    def add_headers(response):
        response.headers['X-XSS-Protection'] = '0'
        response.headers['Cache-Control'] = 'no-store, max-age=0, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response

    ##########################################
    # CORS
    ##########################################

    CORS(
        app,
        resources={r"/api/*": {"origins": client_origin_url}},
        allow_headers=["Authorization", "Content-Type"],
        methods=["GET"],
        max_age=86400
    )

    ##########################################
    # Blueprint Registration
    ##########################################

    app.register_blueprint(user_views.bp)
    app.register_blueprint(exception_views.bp)

    return app
