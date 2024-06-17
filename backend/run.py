import sys
import os

# Add the dash_app directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dash_app')))

from app import create_app
from dash_app.index import create_dash_app

# Initialize Flask app
flask_app = create_app()

# Initialize Dash app
dash_app = create_dash_app(flask_app)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", debug=True)

