from flask import jsonify
from flaskr.todo.model import Todo

def get_todo_list():
    todos=Todo.query.all()
    todo_list=[{"id":todo.id,"todo":todo.todo,"details":todo.details} for todo in todos] 

    return jsonify(todo_list)