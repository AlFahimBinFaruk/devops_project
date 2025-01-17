import uuid
from flaskr import db


class Todo(db.Model):
    __tablename__="todo"

    id=db.Column(db.String(36),primary_key=True,nullable=False)
    todo=db.Column(db.String(100),nullable=False)
    details=db.Column(db.String(255))

    def __repr__(self):
        return f'<Todo {self.todo}'
    
    def __init__(self,todo,details):
        self.id=str(uuid.uuid4())
        self.todo=todo
        self.details=details