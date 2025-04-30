from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime


# Charger les variables d'environnement
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)

# Configurer la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle pour une dépense
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Expense {self.description}: {self.amount}>'

# Initialiser la base de données
with app.app_context():
   db.create_all()

# Route de test
@app.route('/')
def home():
    return 'Welcome to the Expense Tracker!'

@app.route('/add_test_expense')
def add_test_expense():
    expense = Expense(amount=50.0, description="Test Expense")
    db.session.add(expense)
    db.session.commit()
    return 'Test expense added!'	

if __name__ == '__main__':
    app.run(debug=True)
