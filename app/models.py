from app import mongo
from bson.objectid import ObjectId

# Task Model Class
class Task:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def save(self):
        task_data = {
            "task": self.task,
            "completed": self.completed
        }
        return mongo.db.tasks.insert_one(task_data)

    @classmethod
    def get_all(cls):
        return list(mongo.db.tasks.find())

    @classmethod
    def get_by_id(cls, task_id):
        return mongo.db.tasks.find_one({"_id": ObjectId(task_id)})

    @classmethod
    def complete(cls, task_id):
        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})

    @classmethod
    def delete(cls, task_id):
        mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
