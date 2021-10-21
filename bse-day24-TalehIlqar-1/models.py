from extensions import db
from datetime import datetime
from app import app

# a = Products(name="computer", description="some text", categories_id=2, amount=10, price=1000, production=2021)


class Products(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name =  db.Column(db.String(40), unique = True)
    description = db.Column(db.String(200), nullable = True)
    category_id = db.Column(db.Integer(), nullable = True)
    amount = db.Column(db.Float(), default = 0)
    price = db.Column(db.Float(), default = 0.00)
    production = db.Column(db.Integer())
    is_new = db.Column(db.Boolean(), default = False)
    rating = db.Column(db.Float(), default = 0.0) 
    created_at = db.Column(db.DateTime(), default = datetime.now()) 
    updated_at = db.Column(db.DateTime(), default = datetime.now()) 
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    

    def __repr__(self):
        return f'{self.id} | {self.name} | {self.price}'
    
    def __init__(self, name, description=None, amount=None, categories_id=None, price=None, production=None, is_new=None, rating=None):
        self.name = name
        self.description = description
        self.categories_id = categories_id
        self.amount = amount
        self.price = price
        self.production = production
        self.is_new = is_new
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()


class Categories(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name =  db.Column(db.String(30), unique = True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    # products = db.relationship("Products", backref="categories", lazy=True)

    def __repr__(self):
        return self.name    
    
    
     
    def __init__(self, name):
        self.name = name
        
    def save(self):
        db.session.add(self)
        db.session.commit()



    