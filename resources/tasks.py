
from flask import Blueprint, request, jsonify
from datetime import datetime
from database import tasks

task_bp = Blueprint('routes-tasks', __name__)

#Hemos creado este archivo para añadir aqui las funciones, para poder luego usar route hemos utilizado Blueprint
@task_bp.route('/tasks', methods=['POST']) #http://127.0.0.1:5000/tasks
def add_task():
    title = request.json['title']
    created_date = datetime.now().strftime("%x")

    data = (title, created_date)
    task_id = tasks.insert_task(data)

    if task_id:
        task = tasks.select_task_by_id(task_id)
        return jsonify({'task': task})
    return jsonify({'message': 'Internal Error'})

@task_bp.route('/tasks', methods=['GET'])
def get_task():
    data = tasks.select_all_tasks()

    if data:
        return jsonify({'tasks':data})
    elif data == False:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'tasks': {}})

@task_bp.route('/tasks', methods=['PUT'])
def update_task():
    title = request.json['title']
    id_arg = request.args.get('id')
    
    if tasks.update_task(id_arg, (title,)): #si tienes un topo, tienes que poderle despues una "," o da error.
        task = tasks.select_task_by_id(id_arg)
        return jsonify(task)    
    return jsonify({'message': 'Internal Error'})

@task_bp.route('/tasks', methods=['DELETE'])
def delete_task():    
    id_arg = request.args.get('id')
    
    if tasks.delete_task(id_arg):        
        return jsonify({'message': 'Task Deleted'})
    return jsonify({'message': 'Internal Error'})   

@task_bp.route('/tasks/completed', methods=['PUT'])
def complete_task():    
    id_arg = request.args.get('id')
    completed = request.args.get('completed')
    
    if tasks.complete_task(id_arg, completed):        
        return jsonify({'message': 'Well done'})
    return jsonify({'message': 'Internal Error'})   