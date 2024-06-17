from flask import current_app as app

@app.route('/')
def home():
    return "Welcome to the Flask Backend!"
