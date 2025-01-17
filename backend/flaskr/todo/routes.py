from flask import Blueprint

from flaskr.todo.controllers.get_todo_list import get_todo_list


todo_bp=Blueprint("todo",__name__)

todo_bp.route("/todos",methods=["GET"])(get_todo_list)