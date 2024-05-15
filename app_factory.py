from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app instance
app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

# Set the secret key for session security
app.config['SECRET_KEY'] = 'dfe7b0946804edf295050cbb8ce8d3aec72063aede88df37'

# Initialize SQLAlchemy to work with the Flask app
db = SQLAlchemy(app)

# Defineroutes and views below
@app.route('/')
def home():
    return 'Welcome to One Click Project'

# Add more routes and views as needed

if __name__ == "__main__":
    app.run(debug=True)
