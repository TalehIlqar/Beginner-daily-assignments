from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError 
from extensions import db
from models import Contact

class ContactForm(FlaskForm):
    full_name = StringField(label = "Full name",  validators = [DataRequired(), Length(max = 30)])
    email = StringField(label = "Email",  validators = [DataRequired(),Email(), Length(max = 20)])
    needed_services = SelectField(label = "Needed Services", choices=[("Choose", "Choose"),("UI/UX", "UI/UX"), ("eCommerce", "eCommerce"), ("Choose", "Choose")], validate_choice = False)
    budget = SelectField(label = "Budget", choices=[("Select Budget", "Select Budget"),("2000 $", "2000 $"), ("2500 $", "2500 $"), ("3000 $", "3000 $")], validate_choice = False)
    message = StringField(label = "Message",  validators = [DataRequired()])



    # def validate_email(form, field):
    #     domain = field.data.split('@')[1]
    #     regdomains = db.session.query(Contact.id, Contact.email).filter(Contact.email != 'gmail.com').all()
    #     print(regdomains[2][1].split('@')[1])
    #     print(domain)
    #     if regdomains[2][1].split('@')[1] == domain:
    #         print('ela')
    #     else:
    #         raise ValidationError('Email address must be from an authorised domain')




