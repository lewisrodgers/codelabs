from flask import Flask, jsonify, abort, make_response
import requests

app = Flask(__name__)

# In memory db
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Go to dinner',
        'description': u'Dinner at Hilary',
        'done': False
    }
]

@app.route('/todo/api/v1/tasks')
def get_tasks():
    return jsonify({'task': tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>')
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
