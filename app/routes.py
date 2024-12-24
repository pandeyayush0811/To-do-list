from app import app, mongo
# from bson import ObjectId
from app.models import Task  # Import the Task class from models.py

from flask import render_template, request, redirect, url_for

# # Home route - tasks dikhayega
# @app.route("/")
# def index():
#     # MongoDB se saare tasks laayenge
#     tasks = list(mongo.db.tasks.find())
#     return render_template("index.html", tasks=tasks)


# Home route to show all tasks
@app.route('/')
def index():
    tasks = Task.get_all()  # Fetch all tasks using the Task model
    return render_template('index.html', tasks=tasks)





# # Add task - naya task add karna
# @app.route("/add", methods=["POST"])
# def add_task():
#     task = request.form.get("task")  # Form se task liya
#     if task:
#         mongo.db.tasks.insert_one({"task": task, "completed": False})  # Task add kiya MongoDB mein
#     return redirect(url_for("index"))  # Home page pe redirect karenge


# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')  # Get task name from the form
    if task_name:
        task = Task(task_name)  # Create a Task object
        task.save()  # Save the task to the database
    return redirect(url_for('index'))



# # Complete task - task ko complete mark karna
# @app.route("/complete/<task_id>")
# def complete_task(task_id):
#     # mongo.db.tasks.update_one({"_id": mongo.ObjectId(task_id)}, {"$set": {"completed": True}})
#     mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
#     return redirect(url_for("index"))

# Route to mark a task as completed
@app.route('/complete/<task_id>')
def complete_task(task_id):
    Task.complete(task_id)  # Mark the task as completed using Task model
    return redirect(url_for('index'))





# # Delete task - task ko delete karna
# @app.route("/delete/<task_id>")
# def delete_task(task_id):
#     # mongo.db.tasks.delete_one({"_id": mongo.ObjectId(task_id)})
#     mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})

#     return redirect(url_for("index"))


# Route to delete a task
@app.route('/delete/<task_id>')
def delete_task(task_id):
    Task.delete(task_id)  # Delete the task using Task model
    return redirect(url_for('index'))