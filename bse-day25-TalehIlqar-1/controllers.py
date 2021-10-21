from flask import render_template, request
from app import app
from forms import ContactForm
from models import Contact



@app.route('/form', methods = ['GET', 'POST'])
def contact():
    post_data = request.form
    # print(post_data)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = post_data)
        if form.validate_on_submit():   
            contact = Contact(full_name = form.full_name.data, email = form.email.data, needed_services = form.needed_services.data, budget = form.budget.data, message = form.message.data)
            contact.save()
    return render_template('index.html', form = form)


