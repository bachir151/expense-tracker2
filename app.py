from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)

# Configurer la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Route de test
@app.route('/')
def home():
    return 'Welcome to the Expense Tracker!'

if __name__ == '__main__':
    app.run(debug=True)
