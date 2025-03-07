from flask import request, render_template, redirect, url_for, Blueprint

from blueprintapp.app import db
from .models import User

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
def index():
    user_data = User.query.all()
    return render_template('user/index.html', user = user_data)

@user.route('/create', methods=["GET","POST"])
def create_user():
    if request.method == "GET":
        return render_template('user/create.html')
    elif request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        job = job if job != '' else None
        
        person = User(name = name, age = age, job = job)
        db.session.add(person)
        db.session.commit()

        return redirect(url_for('user.index'))

