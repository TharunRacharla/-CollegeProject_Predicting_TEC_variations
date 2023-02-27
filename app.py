from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
