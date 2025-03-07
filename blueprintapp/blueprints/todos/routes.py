from flask import request, render_template, redirect, url_for, Blueprint

from blueprintapp.app import db
from .models import Todo

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
    todo = Todo.query.all()
    return render_template('/todos/index.html', todos = todo)

@todos.route('/create', methods=["GET","POST"])
def create_todo():
    if request.method == "GET":
        return render_template('todos/create.html')
    elif request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        done = True if request.form.get('done') else False

        todo = Todo(title = title, description = description, done = done)
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todos.index'))

