from dash_app.app import app

def create_dash_app(flask_app):
    app.init_app(flask_app)
    return app


