from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Emails


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/new_email', methods=['POST'])
def add_email():
    if not Emails.validate_emails(request.form):
        return redirect('/')
    #if not Emails.validate_email(request.form):
        #return redirect('/')
    data = {
        'theemail':request.form['theemail']
    }
    friends = Emails.save(data)
    return redirect('/email_list')
@app.route('/email_list')
def show():
    friends = Emails.get_all()
    return render_template('all_emails.html', all_emails = friends)