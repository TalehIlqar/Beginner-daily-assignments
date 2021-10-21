from extensions import db
from datetime import datetime
from app import app



class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    full_name =  db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(30), nullable = False)
    needed_services = db.Column(db.String(30), nullable = False)
    budget = db.Column(db.String(30), nullable = False)
    message =  db.Column(db.Text, nullable = False)



    def __repr__(self):
        return self.full_name 
    
    def __init__(self, full_name, email,needed_services,budget, message):
        self.full_name = full_name
        self.email = email
        self.needed_services = needed_services
        self.budget = budget
        self.message = message
        

    def save(self):
        db.session.add(self)
        db.session.commit()

    
    